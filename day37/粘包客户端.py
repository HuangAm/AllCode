#coding:utf8
import socket,struct
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ts.connect(("192.168.16.116",8082))
while True:#通信循环
    msg=input(">>:").strip()
    if not msg:continue
    ts.send(msg.encode("utf-8"))#传数据的时候就是
    #收报头
    baotou=ts.recv(4)
    data_size=struct.unpack("i",baotou) #data_size现在就是数字
    #收数据
    recv_size=0
    recv_data=b""
    while recv_data < data_size:
        data=ts.recv(1024)
        recv_size+=data
ts.close()