#select通过IO多路复用解决soket并发问题
#server端
import socket
import select
sock=socket.socket()
sock.bind(("127.0.0.1",8080))
sock.listen(5)
inputs=[sock,]
while True:
    r,w,e=select.select(inputs,[],[])
    print(len(r))
    for obj in r:
        if obj == sock:
            conn,addr=obj.accept()
            print(conn)
            inputs.append(conn)
        else:
            data_byte=obj.recv(1024)
            print(data_byte.decode("utf8"))
            inp=input("回答%s号客户>>>"%inputs.index(obj))
            obj.sendall(inp.encode("utf8"))
    print(">>:",r)
