import pika
import sys
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel() #队列连接诶通道
channel.exchange_declare(exchange='logs',type='fanout')
message=" ".join(sys.argv[1:]) or "info:Hello World!"
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)
print(" [x] Sent %r" % message)
connection.close()