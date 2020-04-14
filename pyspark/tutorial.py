raw = ['{"name":"Drake"}','{"name":"Travis Scott"}','{"name":"Post Malone"}']
import json
for entry in raw:
    print(json.loads(entry)['name'])

#zepline은 gui로 설정이 가능하지만, 여기서는 설정해줘야 한다.
from pyspark import SparkContext
from pyspark import SQLContext
sc =SparkContext(master='local',appName='first app')

# 파이썬에서는 for로 돌면서 하지만, rdd는 한번에 mapping을 한다.
rdd = sc.parallelize(raw)
print(rdd.count())
print(rdd.map(json.loads).map(lambda  entry: entry['name'].collect()))
print(rdd.map(json.loads).map(lambda  entry: entry['name'].count()))


raw =SQLContext.read.format('parquet').load('')