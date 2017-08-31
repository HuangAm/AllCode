import pika, time

credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101')
connection = pika.BlockingConnection(parameters)

channel = connection.channel() #队列连接通道

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback,
                      queue='hello2',
                      # no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()