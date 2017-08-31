import socket
upsock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    inp=input(">>:")
    upsock.sendto(inp.encode("utf-8"),("127.0.0.1",8080))
    data,addr=upsock.recvfrom(1024)
    print(data.decode("utf8"))