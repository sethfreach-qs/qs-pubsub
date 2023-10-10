import os
import time
import csv
from json import dumps
from kafka import KafkaProducer


ordersFile = 'orders/orders.csv'

kaftka_server = os.environ['KAFKA_BROKER']
producer = KafkaProducer(
    bootstrap_servers=[kaftka_server],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)


while True:
    if os.path.isfile(ordersFile):
        print("Orders file found, processing...")
        with open(ordersFile, newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            for row in reader:
                record = {}
                for i, value in enumerate(row):
                    record[headers[i]] = value

                # send to original topic we have been listening to
                producer.send(os.environ['KAFKA_LOG_TOPIC'], value=record)

                # send to city specific topic
                producer.send(record['delivery_city'], value=record)

                # send financial information to a payment topic
                paymentData = {
                    "amount": record['product_price'],
                    "customer_name": record['customer_name']
                }
                producer.send("payment", value=paymentData)

                print(record)
        os.remove(ordersFile)
    time.sleep(1)
