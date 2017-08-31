# import socket
# us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     msg=input(">>:").strip()
#     us.sendto(msg.encode("utf-8"),("127.0.0.1",8080))
#     res,addr=us.recvfrom(1024)
#     print(res.decode("utf-8"))
# us.close()

#qq聊天客户端2
import socket
us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
qq_name_dic={
    "狗哥alex":("127.0.0.1",8080),
    "瞎驴":("127.0.0.1",8080),
    "一棵树":("127.0.0.1",8080),
    "武大郎":("127.0.0.1",8080),
}
while True:
    qq_name=input("请输入聊天对象：").strip()
    while True:
        msg=input("请输入聊天内容,按回车发送消息：").strip()
        us.sendto(msg.encode("utf-8"),qq_name_dic[qq_name])
        res,addr=us.recvfrom(1024)
        print("收到来自[%s:%s]的一条消息:\033[5;44m%s\033[5m" %(addr[0],addr[1],res.decode("utf-8")))
us.close()