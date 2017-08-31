import pika
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel() #队列连接诶通道
channel.exchange_declare(exchange='logs',type='fanout')
queue_obj = channel.queue_declare(exclusive=True)
#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = queue_obj.method.queue
print('queue_name****',queue_name,queue_obj)
channel.queue_bind(exchange='logs',queue=queue_name) #绑定对列和exchange
print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch,method,properties,body):
    print("[x] %r"%body)
channel.basic_consume(callback,queue=queue_name,no_ack=True)
channel.start_consuming()