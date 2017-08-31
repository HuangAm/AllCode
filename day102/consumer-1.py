import pika
import time

credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101')
connection = pika.BlockingConnection(parameters)

channel = connection.channel() #队列连接通道

def callback(ch,method,properties,body):
    print("[x] Recived %r" %body)#%r是用rper()方法处理对象,%s是根据str()方法处理对象
    print('msg handle done ...',body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    callback, #取到消息后,调用callback函数
    queue='hello',
    # no_ack=True, #消息处理后,不向rabbit-server确认消息已消费完毕
)

print('[x]Waiting for messages,To exit press CTRL+C')
channel.start_consuming() #阻塞模式