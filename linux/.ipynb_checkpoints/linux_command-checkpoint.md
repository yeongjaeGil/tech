ssh-login  
```
$ ssh <ID>@<IP> -p <port>
```

폴더 삭제
```
rm -rf <folderName>
```

폴더 이동
```
mv [DIR_old] [DIR_new]
```

폴더 복사
```
cp -r [DIR_old] [DIR_new]
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

포트  
```
sudo ufw allow [PID(ex:8000)]
    :포트 열기
losf -i:[PID(ex:8014)]
    :포트 확인
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

권한 변경
```
chown –R root:root <directory (ex:/data/yj)>
chown –R 777 <directory (ex:/data/yj)>
```

