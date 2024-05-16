# See Hello World! Example at
# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# running for Levi Lowther Module 3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello World!")
print(" [x] Sent 'Hello Brave New World!'")
connection.close()
