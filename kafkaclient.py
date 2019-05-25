# This script receives messages from a Kafka topic
from kafka import KafkaConsumer
consumer = KafkaConsumer(
    "Test123",
    bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
    client_id="Test",
    group_id="Test123",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)
raw_msgs = consumer.poll(timeout_ms=1000)
for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print("Test123")
consumer = KafkaConsumer(
"Forfun",
bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
client_id="Test1",
group_id="Forfun",
security_protocol="SSL",
ssl_cafile="ca.pem",
ssl_certfile="service.cert",
ssl_keyfile="service.key",
)
raw_msgs = consumer.poll(timeout_ms=1000)
for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print( messages)

consumer = KafkaConsumer(
    "Test1234",
    bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
    client_id="Test2",
    group_id="Test1234",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

raw_msgs = consumer.poll(timeout_ms=1000)
for tp, msgs in raw_msgs.items():
    for msg in msgs:
        print("Test1234")

