import socket
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ts.connect(("127.0.0.1",8080))
while True:
    msg=input(">>:").strip()
    if not msg:continue
    ts.send(msg.encode("utf8"))
    data=ts.recv(1024)
    print(data)
ts.close()