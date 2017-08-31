import pika
import time
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()#队列连接通道

def callback(ch,method,properties,body):
    print("[x] Received %r" %body)
    time.sleep(10)
    print('msg handle done ...',body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    callback,
    queue='hello2'
)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming() #阻塞模式