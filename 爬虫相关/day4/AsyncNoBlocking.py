import socket
import select

"""
select.select检测的不只socket对象而是有fileno方法的对象就行
select.select检测的就是fileno返回的文件描述符(整数),这是专门给系统提供的
"""

class Request(object): #这个类就是用来封装用的
    def __init__(self,sock,info):
        self.sock = sock
        self.info = info #把req_info封装到这里
    def fileno(self): #给Request封装fileno方法
        return self.sock.fileno()

class AsyncNoBlocking(object):
    def __init__(self):
        self.sock_list = []
        self.conns = []

    def add_request(self,req_info):
        """
        创建请求
        :return:
        """
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((req_info['host'],req_info['port']))
        except BlockingIOError as e:
            pass
        obj = Request(sock,req_info)
        self.sock_list.append(obj)
        self.conns.append(obj)

    def run(self):
        """
        开始时间循环,检测连接成功了么,数据是否返回
        :return:
        """
        while True:
            r,w,e = select.select(self.sock_list,self.conns,[],0.05) #最大超时时间0.05s
            #w,是否连接成功
            for obj in w:
                #检查obj是哪个字典
                data = "GET %s http/1.1\r\nhost:%s\r\n\r\n" %(obj.info['path'],obj.info['host'])
                obj.sock.send(data.encode('utf-8'))
                self.conns.remove(obj)
            for obj in r:
                #接收数据的对象
                response = obj.sock.recv(8096)
                # print(obj.info['host'],response)
                obj.info['callback'](response)
                self.sock_list.remove(obj)
            if not self.sock_list:
                #所有的请求已经反回
                break
