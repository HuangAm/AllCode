#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

import socket
import struct
import json
import os
downland_dir = r'D:\pycharm\Test1\Thrid_module\网络编程\文件传输\文件传输优化_函数版\客户端\dowland'
share_dir = r'D:\pycharm\Test1\Thrid_module\网络编程\文件传输\文件传输优化_函数版\客户端\share'

def get(client,cmd):
    '''
    用户下载功能
    :param client:
    :param cmd:
    :return:
    '''
    # 等待接收
    # 1、获取报头长度
    obj = client.recv(4)
    header_size = struct.unpack('i', obj)[0]
    # 2、获取报头内容
    header_bytes = client.recv(header_size)
    # 3、解析报头，获取真实数据长度
    header_data = header_bytes.decode('gbk')  # bytes解码成字符串
    header_dic = json.loads(header_data)  # 字符串反序列化为字典（报头）
    total_size = header_dic['total_size']  # 得到真实数据长度
    file_name = header_dic['file_name']
    # 4、接收真实数据
    with open('%s\%s' % (downland_dir, file_name), 'wb') as f:
        recv_size = 0
        while recv_size < total_size:
            line = client.recv(1024)
            f.write(line)
            recv_size += len(line)
            print('文件总大小：%s\t已下载大小：%s' % (total_size, recv_size))
def put(client,cmd):
    '''
    用户上传功能
    :param cmd:
    :return:
    '''
    # 1、制作报头
    file_name = cmd.split()[1]
    file_dic = {
        'file_name':file_name,
        'md5':'xxxxxxxx',
        'total_size':os.path.getsize('%s\%s'%(share_dir,file_name))
    }
    # 2、编辑并发送报头长度
    header_json = json.dumps(file_dic)
    head_bytes = header_json.encode('gbk')
    client.send(struct.pack('i',len(head_bytes)))
    # 3、发送报头信息
    client.send(head_bytes)
    # 4、发送真实数据信息
    with open('%s\%s'%(share_dir,file_name),'rb') as f:
        for line in f:
            client.send(line)
            # print('文件总大小为：%s\t已上传文件大小为：%s'%(file_dic['total_size'],))
def run():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8889))
    while True:
        cmd = input('输入下载(get)或上传(put)的文件及后缀名>>：').strip()
        if not cmd:continue
        client.send(cmd.encode('gbk'))
        res = cmd.split()[0]
        if res == 'get':
            print('你正在进行下载操作...')
            get(client,cmd)
        elif res == 'put':
            print('你正在进行上传操作...')
            put(client,cmd)

    client.close()
if __name__ == '__main__':
    run()
