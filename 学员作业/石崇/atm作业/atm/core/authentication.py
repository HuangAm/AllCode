#！/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import json
from config import settings

def load_data(account):
    '''根据account id 找到对应账户文件，并进行处理'''
    account_file = os.path.join(settings.DB_PATH,'%s.json'%account) # 传入用户信息文件
    if os.path.isfile(account_file):   #  文件是否存在
        f = open(account_file,'r',encoding='utf-8') # 打开文件
        data = json.load(f)                  # 获取信息
        f.close()
        return data               # 返回数据
    else:
        return {'error':'file does not exist'}  # 返回错误信息

def authenticate(account,password):
    ''' 验证用户是否登录'''
    account_data = load_data(account)
    if password == account_data['password']: # 判断密码是否匹配
        #print(password)
        return account_data          # 匹配成功就返回数据
    else:
        return 0                     # 匹配不成功就返回0，代表验证失败




