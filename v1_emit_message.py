"""
    This program sends a message to a queue on the RabbitMQ server.
    Levi Lowther Module 3
    16May2024

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))

# use the connection to create a communication channel
ch = conn.channel()

# use the channel to declare a queue
ch.queue_declare(queue="hello")

# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body="ECHO")

# print a message to the console for the user
print(" [x] Sent 'ECHO'")

# close the connection to the server
conn.close()
