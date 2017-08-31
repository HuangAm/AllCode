import socketserver
class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):#handle必须有，是放到__init__里面的
        print(self.request)

if __name__ == '__main__':
    obj=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FtpServer)
    obj.serve_forever()