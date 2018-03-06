#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

import json

def authentication(name,pwd,count):
    f = open('users_info.json', 'r')
    user_data = json.load(f)
   # print(user_data,count)
    if count < 4:
        if  name in user_data.keys() and user_data[name]['status']==1:
            if user_data[name]['pwd']==pwd:
                return {name,pwd}
    else:
        user_data[name]['status'] = 0
        f = open('users_info.json','w')
        json.dump(user_data, f)
        f.close()

def login():
    count = 1
    while count < 4:
        username = input('用户名：').strip()
        password = input('密码：').strip()
        auth = authentication(username,password,count)
        print(auth)
        if auth:
            print('welcome %s login !'%username)
            break
        else:
            count += 1
login()
'''
else:
     f = open('users_info.json', 'r')
     data = json.load(f)
     f =open('users_info.json', 'w')
     data[username]['status'] = 0
     json.dump(data,f)
     f.close()
'''






