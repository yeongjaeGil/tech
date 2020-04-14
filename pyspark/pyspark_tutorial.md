```
sudo apt-get install openjdk-8-jdk # 자바 설치
wget http://apache.mirror.cdnetworks.com/spark/spark-2.3.4/spark-2.3.4-bin-hadoop2.7.tgz
tar -xf spark-2.4.5-bin-hadoop2.7.tgz
ln -s spark-2.4.5-bin-hadoop2.7 spark # 이름 길어서 spark로 만든다.
pip3 install pyspark -U --no-cache
/etc/profile에다가
export PYSPARK_PYTHON=python3
alias pyspark=~/spark/bin/pyspark
```
[refe](https://m.blog.naver.com/PostView.nhn?blogId=semtul79&logNo=221489908486&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
- 데이터가 방대하게 들어날때 처리하는 방식에 문제가 생긴다.
    - mysql에서 지속적으로 들어나는데 전부다 처리해야 할 때
    - 속도, 비용적인 측면에서 문제가 있다.

- Apache Spark
    - Spark SQL
    - Spark Streaming
    - MLlib
    - GraphX
- Map Reduce
    - 데이터가 여러개로 쪼개져 있다.
    - 파티션을 통해서 데이터가 나눠져 있다
    - 어떤 식으로 데이터를 맵핑을(node) 할 것인지
    - 데이터를 병렬적으로 분산해서 처리한다.