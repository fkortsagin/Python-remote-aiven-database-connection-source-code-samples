from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='pg-1a2c0c5d-fjodor-0b37.aivencloud.com:15102')
for _ in range(25):

    producer.send('foobar', b'some_message_bytes');
# Block until a single message is sent (or timeout)
future = producer.send('foobar', b'another_message')
result = future.get(timeout=60);

# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()

