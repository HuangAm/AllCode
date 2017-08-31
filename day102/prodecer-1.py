import pika
#生产者要做的事情
'''
	1. 端口，ip,认证信息,端口默认5672
	2. 创建一个队列
	3. 往队列里发消息
	Linux上查看端口命令：netstat -tulnp
'''
credentials = pika.PlainCredentials('alex','alex3714') #简单的认证信息
parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials) #连接需要的参数
connection = pika.BlockingConnection(parameters) #真正建立连接
channel = connection.channel() #队列连接通道

#声明queue,或者说是创建对列
channel.queue_declare(queue='hello',durable=True) #durable是队列持久化,如果服务器
channel.basic_publish(exchange='',
                      routing_key='hello', #路由
                      properties = pika.BasicProperties(
                          delivery_mode=2 #2是消息持久化,1是消息非持久化
                      ),
                      body = 'Hello World2!'
                      )
print("[x] Sent 'Hello World!'")
connection.close()

