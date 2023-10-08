from time import sleep
from json import dumps
from kafka import KafkaProducer


topic = "test_topic"
kaftka_server = "localhost:9092"


producer = KafkaProducer(
    bootstrap_servers=[kaftka_server],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


for j in range(9999):
    print("Iteration", j)
    data = {'counter': j}
    producer.send(topic, value=data)
    sleep(0.2)
