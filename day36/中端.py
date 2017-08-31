import socket,subprocess,json
ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ts.bind(("127.0.0.1",8082))
ts.listen(5)
while True:
    conn,addr=ts.accept()
    while True:
        try:
            data=(conn.recv(1024)).decode("utf-8")
            print(data)
            res=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            a=res.stderr.read()
            b=res.stdout.read()
            if a:conn.send(a)
            if b:conn.send(b)
        except Exception:
            break
    conn.close()
ts.close()