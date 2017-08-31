import socket
sock=socket.socket()
sock.bind(("127.0.0.1",8080))
sock.listen(5)
while 1:
    conn,addr=sock.accept()
    conn.recv(1024)
    conn.send(b"HTTP/1.1 201 OK\r\n\r\nyuan")
    conn.close()