# import socket
# def main():
#     sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     sock.connect(('43.226.160.17',80))
#     sock.sendall(b"GET / HTTP/1.0\r\nhost: dig.chouti.com\r\n\r\n")
#     request = sock.recv(1024)
#     print("request",request.decode('utf-8'))
#     sock.close()
#
# main()

# import socket
# def main():
#     sock = socket.socket()
#     sock.connect(('43.226.160.17',80))
#     sock.sendall(b"GET / HTTP/1.1\r\nHost: dig.chouti.com\r\n\r\n")
#     request = sock.recv(1024)
#     print("request",request.decode('utf-8'))
#     sock.close()
#
# main()


# from functools import reduce
# l=list(range(100))
# print(l)
# print(reduce(lambda x,y:x+y,l))#默认初始值为0，看到的并不是真的，他还是直窜一个值，只是最开始有个默认的0
# print(reduce(lambda x,y:x+y,l,100))#默认初始值为100

# l = [1,2,3]
# l1 = [2,3,4]
# l.extend(l1)
# print(l)