#1 。 定义fib函数
#2. 声明接收指令的队列名rpc_queue
#3. 开始监听队列，收到消息后 调用fib函数
#4 把fib执行结果，发送回客户端指定的reply_to 队列
import subprocess
import pika
import time
credentials = pika.PlainCredentials('alex','alex3714')
parameters = pika.ConnectionParameters(host='192.168.0.101')
connection = pika.BlockingConnection(parameters)
channel = connection.channel() #队列连接通道
channel.queue_declare(queue='rpc_queue2')
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def run_cmd(cmd):
    cmd_obj=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result = cmd_obj.stdout.read()+cmd_obj.stderr.read()
    return result
def on_request(ch,method,props,body):
    n=int(body)
    print("[.] fib(%s)" %n)
    response = fib(n)
    # cmd=body.decode("utf-8")
    # print("[.] run (%s)" %cmd)
    # response=run_cmd(cmd)
    ch.basic_publish(exchange='',
                    routing_key=props.reply_to, #关键字
                    properties=pika.BasicProperties(correlation_id=props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag) # delivery_tag代表消息的索引
channel.basic_consume(on_request, queue='rpc_queue2')

print(" [x] Awaiting RPC requests")
channel.start_consuming()