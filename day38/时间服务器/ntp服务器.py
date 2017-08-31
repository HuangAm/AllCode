# from socket import *
# from time import strftime
# ip_port=("127.0.0.1",8080)
# bufsize=1024
#
# tcp_server=socket(AF_INET,SOCK_DGRAM)
# tcp_server.bind(ip_port)
#
# while True:
#     msg,addr=tcp_server.recvfrom(bufsize)
#     print("===>",msg)
#     if not msg:
#         time_fmt="%Y-%m-%d %X"
#     else:
#         time_fmt=msg.decode("utf-8")
#     back_msg=strftime(time_fmt)  #strftime把structtime变为formattime
#     tcp_server.sendto(back_msg.encode("utf-8"),addr)
# tcp_server.close()































