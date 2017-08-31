# import socket
# us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#产生一个udp对象
# us.bind(("127.0.0.1",8080)) #绑定ip+端口号，
# while True:
#     try:
#         res,addr=us.recvfrom(1024) #接收信息和客户端地址
#         print(res.decode("utf8"))
#         msg=input(">>:").strip()
#         us.sendto(msg.encode("utf-8"),addr) #发送信息和要发送的对象
#     except Exception:
#         break
# us.close()

# qq聊天服务端
import socket
ip_port=("127.0.0.1",8080)
udp_server_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server_sock.bind(ip_port)
while True:
    qq_msg,addr=udp_server_sock.recvfrom(1024)
    print("来自[%s:%s]的一条消息：\033[1;44m%s\033[0m"%(addr[0],addr[1],qq_msg.decode("utf-8")))
    back_msg=input("回复消息：").strip()
    udp_server_sock.sendto(back_msg.encode("utf-8"),addr)
udp_server_sock.close()


# import time
# class Student:
#     def __init__(self,name):
#         self.name = name
#     def study(self):
#         day63 = 0
#         while True:
#             if day63 == 150:
#                 time.sleep(2)
#                 print("就这样我们搞了150天Python...")
#                 break
#             print("吃饭")
#             print("睡觉")
#             print("学python")
#             day63 += 1
#         time.sleep(3)
#         print("开始了屌丝逆袭之路...")
#
# Student.study("像我一样的屌丝们")