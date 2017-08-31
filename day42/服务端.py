import time
import socket
tcp=socket.socket()
tcp.bind(("127.0.0.1",8080))
tcp.listen(5)
tcp.setblocking(False)
while True:
    try:
        print("waiting client connection ......")
        conn,addr=tcp.accept()  #进程主动轮询
        print("+++",addr)
        client_message=conn.recv(1024)
        print(client_message.decode("utf8"))
        conn.close()   #通信完成后直接断掉，
    except Exception as e:
        print(e)
        time.sleep(4)