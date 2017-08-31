#反射实现可插拔机制
class FtpClient:
    "ftp客户端，但是还没有实现具体功能"
    def __init__(self,addr):
        print("正在连接服务器[%s]" %addr)
        self.addr=addr
