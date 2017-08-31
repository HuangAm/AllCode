import socket
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('127.0.0.1',8081))
    sock.listen(5)
    while True:
        print("server is working.....")
        conn, address = sock.accept()
        request = conn.recv(1024)
        print("request",request.decode("utf8"))
        with open("index.html",encoding="utf8") as f:
            z=f.read()
        conn.sendall(b"HTTP/1.1 201 OK\r\n\r\n%s"%z.encode("utf8"))
        #浏览器编码问题，要下个插件，草草草
        conn.close()
if __name__ == '__main__':
    main()
