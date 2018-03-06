#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

import socket
import subprocess
import struct
import json
import os
share_dir = r'D:\pycharm\Test1\Thrid_module\网络编程\文件传输\文件传输优化_函数版\服务端\share'
recieve_dir = r'D:\pycharm\Test1\Thrid_module\网络编程\文件传输\文件传输优化_函数版\服务端\recieve'

def get(conn,cmd):
    # 执行客户端的命令，并返回执行后的信息
    # 1、解析客户端的指令，提取文件名
    data = cmd.decode('gbk').split()
    file_name = data[1]
    # 1、制作报头
    header_dic = {
        'file_name': file_name,  # 客户端需要下载的文件名
        'md5': 'xxxxxxxx',
        'total_size': os.path.getsize('%s\%s' % (share_dir, file_name))  # 服务端对应文件的大小
    }
    # 2、编辑并发送报头长度
    header_json = json.dumps(header_dic)  # 报头字典转字符串
    header_bytes = header_json.encode('gbk')  # 字符串转bytes
    conn.send(struct.pack('i', len(header_bytes)))  # 发送报头长度
    # 3、发送报头信息
    conn.send(header_bytes)
    # 4、发送真实数据
    with open('%s\%s' % (share_dir, file_name), 'rb') as f:
        for line in f:
            conn.send(line)
def put(cmd,conn):
    '''
    获取用户上传的内容
    :param cmd:
    :param conn:
    :return:
    '''
    # 1、接收报头的大小
    obj = conn.recv(4)
    header_size = struct.unpack('i', obj)[0]
    # 2、接收报头的信息
    head_bytes = conn.recv(header_size)
    # 3、解析报头信息并获取真实数据的大小
    head_data = head_bytes.decode('gbk') # bytes-->str
    head_dic = json.loads(head_data)  # str-->dict
    file_name = head_dic['file_name']
    total_size = head_dic['total_size']
    # 4、接收真实数据
    with open('%s\%s'%(recieve_dir,file_name),'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = conn.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('文件总大小为：%s\t已接收的文件大小为：%s'%(total_size,recv_size))

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8889))
    server.listen(5)
    while True:
        conn,client_addres = server.accept()
        while True:
            try:
                cmd = server.recv(1024)
                data = cmd.decode('gbk').split()
                if data[0] == 'get':
                    get(cmd,conn)
                elif data[0] == 'put':
                    put(cmd,conn)

            except ConnectionResetError:
                break
        conn.close()
    server.close()

if __name__ == '__main__':
    run()


