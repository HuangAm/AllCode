#！/usr/bin/env python3
#-*- coding:utf-8 -*-

'''
此模块是程序的主要的逻辑交互程序
'''

from core import authentication
from db import account
from core import transaction
from shopping_mall import shopping_cart

def user_info(user_initial):
    ''' 查看账户信息'''
    print('ACCOUNT INFO'.center(30,'-'))
    for k,v in user_initial['data'].items(): # 将字典转为列表
        if k != 'password':
            print('%10s :%s'%(k,v))
    print('END'.center(30,'-'))

def with_draw(user_initial):
    ''' 账户提现 '''
    exit_flag = False
    while not exit_flag:   # 不退出就可以一直取
        print('\033[32;1m你正在进行账户提现...\033[0m')
        print('你当前的账户余额：',user_initial['data']['balance'])
        wd_money = input('提取金额：').strip()  # 用户输入取款金额
        if not wd_money:continue             # 未输入时等待
        elif wd_money.isdigit() and int(wd_money) > 0:  # 取款为整数且大于0
            if float(wd_money)*(1+0.05) <= (user_initial['data']['balance']/2): # 小于账户余额
                wd_money = int(wd_money)
                transa_result = transaction.transac_tion(user_initial,'withdraw',wd_money) # 返回交易后的结果
                print('你现在的账户余额：\033[33;1m%s\033[0m'%transa_result,'按b返回，q退出')
            else:
                print('\033[31;1m你的账户余额不足！\033[0m')
        elif wd_money == 'b':
            exit_flag = True   # 取款结束
        else:
            print('\033[31;1m你的取款金额不符合要求！\033[0m')

def re_pay(user_initial):
    ''' 用户还款 '''
    print('\033[32;1m你正在进行账户还款...\033[0m')
    print('你当前的账户余额：', user_initial['data']['balance'])
    rp_money = input('还款金额：').strip()  #
    if rp_money.isdigit() and int(rp_money) > 0:
        rp_money = int(rp_money)
        transa_result = transaction.transac_tion(user_initial,'repay',rp_money)
        print('你现在的账户余额：\033[33;1m%s\033[0m'%transa_result,'按q退出')

def trans_fer(user_initial):
    ''' 账户转账 '''
    print('\033[32;1m你正在进行账户转账...\033[0m')
    print('你当前的账户余额：', user_initial['data']['balance'])
    tra_choice = input('请输入转账用户id>>:').strip()      # 转账的目标用户id
    if tra_choice.isdigit() and int(tra_choice)!= user_initial['data']['id']:
        tra_choice = int(tra_choice)                     # 转为整型
        if tra_choice >= 1 and tra_choice < 4:
            tf_money = input('转帐金额：').strip()              # 转账金额
            if tf_money.isdigit() and int(tf_money) > 0:         # 判断转帐金额是否符合要求
                tf_money = int(tf_money)
                transa_result = transaction.transac_tion(user_initial,'transfer',tf_money,tra_choice)
                print('你现在的账户余额：\033[33;1m%s\033[0m'%transa_result,'按q退出')
            else:
                print('\033[31;1m你转账的金额不合法！\033[0m')
        else:
            print('\033[31;1m你输入的账户id不存在!\033[0m')



def con_sume(user_initial):
    '''用户购物后结账接口'''
    print('\033[32;1m你正在进入购物商城...\033[0m')
    print('你当前的账户余额：', user_initial['data']['balance'])
    cart = {}               # 新建一个字典存储传入的商品
    exit_flag = False      # 退出标志
    while not exit_flag:    # 循环直到 exit_flag = True
        cart = shopping_cart.shop() # 选择的商品放入字典中
        #print(cart)
        cs_money = input('付款金额：').strip()  # 输入付款金额
        if cs_money.isdigit() and float(cs_money) > 0:  # 判断输入是否合法
            cs_money = float(cs_money)                  # 将字符串转为浮点数
            if cs_money == float(cart['price']):        # 判断付款是否等于商品价格
                transa_result = transaction.transac_tion(user_initial,'consume',cs_money) # 传入参数并返回结果
                print('你现在的账户余额：\033[33;1m%s\033[0m'%transa_result,'按b返回，q退出')
                user_initial['data']['shopping_cart'].append(cart)  # 将购买的商品加入账户存储
            else:
                print('\033[31;1m你输入的金额有误！\033[0m')
        elif cs_money == 'b': # 退出循环
            exit_flag = True
        else:
            print('\033[31;1m你输入的金额有误！\033[0m')

functions = [                     # 将功能选项写成字典
    ['账户信息',user_info],
    ['提现',with_draw],
    ['存款',re_pay],
    ['转账',trans_fer],
    ['购物',con_sume]
]
def control(user_initial):  # 让用户选择不同的功能
    while True:          # 循环打印选项列表
        for k,index in enumerate(functions) :
            print('\033[32;1m%s   %s\033[0m'%(k,functions[k][0]))
        choice = input('请输入序号选择对应的服务>>:').strip()     # 用户输入
        if not choice:continue                                 # 未输入时等待
        elif choice.isdigit():                      # 输入为整数时继续
            choice = int(choice)
            if choice >= 0 and choice < 5:           # 判断选项是否在列表中
                functions[choice][1](user_initial)   # 执行相关功能
        elif choice == 'q':                         # 输入 q 退出
            exit('Bye')
        else:
            print('\033[31;1m Invalid input!\033[0m')  # 输入错误


def login_entry():
    '''用户从此处登录，最多可尝试三次'''
    user_initial = {
        # 记录用户的初始状态
        'authentication_enter':False,
        'data':None            # 初始无用户数据
    }
    count = 1   # 计数器
    while user_initial['authentication_enter'] is False:
        usename = input('用户id：').strip()
        password = input('密码：').strip()
        auth_return = authentication.authenticate(usename,password)  # 对用户名和密码进行验证并返回
        if auth_return: # 用户通过验证
            user_initial['authentication_enter'] = True  # 更改初始状态
            user_initial['data'] = auth_return           # 返回数据更改初始状态
            print('Welcome login!')
            control(user_initial)                        # 调用其他功能
        else:
            print('\033[31;1mInvalid usename or password,please try again...\033[0m')
        count += 1
        if count > 3:
            print('\033[31;1mYou haved tried too much times!!!\033[0m')
            break




