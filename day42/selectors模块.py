import selectors
import socket
soc=socket.socket()
soc.bind(("127.0.0.1",8080))
soc.listen(5)
soc.setblocking(False)
sel=selectors.DefaultSelector()#根据具体平台选择最佳IO多路机制，比如Linux选择epoll
def read(conn,mask): #通信函数
    try:   #针对Windows客户端突然断开
        data=conn.recv(1024)
        # if not data: 结局Linux上的客户端突然断开
        #     sel.unregister(conn)
        #     return
        print(data.decode("utf8"))
        data2=input(">>:")
        conn.send(data2.encode("utf8"))
    except Exception:
        sel.unregister(conn)
def accept(soc,mask):
    conn,addr=soc.accept()
    sel.register(conn,selectors.EVENT_READ,read)
sel.register(soc,selectors.EVENT_READ,accept) #注册，这里可以理解为封装
#注册把套接字对象和所对应的方法封装到一起这里可以理解为封装到key中
#key.data就是通信函数或者链接函数
#key.fileobj就是文件描述符：服务端套接字或conn
while True:
    events=sel.select() #监听  [(key1,mask1),(key2,mask2)....]
    for key,mask in events:
        func=key.data #通信函数或连接函数
        obj=key.fileobj #文件描述符：服务端套接字soc或conn
        func(obj,mask) #accept(sock,mask)    read(conn,mask)



# import selectors
# import socket
# sock=socket.socket() #默认TCP套接字对象
# sock.bind(("127.0.0.1",8080))
# sock.listen(5)
# sock.setblocking(False)
# conn,addr=sock.accept()
# data=conn.recv(1024)
# print(data.decode("utf8"))
# back_data=input(">>:")
# conn.send(back_data.encode("utf8"))

















