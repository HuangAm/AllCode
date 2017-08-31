# from socket import *
# ip_port=("127.0.0.1",8080)
# bufsize=1024
#
# udp_client=socket(AF_INET,SOCK_DGRAM)
#
# while True:
#     msg=input("请输入时间格式(例%Y %m %d)>>: ").strip()
#     udp_client.sendto(msg.encode("utf-8"),ip_port)
#     data=udp_client.recv(bufsize)
#     print(data.decode("utf-8"))
# udp_client.close()
# for i in "hello":
#     print(i,end="")
#     print(i)
