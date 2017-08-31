import socket,subprocess
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ts.connect(("127.0.0.1",8081))
while True:
    msg=input(">>:").strip()
    if not msg:continue
    ts.send(msg.encode("utf8"))
    data=ts.recv(1024)
    print(data.decode("gbk"))
ts.close()