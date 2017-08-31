import pika

credentials = pika.PlainCredentials('alex', 'alex3714') #认证

parameters = pika.ConnectionParameters(host='192.168.11.92',credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel() #队列连接通道

#声明queue
channel.queue_declare(queue='hello2')

channel.basic_publish(exchange='',
                      routing_key='hello2', #路由
                      body='Hello World2!')

print(" [x] Sent 'Hello World!'")


connection.close()
