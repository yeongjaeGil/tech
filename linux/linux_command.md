ssh-login
<code>
$ ssh [ID]@[IP] -p [port]
</code>

가상환경 정리
<code>
pip install virtualenv
virtualenv [가상환경명]
source [가상환경명]bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt
</code>

프로세스 확인:keyword
<code>
ps -ef|grep [keyword (ex:python)]
</code>

포트확인
<code>
losf -i:[PID(ex:8014)]
</code>
해당 포트 프로세스 죽이기
<code>
lsof -i:8014|ps -ef|xargs kill -9 
</code>
좀비 죽이기
<code>
ps -ef | grep defunct | awk '{print $3}' | xargs kill -9
</code>
버퍼비우기
<code>
echo 3 > /proc/sys/vm/drop_caches
</code>