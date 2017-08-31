import pika

credentials = pika.PlainCredentials('alex', 'alex3714')

parameters = pika.ConnectionParameters(host='192.168.11.92',credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel() #队列连接通道


def callback(ch, method, properties, body):
    print(" [x] Received %r" % ch, method, properties, body)

channel.basic_consume(callback, #取到消息后，调用callback 函数
                      queue='hello2',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming() #阻塞模式
