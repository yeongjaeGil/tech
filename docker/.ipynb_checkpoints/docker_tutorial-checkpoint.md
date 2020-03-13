## Docker
---

#### 도커 관리

0) docker hub 이용[IMAGE]
```
sudo docker login
sudo docker pull [ID]/[IMAGE]
tag 바꾸기
sudo docker push [ID]/[IMAGE]:tag
```

1) 컨테이너 생성
```
mkdir –p /data/[USERNAME]/notebook
sudo chown –R super:super /data/[USERNAME]
sudo NV_GPU=0,1 nvidia-docker run -td --restart unless-stopped -p [PORT]:8888 -p [PORT]:6006 -p [PORT]:22 -v /data/[USERNAME]:/data:rw -v /data/shared:/data/[USERNAME]/notebook/shared --shm-size=1g --name [USERNAME] [IMAGE]
*8888: 주피터 포트 **6006: 텐서보드 포트 ***22: ssh 포트
sudo nvidia-docker exec –it [USERNAME] passwd admin
```
2) 컨테이너 삭제
```
sudo docker stop [ID]
sudo docker rm [ID]
```

3) 도커 빌드
### Dockerfile 