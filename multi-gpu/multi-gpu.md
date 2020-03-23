
cta Parallel이라는 기능 제공
- 1) 모델을 각 GPU에 복사해서 할당
- 2) 매 iteration 마다 batch를 GPU의 개수만큼 분할(scatter)
- 3) GPU 에서 forward 과정을 진행
- 4) 각 입력에 대해 모델이 출력을 내보내면 이 출력들을 하나의 GPU로 모은다(gather)
- 5) Loss function을 통해 loss를 계산하고 back-propagation
    - back-propagation은 각 GPU에서 수행하며 그 결과로 각 GPU에 있던 모델의 gradient를 구할 수 있음.
    - 만약 4개의 GPU를 사용한다면 4개의 GPU에 각각 모델이 있고 각 모델은 계산된 gradient를 가지고 있음.
    - 모델 업데이트를 위해 GPU에 있는 gradient를 또 하나의 GPU로 모아서 업데이트 진행
    - Adam 같은 경우는 gradient를 모은 다음 추가 연산 이후 업데이트
```python
import torch.nn as nn
model = nn.DataParallel(model)
```
####과정
- replicate -> scatter -> Parallel_apply -> gather 순서로 진행
    - 여기서 gather는 한 GPU에서 각 모델의 출력을 모아주기 때문에 하나의 gpu의 메모리 사용량이 많을 수 밖에 없음.
```python
def data_parallel(module, input, device_ids, output_device):
    replicas = nn.parallel.replicate(module, device_ids)
    inputs = nn.parallel.scatter(input, device_ids)
    replicas = replicas[:len (inputs)]
    outputs = nn.parallel.parallel_apply(replicas, inputs)
    return nn.parallel.gather(outputs, output_device)
```

```python
import torch
import torch.nn as nn
model = BERT(args)
model = torch.nn.DataParallel(model)
model.cuda()
'''
#data loader
'''
for i, (inputs, labels) in enumerate(trainloader):
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
- [BERT 코드](https://github.com/codertimo/BERT-pytorch)
- 문제점: 하나의 GPU가 상대적으로 많은 메모리를 사용하면 batch size를 많이 키울 수 없다.
- batch size는 학습 성능에 영향을 주는 경우가 많아서 메모리 사용 불균형은 꼭 해결해야할 문제다.
---
#### 해결책
- 간단한 방법: 단순히 출력을 다른 GPU로 모은다. 
    - default(0)로 설정되어 있는 GPU는 gradient 또한 해당 GPU로 모이기 떄문에 다른 GPU에 비해 메모리 사용량이 상당히 많다.
    - 출력을 다른 GPU로 모으면 메모리 사용량의 차이를 줄일 수 있다.
```python
import os
import torch.nn as nn
on.environ["CUDA_VISIBLE_DEVISES"] = '0,1,2,3'
model = nn.DataParallel(model, output_device = 1)
```
- 여전히 제대로 사용하지 못한다. (GPU-Util을 보면)

## Custom으로 DataParallel  사용
- PyTorch-Encoding 패키지
    - GPU의 메모리 사용량이 늘어나는 것은 모델의 출력을 하나의 GPU로 모으는 작업 때문이다.
    - why?) 모델의 출력을 사용해서 loss function을 계산해야하기 떄문이다.
    - solution) loss function 또한 병렬로 연산하도록 만들면 메모리 불균형 문제를 어느정도 해결가능
```python
from torch.nn.parallel.data_parallel import DataParallel

class DataParallelCriterion(DataParallel):
    def forward(self, inputs, *targets, **kwargs):
        targets, kwargs = self.scatter(targets, kwargs, sefl.device_ids)
    replicas = self.replicate(self.module, self.device_ids[:len(inputs)])
        targets = tuple(targets_per_gpu[0] for targets_per_gpu in targets)
        outputs = _criterion_parallel_apply(replicas, inputs, targets, kwargs)
        return Reduce.apply(*outputs) / len(outputs), targets
```
- DataParallelCriterion을 사용 할 경우에 일반적으로 DataParallel로 모델을 감싸면 안된다.
- DataParallel은 기본적으로 하나의 GPU로 출력을 모으기 때문이다.
- 그러므로 Custom DataParallel 클래스인 DataParallelModel을 사용한다
- Pytorch-Encoding 패키지의 parallel.py파일만 가져오면 됨
```python
import torch
import torch.nn as nn
from parallel import DataParallelModel, DataParallerlCriterion
model = BERT(args)
model = DataParallelModel(model)
model.cuda()

criterion = nn.NLLLoss()
criterion = DataParallelCriterion(criterion)

for i, (inputs, labels) in enumerate(trainloader):
    outputs = model(inputs)
    loss = criterion(outputs, labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```
## 100%까지 GPU 성능 올리기
- Pytorch에서 Distributed 패키지 사용
- multi-GPU 학습을 할 때도 분산 학습을 사용할 수 있다.
- [tutorial 읽어보기](https://pytorch.org/tutorials/intermediate/dist_tuto.html)
- [ImageNet 예제](https://github.com/pytorch/examples/blob/master/imagenet/main.py)의 main.py에서 multi-GPU 관련 부분 정리
    - main.py를 실행하면 main이 실행되는데 main은 다시 main_worker 들을 multi-processing으로 실행
```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel

def main():
    args = parser.parse_args()
    ngpus_per_node = torch.cuda.device_count()
    args.world_size = ngpus_per_node * args.world_size
    mp.spawn(main_worker, nprocs = ngpus_per_node, args = (ngpus_per_node, args)

def main_worker(gpu, ngpus_per_node, args):
    global best_acc1
    args.gpu = gpu
    torch.cuda.set_device(args.gpu)
    print("Use GPU: {} for training" . format(args.gpu))
    args.rank = args.rank * ngpus_per_node + gpu
    dist.init_process_group(backend = 'nccl', init_method = 'tcp://127.0.0.1:FREEPORT', world_size=args.world_size, rank=args.rank)
model = Bert()
model.cuda(args.gpu)
model = DistributedDataParallel(model, device_ids = [args.gpu])
acc = 0
for i in range(args.num_epochs):
    model = train(model)
    acc = test(model, acc)

```
# branch4
# branch4
# branch4
# branch4

