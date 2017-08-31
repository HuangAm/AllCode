# import socket
# phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# phone.connect(("127.0.0.1",8080))
#
# phone.send("hello".encode("utf-8"))
#
# data=phone.recv(1024)
# print(data)
#
# phone.close()



# import socket
# ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ts.connect(("127.0.0.1",8080)) #对应服务端的accpet
# while True: #通信循环
#     msg=input(">>:").strip()
#     if not msg:continue
#     ts.send(msg.encode("utf8")) #像服务端发数据
#     data=ts.recv(1024) #接收服务端处理过的消息
#     print(data)
#
# ts.close()


import socket
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(ts)
ts.connect(("127.0.0.1",8081))
print(ts)
while True:
    msg=input(">>:")
    ts.send(msg.encode("utf8"))
    data=ts.recv(1024)
    print(data)
ts.close()






















