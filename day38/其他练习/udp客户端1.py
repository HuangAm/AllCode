# import socket
# us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     msg=input(">>:").strip()
#     us.sendto(msg.encode("utf-8"),("127.0.0.1",8080))
#     res,addr=us.recvfrom(1024)
#     print(res.decode("utf-8"))
# us.close()

#qq聊天客户端1
import socket
us=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
qq_name_dic={
    "狗哥alex":("127.0.0.1",8080),
    "瞎驴":("127.0.0.1",8080),
    "一棵树":("127.0.0.1",8080),
    "武sir":("127.0.0.1",8080),
}
while True:
    qq_name=input("请选择聊天对象：").strip()#不能放到底下的循环里，因为每次跟同一个人聊天不应该都输入一次聊天对象
    while True:
        msg=input("请输入消息，回车发送：").strip()
        if msg=="quit":break
        if not msg or not qq_name or qq_name not in qq_name_dic:continue
        us.sendto(msg.encode("utf-8"),qq_name_dic[qq_name])
        res,addr=us.recvfrom(1024)
        print("来自[%s:%s]的一条消息:\033[1;44m%s\033[0m" %(addr[0],addr[1],res.decode("utf8")))
us.close()