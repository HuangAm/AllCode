#思考题
# class Person:
#     def __init__(self,name,age,sex,weight):
#         self.name=name
#         self.sex=sex
#         self.age=age
#         self.weight=weight
#     def __eq__(self,other):
#         if self.name==other.name and self.sex == other.sex:
#             return True
#     def __hash__(self):
#         return (self.name,self.sex).__hash__()
#     # def __str__(self):
#     #     return str(self.__hash__())
#
# a1=Person("alex",18,"male",59)
# a2=Person("alex",30,"male",60)
# print(set([a1,a2]))

# class Person:
#     def __init__(self,name,age,sex,weight):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.weight=weight
#     def __eq__(self, other):
#         if self.name==other.name and self.sex==other.sex:
#             return True
#     def __hash__(self):
#         return (self.name,self.sex).__hash__()
#
# p1=Person("alex",18,"male",56)
# p2=Person("alex",18,"male",56)
# print(set([p1,p2]))

#4 基于对列实现一个生产者消费者模型，要求：队列内元素不能超过5个，一旦有五个元素了，生产者不再生产，其他内容   自由扩散
# import queue
# import threading
# q=queue.Queue()
#
# def producer(q):
#     num=1
#     while True:
#         if q.qsize()<5:
#             q.put(num)
#             num+=1
# def consumer(q):
#     while True:
#         if not q.empty():
#             print("get:",q.get())
# pro=threading.Thread(target=producer,args=(q,))
# con=threading.Thread(target=consumer,args=(q,))
# pro.start()
# con.start()

#socketserver模块
import socket
import selectors
sock=socket.socket()
sock.bind(("127.0.0.1",8080))
sock.listen(5)
sel=selectors.DefaultSelector() #默认选择最好的IO多路复用处理机制
def read(fd,mask):
    try:
        data=fd.recv(1024)
        print(data.decode("utf8"))
        msg=input(">>:")
        fd.send(msg.encode("utf8"))
    except Exception:
        sel.unregister(fd)
    return

def accept(fd,mask):
    conn,addr=fd.accept()
    sel.register(conn,selectors.EVENT_READ,read)
sel.register(sock,selectors.EVENT_READ,accept) #注册
while True: #循环监听，通信循环和链接循环
    events=sel.select()  #监听事件
    for key,mask in events:  #events是一个元组
        func=key.data #这就是属性
        fd=key.fileobj #这就是套接字对象
        func(fd,mask) #运行函数








