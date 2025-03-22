pip install s3fs

import pandas as pd
from kafka import KafkaConsumer
from time import sleep
from json import dumps
from json import loads
import requests
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'demo_test1',
     bootstrap_servers=['18.217.20.39:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()

 for c in consumer:
    print(c.value)

for count, i in enumerate(consumer):
    with s3.open("s3://kafka-bucket-vamsi/weather_updates_{}.json".format(count), 'w') as file:
        json.dump(i.value, file) 

