# import socket
# sock=socket.socket()
# sock.bind(("127.0.0.1",8080))
# sock.listen(5)
# while True:
#     conn,addr=sock.accept()
#     request=conn.recv(1024)
#     print(request)
#     with open("index.html",encoding="utf8") as f:
#         data=f.read()
#     conn.sendall(b"HTTP/1.1 201 OK\r\n\r\n%s" %data.encode("utf8"))
#     conn.close()
