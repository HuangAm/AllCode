# import time
# import socket
# sk=socket.socket()
# while True:
#     sk.connect(("127.0.0.1",8080))
#     print("hello")
#     sk.sendall(bytes("hello","utf8"))
#     time.sleep(2)
#     break

#client端
# import socket
# sock=socket.socket()
# sock.connect(("127.0.0.1",8080))
# while True:
#     data=input(">>:")
#     sock.send(data.encode("utf8"))
#     rece_data=sock.recv(1024)
#     print(rece_data.decode("utf8"))
# sock.close()
