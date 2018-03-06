#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong
import sys
import os
from conf.settings import *
from core.Teacher import Teacher
from core.Admin import Admin
from core.Student import Student
def login():
    '''
    用户登录，判断账户类型，并验证
    登陆成功后，查看身份确定进入何种视图
    :return:
    '''
    menu = {
        1:'admin',
        2:'teacher',
        3:'student'
    }
    print('\033[32;0m选择身份登录...\033[1m')
    for k,index in enumerate(menu):
        print(index,menu[index])
    status = int(input('>>>:').strip())
    count = 0
    while count < LOGIN_TRY:
        if status == 1 or status == 2:
            user = input('用户名：').strip()
            pwd = input('密码：').strip()
            with open( userinfo,'r',encoding='utf-8') as f:
                for line in f:
                    user_name,password,role = line.strip('\n').split('-')
                    if user_name == user and password == pwd:
                        print('\033[32;0m 登录成功\033[1m ')

                        return {'role':role,'name':user}
                else:
                    print('\033[31;1m用户名或密码错误\033[0m')
        elif status == 3:
            list = ['注册','登录']
            for index,i in enumerate(list):
                print(index,i)
            chance =int(input('输入序号>>：').strip())
            if chance == 0:
                user = input('用户名：').strip()
                pwd = input('密码：').strip()
                with open(userinfo,'a',encoding='utf-8') as f:
                    f.write('%s-%s-Student\n'%(user,pwd))
                    print('\033[32;1m恭喜%s注册成功\033[0m'%user)
                    return {'role': 'Student', 'name': user}
            if chance == 1:
                user = input('用户名：').strip()
                pwd = input('密码：').strip()
                with open(userinfo, 'r', encoding='utf-8') as f:
                    for line in f:
                        user_name, password, role = line.strip('\n').split('-')
                        if user_name == user and password == pwd:
                            print('\033[32;0m 登录成功\033[1m ')

                            return {'role': role, 'name': user}
                    else:
                        print('\033[31;1m用户名或密码错误\033[0m')

        else:
            print('\033[31;1m选项不存在\033[0m')
        count += 1

def main():
    '''
    登陆成功后，欢迎。
    打印相应身份可调用的功能
    实例化一个对应身份的对象，调用相关功能
    :return:
    '''
    print('欢迎来到选课系统')
    lg_re = login()
    print(lg_re)

    if lg_re:
        role_class = getattr(sys.modules[__name__],lg_re['role']) # 根据反射本模块中的admin文件中角色内容反射对应的角色类
        obj = role_class(lg_re['name'],[],[])  # 实例化一个对应用户的对象
        # print(sys.modules[__name__])
        while True:
            for index,k in enumerate(role_class.menu,1):
                print(index,k[0])  # 打印功能列表
            try:
                retry = int(input('请输入对应操作的序号(按''b''退出)：').strip())
                if retry == 'b':
                    exit('Bye')
                else:
                    getattr(obj,role_class.menu[retry-1][1])() # 反射，调用对象相对应的函数功能
            except Exception as e:
                print('输入内容有误',e)



# menu = {
#     1:'userinfo',
#     2:'teacher_obj',
#     3:'student'
# }
# status = int(input('>>>:').strip())
# print(menu[status])