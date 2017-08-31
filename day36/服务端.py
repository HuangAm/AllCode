# import socket
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #买手机
# phone.bind(("192.168.16.12",8280)) #绑定手机卡
# phone.listen(5)
#
# print("starting....")
# conn,addr=phone.accept() #等待电话连接
#
# print("电话线路是",conn)
# print("客户端的手机号是",addr)
# data=conn.recv(1024)  #收消息
# print("客户端发来的消息是",data.decode("utf8"))
#
# conn.send(data.upper())
# conn.close()
# phone.close()
# import socket
# ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #拿到TCP套接字，产生一个socket对象
# ts.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #解决高并发
# ts.bind(("127.0.0.1",8080)) #绑定服务器IP和端口
# ts.listen(5)  #？5，不能设成死的，应该写到配置文件里
# print("starting....")
# while True: #链接循环
#     conn,addr=ts.accept() #等客户端发请求
#     print("接收线路是", conn)  # conn是套接字的连接对象
#     print("客户端的ip地址", addr)
#     while True: #通信循环
#         try: #应对Windows客户端自己关闭后解决服务器崩溃的问题
#             data=conn.recv(1024) #接收请求，最大1024字节，从缓存里面收，这个值设大了也没有意义
#             if not data:break #应对Linux客户端自己关闭后服务端陷入死循环的问题
#             print("客户端发来的消息是",data)
#             conn.send(data.upper())
#         except Exception:
#             break
#     conn.close()
# ts.close()
# import socket
# ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ts.bind(("127.0.0.1",8080))
# ts.listen(5)
# while True:
#     conn,addr=ts.accept() #到这里tcp套接字干的事就完了，以后的都叫给了链接对象，接受链接
#     print(ts.accept())
#     print("接收的路线是",conn)
#     print("客户的ip地址是",addr)
#     while True:
#         try:
#             data=conn.recv(1024)#收到data包
#             if not data:break
#             print("客户发来的消息是",data)
#             conn.send(data.upper())#发送处理后data包
#         except Exception:
#             break
#     conn.close()
# ts.close()

import socket
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(ts)
ts.bind(("127.0.0.1",8081))
print(ts)
ts.listen(5)
while True:
    cd=ts.accept()
    print(cd)
    conn,addr=cd
    # print("链接对象",conn)
    # print("用户端ip地址",addr)
    while True:
        try:
            data=conn.recv(1024) #recv中必须有一个参数
            if not data:break
            print("收到的包是",data)
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
ts.close()

























