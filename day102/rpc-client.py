# 1.  声明一个队列，作为reply_to返回消息结果的队列
# 2.  发消息到队列，消息里带一个唯一标识符uid，reply_to(服务端执行命令结果放置的队列)
# 3.  监听reply_to 的队列，直到有结果
import queue

import pika
import uuid

# class CMDRpcClient(object):
#     def __init__(self):
#         credentials = pika.PlainCredentials('alex', 'alex3714')
#         parameters = pika.ConnectionParameters(host='192.168.0.101',credentials=credentials)
#         self.connection = pika.BlockingConnection(parameters)
#         self.channel = self.connection.channel()
#
#         result = self.channel.queue_declare(exclusive=True)
#         self.callback_queue = result.method.queue #命令的执行结果的queue
#
#         #声明要监听callback_queue
#         self.channel.basic_consume(self.on_response, no_ack=True,
#                                    queue=self.callback_queue)
#
#     def on_response(self, ch, method, props, body):
#         """
#         收到服务器端命令结果后执行这个函数
#         """
#         if self.corr_id == props.correlation_id:
#             self.response = body.decode("gbk") #把执行结果赋值给Response
#
#     def call(self, n):
#         self.response = None
#         self.corr_id = str(uuid.uuid4()) #唯一标识符号
#         self.channel.basic_publish(exchange='',
#                                    routing_key='rpc_queue2',
#                                    properties=pika.BasicProperties(
#                                          reply_to = self.callback_queue,
#                                          correlation_id = self.corr_id,
#                                          ),
#                                    body=str(n))
#
#         while self.response is None:
#             self.connection.process_data_events()  #检测监听的队列里有没有新消息，如果有，收，如果没有，返回None
#             #检测有没有要发送的新指令
#         return self.response
#
# cmd_rpc = CMDRpcClient()
# print(" [x] Requesting fib(30)")
# response = cmd_rpc.call('ipconfig')
#
# print(response)


class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('alex', 'alex3714')
        parameters = pika.ConnectionParameters(host='192.168.0.101', credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive = True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,queue=self.callback_queue)
    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body
    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue2',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id = self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonnacci_rpc = FibonacciRpcClient()
print("[x] Requesting fib(30)")
response=fibonnacci_rpc.call(30)
print("[.]Got %r" %response)

