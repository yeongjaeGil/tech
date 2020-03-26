MULTI-GPU
---
- GPU 정보 확인
```
$ nvidia-smi
```
- multi-GPU 원리
![ex_screenshot](img/multi-gpu-process.png)
```
    - 여러개 GPU를 사용하려면 모델을 각 GPU에 할당
    - scatter: iteration 마다 batch를 GPU개수 만큼 나눔
    - gather: 하나의 GPU로 모음

```
import torch.nn as nn
model = nn.DataParallel(model)
```
