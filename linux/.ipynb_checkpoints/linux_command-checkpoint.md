ssh-login  
```
$ ssh <ID>@<IP> -p <port>
```
폴더 삭제
```
rm -rf <folderName>
```
버퍼확인
```
free -h
```
GPU 확인
```
nvidia-smi
```
가상환경  
```
pip install virtualenv
virtualenv <virtual_envs>
source <virtual_envs>bin/activate

conda create --n [virtual_envs] python=3.6.4
source active <virtual_envs>

pip freeze > requirements.txt
pip install -r requirements.txt

```

프로세스 확인:keyword  
```
ps -ef|grep [keyword (ex:python)]
```

포트확인  
```
losf -i:[PID(ex:8014)]
```

해당 포트 프로세스 죽이기  
```
lsof -i:[PID(ex:8014)]|ps -ef|xargs kill -9 
```

좀비 죽이기  
```
ps -ef | grep defunct | awk '{print $3}'|xargs kill -9
```

버퍼비우기  
```
echo 3 > /proc/sys/vm/drop_caches
```


