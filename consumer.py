from time import sleep
from json import loads
from kafka import KafkaConsumer


topic = "test_topic"
kaftka_server = "localhost:9092"


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[kaftka_server],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)


for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(0.2)
