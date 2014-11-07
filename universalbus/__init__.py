import pika
import json


class EventSender(object):
    def __init__(self, login, password, host, virtual_host, exchange='kit'):
        self.exchange = exchange
        conn_params = pika.ConnectionParameters(
            host=host,
            virtual_host=virtual_host,
            credentials=pika.PlainCredentials(login, password)
        )
        self.connection = pika.BlockingConnection(conn_params)

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, type='topic')

    def __del__(self):
        self.connection.close()

    def push(self, routing_key, message):
        dumped_message = json.dumps(message)
        self.channel.basic_publish(exchange=self.exchange, routing_key=routing_key, body=dumped_message)
