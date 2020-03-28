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

계정 추가
```
sudo useradd -m [ID]
sudo passwd [ID]
```

사용자 변경
```
su [ID]
```

sudo 권한 주기
```
vi /etc/sudoers
root ALL=(ALL:ALL) ALL
[ID] ALL=(ALL:ALL) ALL
```

#### 로그인 
1. (로컬) 내 컴퓨터의 지문을 암호화
    - 1. ssh-keygen
    - 2. ~/.ssh 폴더 만들어 졌는 지 확인
    - 3. .pub 공유
2. (로컬) config 설정하기
    - 1. .ssh 폴더에 config 파일 만들기 (ssh rlfdudwo 같은 설정을 위해 쓰임)
    - 2. vi config 이후 
```
    HOST rlfdudwo
        HostName xxx.xx.xx.xxx
        Port xxxx
        User rlfdudwo
```
3. (서버) 내 지문을 서버에 알려주기
    - 1. ~/.ssh/authorized_keys 파일 있는 지 없는 지 확인
    - 2. 없다면 mkdir .ssh
    - 3. Touch ~/.ssh/authorized_keys
    - 4. (로컬) cat ~/.ssh/id_rsa.pub |pbcopy
    - 5. (서버) vi ~/.ssh/authorized_keys
    - 6. 제일 상단에 붙여 넣기 한 뒤 저장
