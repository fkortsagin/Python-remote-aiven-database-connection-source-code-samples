from kafka import KafkaProducer
import time

HollywoodProducer = KafkaProducer(
    bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)


for e in range(0,230):
    message = "message number {}".format(e)
    print("Sending: {}".format(message))
HollywoodProducer.send("Test1234",message.encode("utf-8"))
time.sleep(0)
# Wait for all messages to be sent
HollywoodProducer.flush()
