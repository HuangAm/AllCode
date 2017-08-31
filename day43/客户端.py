# import socket
# sock=socket.socket()
# sock.connect(("127.0.0.1",8080))
# while True:
#     data=input("input>>:")
#     sock.send(data.encode("utf8"))
#     rece_data=sock.recv(1024)
#     print(rece_data.decode("utf8"))
# sock.close()