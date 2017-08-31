#coding:utf8
#----初始代码------------------------------------------------------------------
# import socket,subprocess
# ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ts.bind(("127.0.0.1",8082))
# ts.listen(5)
# while True:
#     conn,addr=ts.accept()
#     while True:
#         try:
#             data=(conn.recv(1024)).decode("utf-8")
#             print(data)
#             res=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#             a=res.stderr.read()
#             b=res.stdout.read()
#             # if a:conn.send(a)
#             # if b:conn.send(b)
#             conn.send(a)
#             conn.send(b)
#         except Exception:
#             break
#     conn.close()
# ts.close()
#----解决粘包问题的代码-------------------------------------------------
#我们要模拟报头为我们自己写的软件做一个报头，报头一定是固定字节，一定要有data的长度
# 比如我们现在要给客户端发一个包，客户端如果不知道包的长度就会造成粘包
#所以解决思想就是让客户端知道要接受的数据的长度，按长度去接收，就不会粘包
import socket,subprocess,struct,json
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ts.bind(("127.0.0.1",8082))
ts.listen(5)
while True: #链接循环
    conn,addr=ts.accept() #接受链接，conn是连接对象，addr是客户端的ip地址
    while True: #通信循环
        try:
            data=(conn.recv(1024)).decode("utf-8")
            print(data)
            if not data:break #解决Linux系统中，客户端意外关闭导致服务端一直收空
            res=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            a=res.stderr.read()
            b=res.stdout.read()
            data_size=len(a)+len(b) #计算出字节长度数字
            #发送报头部分
            data_bytes=struct.pack("i",data_size) #将字节长度数字打包成固定4个字节的bytes
            conn.send(data_bytes)
            #发送数据部分
            conn.send(a)
            conn.send(b)
        except Exception:
            break
    conn.close()
ts.close()
