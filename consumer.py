import time
from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "topic name",
        bootstrap_servers = '192.168.1.1:22222',
        auto_offset_reset = 'earliest',
        enable_auto_commit = True,
        group_id = "consumer-group-a")
    print('kafka initiated')

for msg in consumer:
    print("Registered User = {}".format(json.loads(msg.value)))
    time.sleep(10)
