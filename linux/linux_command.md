ssh-login  
```
$ ssh [ID]@[IP] -p [port]
```

가상환경 정리  
```
pip install virtualenv
virtualenv [가상환경명]
source [가상환경명]bin/activate
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
lsof -i:8014|ps -ef|xargs kill -9 
```
좀비 죽이기  
```
ps -ef | grep defunct | awk '{print $3}' | xargs kill -9
```
버퍼비우기  
```
echo 3 > /proc/sys/vm/drop_caches
```
