# import socketserver
#
# class FTPserver(socketserver.BaseRequestHandler): #通讯
#     def handle(self):
#         print("====>",self)
#         print(self.request)
#         while True: #通信循环
#             data=self.request.recv(1024)
#             print(data)
#             self.request.send(data.upper())
#
# if __name__=="__main__":
#     obj=socketserver.ThreadingTCPServer(("127.0.0.1",8080),FTPserver)#建立一个新的tcp线程
#     obj.serve_forever() #链接循环
import socketserver

class Ftpserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('==========>',self)
        print(self.request)
        while True:    #通信链接
            data = self.request.recv(1024)
            print(data.decode('utf8'))
            self.request.send(data.upper())

if __name__ == '__main__':
    obj = socketserver.ThreadingTCPServer(('127.0.0.1',8080),Ftpserver)
    obj.serve_forever()#链接循环
