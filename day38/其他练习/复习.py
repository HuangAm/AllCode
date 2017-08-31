# import socket
# socket.socket(socket_family,socket_type,protocal=0)
# socket_family 可以是AF_UNIX或AF_INET。socket_type可以是SOCK_STREAM 或 SOCK_DGRAM.protocol一般不填，默认值为0

#获取tcp/ip套接字
#tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取udp/ip套接字
#udpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#由于socket模块中有太多的属性，我们在这里破例使用了“from module import *"语句。使用
#“from socket import *”,我们就把socket模块里的所有属性都带到我们的命名空间里，这样能
#大幅缩短我们的代码。

#例如tcpSock=socket(AF_INET,SOCK_STREAM)

'''
1.用打电话的流程快速描述socket通信
2.服务端和客户端加上基于一次链接的循环通信
3.客户端发送空，卡主，证明是哪个位置卡的
'''

#tcp服务端：
# from socket import *
# phone=socket(AF_INET,SOCK_STREAM) #拿到tcp/ip套接字
# phone.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #加入一条socket配置，重用ip和端口
# phone.bind(("127.0.0.1",8080)) #参数是ip+端口号的元组
# phone.listen(5) #服务端最多挂起链接数
# while True: #链接循环
#     conn,addr=phone.accept() #conn是链接对象，addr是客户端的ip+端口号
#     while True: #通信循环，就是recv和send
#         try:
#             data=conn.recv() #接收需要有个参数buffersize
#             print(data.decode("utf8"))
#             conn.send(data.upper()) #发包,这个时候是操作系统发的,所以编码格式也是操作系统默认的
#         except Exception:
#             break
#     conn.close()
# phone.close()

#tcp客户端
# from socket import *
# phone=socket(AF_INET,SOCK_STREAM)#拿到一个tcpsocket对象
# phone.connect(("127.0.0.1",8080)) #建立连接
# while True: #通信循环
#     msg=input(">>:")
#     if not msg:continue
#     phone.send(msg.encode("utf8"))
#     res=phone.recv(1024) #接收需要一个参数buffersize
#     print(res.decode("gbk")) #如果是Windows系统就用gbk,如果是Linux就用utf-8
# phone.close()

#udp服务端
# import socket
# udp_server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udp_server_socket.bind(("127.0.0.1",8080))
# while True:#通信循环，udp接收和发送都是两个值，都是先信息，后地址
#     res,addr=udp_server_socket.recvfrom(1024)
#     print(res.decode("utf-8"))
#     udp_server_socket.sendto(res.upper(),addr)
# udp_server_socket.close()

#udp客户端
# import socket
# us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:#通行循环
#     msg=input(">>:")
#     us.sendto(msg,("127.0.0.1",8080))
#     res,addr=us.recvfrom(1024)
#     print(res.decode("utf8"))
# us.close()
# from time import *
# print(strftime("%Y %m %d"))
#-*-coding:utf-8-*-
# __author__="Wuyongqiang"
# import socket
# bufsize=1024
# ip_port=("127.0.0.1",8080)
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# res=s.connect(ip_port)
# while True:
#     msg=input(">>:").strip()
#     if len(msg) == 0:continue
#     if msg == "quit":break
#     s.send(msg.encode("utf-8"))
#     act_res=s.recv(bufsize)
#     print(act_res.decode("utf-8"),end="")
#-*-coding:utf-8-*-
# __author__="Wuyongqiang"
# from socket import *
# import subprocess
# ip_port=("127.0.0.1",8080)
# bufsize=1024
# udp_server=socket(AF_INET,SOCK_DGRAM)
# udp_server.bind(ip_port)
# while True:
#     #收消息
#     cmd,addr=udp_server.recvfrom(bufsize)
#     print("用户命令--->",cmd)
#     #逻辑处理
#     res=subprocess.Popen(cmd.decode("utf-8"),
#                          shell=True,
#                          stderr=subprocess.PIPE,
#                          stdout=subprocess.PIPE,
#                          )
#     err=res.stderr.read()
#     print("错误===>",err)
#     if err:
#         back_msg=err
#     else:
#         back_msg=res.stdout.read()
#     print("返回结果",back_msg)
#     #发消息
#     udp_server.sendto(back_msg,addr)
# udp_server.close()

from socket import *
ip_port=("127.0.0.1",8080)
bufsize=1024

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input(">>:").strip()
    udp_client.sendto(msg.encode("utf-8"),ip_port)
    data,addr=udp_client.recvfrom(bufsize)
    print(data.decode("utf-8"),end="")




















