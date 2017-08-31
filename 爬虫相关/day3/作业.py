import socket
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('43.226.160.17',80))
    sock.sendall(b"GET / HTTP/1.0\r\nhost: dig.chouti.com\r\n\r\n")
    request = sock.recv(1024)
    print("request",request.decode('utf-8'))
    sock.close()

main()