import socket
import struct
import json
import os
import sys


class MYTCPClient:
    address_family = socket.AF_INET  # 套接字对象的参数
    socket_type = socket.SOCK_STREAM  # 代表TCP
    allow_reuse_address = False  # 不允许，地址重用，不允许多线程
    max_packet_size = 8192  # 一次接受8192字节
    coding = "utf8"  # 编码格式 utf-8
    request_queue_size = 5  # 连接池的个数为5

    def __init__(self, server_address, connect=True):  # 初始化函数
        self.server_address = server_address  # ip+端口号
        self.socket = socket.socket(self.address_family, self.socket_type)  # 拿到套接字对象
        if connect:  # connect为真
            try:
                self.client_connect()  # 建立连接
            except:
                self.client_close()  # 关闭连接
                raise

    def client_connect(self):  # 建立连接函数
        self.socket.connect(self.server_address)

    def client_close(self):  # 关闭连接
        self.socket.close()

    def run(self):  # 主函数
        while True:
            inp = input(">>:").strip()  # 输入如：put a.txt  get b.txt
            if not inp: continue
            if self.login():
                l = inp.split()  # 把输入的内容以空格分开，[0]是命令，[1]是文件名
                cmd = l[0]  # 拿到命令
                if hasattr(self, cmd):  # 自省
                    func = getattr(self, cmd)
                    func(l)
            else:
                return

    def put(self, args):  # 上传，把文件一行行上传到服务端，服务端需要有存放路径，存放往后要告诉客户端成功上传
        cmd = args[0]  # args就是上面的l列表args[0]就是命令
        filename = args[1]  # args[1]就是文件名
        if not os.path.isfile(filename):  # 如果文件不存在
            print("file:%s is not exists" % filename)
            return
        else:
            filesize = os.path.getsize(filename)  # 获得文件大小，即多少字节
        head_dic = {
            "cmd": cmd,
            "filename": os.path.basename(filename),
            "filesize": filesize,
        }  # 自定义报头
        head_json = json.dumps(head_dic)  # 把报头变为json字符串以便实现跨网络传输
        head_json_bytes = bytes(head_json, encoding=self.coding)  # 把json字符串编码成utf-8二进制
        head_struct = struct.pack("i", len(head_json_bytes))  # 把报头的json字符串的字节长度压缩为固定长度
        self.socket.send(head_struct)  # 发送报头的json字符串的字节长度的压缩包，server端可以从这里面拿到len(head_json_bytes)
        self.socket.send(head_json_bytes)  # 发送报头的json字符串的字节，服务端可以根据len(head_json_bytes)拿到head_json_bytes
        # 又可以通过head_json_bytes拿到自定义的报头字典，从字典中拿到filesize，通过filesize拿到真正的文件
        send_size = 0
        with open(filename, "rb") as f:  # 直接以rb的形式读出来，省得编码
            for line in f:
                self.socket.send(line)  # 发送真正的文件
                send_size += len(line)
                persent = int((send_size / filesize) * 100)
                s = "\r%s%% %s" % (persent, "#" * persent)
                sys.stdout.write(s)
                sys.stdout.flush()
            else:
                print("upload successful")

    def get(self, args):  # 下载地方自己放
        cmd = args[0]  # 拿到命令
        filename = args[1]  # 拿到文件名
        head_dic = {
            "cmd": cmd,
            "filename": filename
        }  # 自定义报头
        head_json = json.dumps(head_dic)  # 将报头转为json字符串
        head_json_bytes = bytes(head_json, encoding=self.coding)  # 将json字符串进行编码
        head_struct = struct.pack("i", len(head_json_bytes))  # 编码后的json字符串长度压缩为固定四个字节
        self.socket.send(head_struct)  # 发固定四个字节
        self.socket.send(head_json_bytes)  # 发json字符串
        data = self.socket.recv(10)
        if data.decode("utf8") == "n":
            print("The file not found!")
            return
        else:
            data = self.socket.recv(4)
            data_len = struct.unpack("i", data)[0]
            head_json = self.socket.recv(data_len).decode("utf8")
            head_dic = json.loads(head_json)
            filesize = head_dic["filesize"]
            recv_size = 0
            with open(filename, "wb") as f:
                while recv_size < filesize:
                    recv_data = self.socket.recv(self.max_packet_size)
                    f.write(recv_data)
                    recv_size += len(recv_data)
                    # print("recvsize:%s filesize:%s" %(recv_size,filesize))
                    persent = int((recv_size / filesize) * 100)
                    s = "\r%d%% %s" % (persent, "#" * persent)
                    sys.stdout.write(s)
                    sys.stdout.flush()
                print("download successful")

    def login(self):
        name = input("please input username:")
        password = input("please input password:")
        head_dic = {
            "name": name,
            "password": password,
            "cmd": "login"
        }
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding="utf8")
        head_struct = struct.pack("i", len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        data = self.socket.recv(1)
        if data.decode("utf8") == "y":
            print("login successful!")
            return 1
        else:
            print("login defeated")
            return 0

    def check(self, args):
        head_dic = {
            "cmd": "check"
        }
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding=("utf8"))
        head_struct = struct.pack("i", len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        data = self.socket.recv(1024)
        print(data.decode("gbk"))

    def changedir(self, args):
        cmd = args[0]
        dirname = args[1]
        head_dic = {
            "cmd": "changedir",
            "dirname": dirname
        }
        head_json = json.dumps(head_dic)
        head_json_bytes = bytes(head_json, encoding="utf8")
        head_struct = struct.pack("i", len(head_json_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_json_bytes)
        data = self.socket.recv(self.max_packet_size)
        print(data.decode("gbk"))


client = MYTCPClient(("127.0.0.1", 8080))  # 实例化后就建立了链接,拿到了套接字
client.run()
