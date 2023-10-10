import os
import time
from json import loads
from kafka import KafkaConsumer


topic = os.environ['KAFKA_TOPIC']
kaftka_server = os.environ['KAFKA_BROKER']


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[kaftka_server],
    auto_offset_reset='latest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("Listening to topic: " + topic)

total = 0

for event in consumer:
    event_data = event.value

    name = event_data['customer_name']
    price = event_data['amount']
    total += float(price)
    totalS = "{:.2f}".format(total)
    print(f"charged {name} {price}. Total revenue to date: £{totalS}")

    # print(event_data)
    time.sleep(1)
