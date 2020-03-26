- 여러대의 서버에서 horovod를 사용하면
- 묶어서 전체의 성능을 땡겨서 사용할 수 있다.
- 테스트 해보기
```
설치하고 운용하는게 쉽지 않을 거 같긴하다.
```

```python
import torch
import horovod.torch as hvd

# Initialize Horovod
hvd.init()

# Pin GPU to be used to process local rank (one GPU per process)
torch.cuda.set_device(hvd.local_rank())

# Define dataset...
train_dataset = ...

# Partition dataset among workers using DistributedSampler
train_sampler = torch.utils.data.distributed.DistributedSampler(
    train_dataset, num_replicas=hvd.size(), rank=hvd.rank())

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=..., sampler=train_sampler)

# Build model...
model = ...
model.cuda()

optimizer = optim.SGD(model.parameters())

# Add Horovod Distributed Optimizer
optimizer = hvd.DistributedOptimizer(optimizer, named_parameters=model.named_parameters())

# Broadcast parameters from rank 0 to all other processes.
hvd.broadcast_parameters(model.state_dict(), root_rank=0)

for epoch in range(100):
   for batch_idx, (data, target) in enumerate(train_loader):
       optimizer.zero_grad()
       output = model(data)
       loss = F.nll_loss(output, target)
       loss.backward()
       optimizer.step()
       if batch_idx % args.log_interval == 0:
           print('Train Epoch: {} [{}/{}]\tLoss: {}'.format(
               epoch, batch_idx * len(data), len(train_sampler), loss.item()))
