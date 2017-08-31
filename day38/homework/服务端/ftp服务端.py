import socketserver
import struct
import json
import os
import subprocess
class FtpServer(socketserver.BaseRequestHandler):
    coding="utf8" #编码格式
    server_dir="file_upload" #目录
    max_packet_size=1024 #一次收1024字节
    BASE_DIR=os.path.dirname(os.path.abspath(__file__)) #在这里是目录homework
    def handle(self):
        try:
            # print(self.request) #self.request就是conn
            while True:  #通信循环
                data = self.request.recv(4) #收字json字典头长度的压缩包
                data_len=struct.unpack("i",data)[0] #解压包得到json字典的长度，data是一个元组里面就有一个元素的元组，
                head_json=self.request.recv(data_len).decode(self.coding) #收到json字典解码成json字符串
                head_dic=json.loads(head_json) #通过json.loads把json字符串转为字典
                print(head_dic) #打印自定义的文件头(字典)内容
                cmd=head_dic["cmd"] #客户端输入的put get命令
                if hasattr(self,cmd): #自省
                    func=getattr(self,cmd)
                    func(head_dic) #运行相应的函数
        except Exception:
            pass
    def put(self,args): #上传
        file_path = os.path.join(self.BASE_DIR,self.name, args["filename"])  # 新建一个空文件
        filesize=args["filesize"] #通过自定义的报头字典拿到文件的字节数
        recv_size=0
        # print("--->",file_path)
        with open(file_path,"wb") as f: #直接以wb形式写进去
            while recv_size < filesize: #当接收字节小于文件字节时，开始接收
                recv_data=self.request.recv(self.max_packet_size) #conn.recv(1024)
                f.write(recv_data) #写入文件
                recv_size += len(recv_data) #累计接收数据的长度
                print("recvsize:%s filesize:%s" %(recv_size,filesize)) #这里要做百分比
    def get(self,args): #下载
        filename=args["filename"]
        file_path = os.path.join(self.BASE_DIR, self.name, filename)
        if not os.path.exists(file_path):
            self.request.send("n".encode("utf8"))
            return
        else:self.request.send("y".encode("utf8"))
        filesize=os.path.getsize(file_path)
        head_dic={
            "filesize":filesize,
        }
        head_json=json.dumps(head_dic)
        head_json_bytes=bytes(head_json,encoding=self.coding)
        head_struct=struct.pack("i",len(head_json_bytes))
        self.request.send(head_struct)
        self.request.send(head_json_bytes)
        send_size=0
        with open(file_path,"rb") as f:
            for line in f:
                self.request.send(line)
                send_size+=len(line)
                print(send_size)
    def login(self,args):
        name=args["name"]
        pwd=args["password"]
        with open("db",encoding="utf8") as f:
            dic=eval(f.read())
            for i in dic:
                if name == i:
                    if int(pwd) == dic[name]:
                        self.request.send("y".encode("utf8"))
                        self.name=name
                    else:self.request.send("n".encode("utf8"))
    def check(self,args): #当前用户 self.name
        file_path=os.path.join(self.BASE_DIR,self.name)
        os.chdir(file_path)
        res = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
        a=res.stdout.read()
        self.request.send(a)
    def changedir(self,args):
        dirname=args["dirname"]
        file_path=os.path.join(self.BASE_DIR,self.name,dirname)
        os.chdir(file_path)
        print(file_path)
        res = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
        a = res.stdout.read()
        print(a)
        self.request.send(a)

ftpserver=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FtpServer) #每有一次链接建立，就多一个线程
ftpserver.serve_forever() #链接循环













