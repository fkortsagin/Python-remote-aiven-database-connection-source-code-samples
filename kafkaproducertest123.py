# This script connects to Kafka and send a few messages

from kafka import KafkaProducer
import time
HollywoodProducer = KafkaProducer(
    bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)


for i in range(9999):
    message = "message number {}".format(i)
    print("Sending: {}".format(message))
HollywoodProducer.send("Test123",message.encode("utf-8"))
time.sleep(0)
# Wait for all messages to be sent
HollywoodProducer.flush()

# This script connects to Kafka and send a few messages

