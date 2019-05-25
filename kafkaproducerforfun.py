from kafka import KafkaProducer
import time

HollywoodProducer = KafkaProducer(
    bootstrap_servers="kafka-193a4a83-fjodor-0b37.aivencloud.com:15104",
    security_protocol="SSL",
    ssl_cafile="ca.pem",
    ssl_certfile="service.cert",
    ssl_keyfile="service.key",
)

n = 443243
for c in range(n + 1):
    message = "message number {}".format(c)
    print("Paging Dr,Howard: {}".format(message))
HollywoodProducer.send("Forfun",message.encode("utf-8"))
time.sleep(0)
# Wait for all messages to be sent
HollywoodProducer.flush()

