from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])

producer.send('topic', key=b'cool', value=b'eh?')
producer.flush()
producer.close()
