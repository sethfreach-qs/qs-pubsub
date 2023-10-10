import os
import time
from json import loads
from kafka import KafkaConsumer


topic = os.environ['KAFKA_TOPIC']
kaftka_server = os.environ['KAFKA_BROKER']


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[kaftka_server],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("Listening to topic: " + topic)

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    time.sleep(1)
