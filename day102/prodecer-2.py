import pika
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel() #队列连接诶通道

#声明queue或创建queue
channel.queue_declare(queue='hello2',durable=True)
channel.basic_publish(
    exchange='',
    routing_key='hello2',#路由
    properties=pika.BasicProperties(
        delivery_mode=2,
    ),
    body='Hello World2!',
)
print("[x] Sent 'Hello World2!'")
connection.close()