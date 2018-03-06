# _author_ : yong
# date : 2017/1/18

import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)
import json
import time
import display
import credit_port

buy_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
user_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'user.json')
goods_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'goods_file')

def register():
    print('进入注册页面')
    users_info = open(user_file, 'r+', encoding='utf-8')
    while True:
        user_name = input('请输入用户名：').strip()
        user_pass = input('请输入密码：').strip()
        credit = input('请绑定一张信用卡：').strip()
        for user_item in users_info:
            user_item = json.loads(user_item.strip())
            if user_item['name'] == user_name:
                print('\033[41m用户名已存在！\033[0m')
                break
        else:
            user_item['name'] = user_name
            user_item['pwd'] = user_pass
            user_item['credit'] = int(credit)
            user_item['log'] = {}
            users_info.write('\n')
            users_info.write(json.dumps(user_item))
            print('\033[41m注册成功,回到登陆列表\033[0m')
            break
    users_info.close()


def logon():
    print('进入登录页面')
    for i in range(3):
        users_info = open(user_file, 'r', encoding='utf-8')
        user_name = input('请输入用户名：')
        user_pass = input('请输入密码：')
        for user_item in users_info:
            user_item = eval(user_item.strip())
            if user_item['name'] == user_name:
                if user_item['pwd'] == user_pass:
                    print('\033[41m登录成功！\033[0m')
                    users_info.close()
                    shop_menu(user_item)
                else:
                    print('\033[41m用户名或密码错误！\033[0m')
                    break
        else:
            print('\033[41m用户名不存在！\033[0m')
            continue
        if logon_authentication:
            break
        else:
            users_info.close()
            print('\033[41m三次失败退出\033[0m')
            exit()


def logout(user_item):
    exit()


def log_list(user_item):
    pass


def shopping(user_item):
    goods, goods_list = load_goods()
    my_goods = []
    cost = 0
    account = user_item['credit']

    while True:
        print(goods_list)
        goods_num = input('>>>:')
        if goods_num.isdigit():
            goods_num = int(goods_num)
            goods_price = goods[goods_num - 1]['price']
            goods_name = goods[goods_num - 1]['name']
            my_goods.append(goods[goods_num - 1])
            cost += goods[goods_num - 1]['price']
            print('\033[41m%s 已加入购物车,话费 %d \033[0m' % (goods_name, goods_price))
        elif goods_num == 'q':
            print('\033[41m 购物车商品总计 %d \033[0m' % cost)
            print('信用卡结账-----')
            card_data = credit_port.credit_b(account)
            balances = card_data['balance']
            if cost > balances:
                print('\033[41m您的余额不足！\033[0m')
            else:
                credit_port.credit_s(card_data, cost)

                # 打印购买列表
                goods_h_list = ''
                my_g_title = display.my_g_title
                for i, product in enumerate(my_goods, 1):
                    goods_h_item = "%-s %10s %10d" % (i, product['name'], product['price'])
                    goods_h_list = '\n'.join([goods_h_list, goods_h_item])
                goods_h_list = my_g_title % goods_h_list
                print(goods_h_list)
                user_item['log'][buy_time] = goods_h_list
                print('\033[41m您的兜里还剩: %d \033[0m \n返回商城' % balances)
                break


def users_load():
    if os.path.exists('user.json'):
        users_info = open('user.json', 'r', encoding='utf-8')
        users_info.close()
    else:
        key = input('找不到用户文件，是否初始化y/n：')
        if key == 'y':
            users_info = open('user.json', 'w', encoding='utf-8')
            users_module = {'name': 'name', 'pwd': 'password', 'bla': 0, 'log': {'0001-01-01': 'goods_h_list'}}
            users_info.write(json.dumps(users_module))
            users_info.close()
            print('已创建用户文件')


def load_goods():
    with open(goods_file, 'r') as f:
        goods = json.loads(f.read())
    goods_list = ''
    goods_title = display.goods_title
    for i, product in enumerate(goods, 1):
        goods_item = "%-s %10s %10d" % (i, product['name'], product['price'])
        goods_list = '\n'.join([goods_list, goods_item])
    goods_list = goods_title % goods_list
    return goods, goods_list


def shop_menu(user_item):
    menu_dic = {
        '1': shopping,
        '2': log_list,
        '3': logout,
    }
    user_name = user_item['name']
    buy_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print('当前日期：{date}'.format(date=buy_time))
    print('欢迎{user}的进入购物商店'.format(user=user_name))
    logon_authentication = False
    while not logon_authentication:
        print(display.p_list)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](user_item)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def main_menu():
    menu_dic = {
        '1': register,
        '2': logon,
        '3': logout,
    }
    logon_authentication = False
    while not logon_authentication:
        print(display.g_list)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("\033[31;1mOption does not exist!\033[0m")
