#！/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
此模块用于处理账户的交易操作
'''
import os,json
from config  import settings
from db import account

def save_db(account_data):
    json_account = os.path.join(settings.DB_PATH,'%s.json'%account_data['id']) # 获取用户json文件
    if os.path.isfile(json_account):
        f = open(json_account,'w',encoding='utf-8')
        data = json.dump(account_data,f)
        f.close()
        return data
    else:
        return {'error':'account file does not exist'}


def transac_tion(user_initial,trans_type,amount,*tra_choice):
    amount = float(amount)                      # 转换成浮点数
    if trans_type in settings.TRANSACTION_TYPE: # 判断交易类型
        amt_intere = amount*settings.TRANSACTION_TYPE[trans_type]['interest']  # 计算利息
        last_balance = user_initial['data']['balance']      # 取出上次交易后的剩余金额
        if settings.TRANSACTION_TYPE[trans_type]['action'] == 'plus': # 还款
            new_balance = last_balance + amount + amt_intere    # 还款后金额
        elif settings.TRANSACTION_TYPE[trans_type]['action'] == 'minus' : # 仅取款
            new_balance = last_balance - amount - amt_intere    # 取款后金额
            if new_balance < 0:     # 金额不足
                print('\033[31;1m你的账户余额不足...\033[0m')
                return {'交易失败'}
            else:
                user_initial['data']['balance'] = new_balance  # 修改内存里的剩余金额
                save_db(user_initial['data'])  # 将修改保存到硬盘
                return {'msg': '交易成功', '你的余额：': new_balance}
        elif settings.TRANSACTION_TYPE[trans_type]['action2']=='plus':  # 是否进行转账
            new_balance = last_balance - amount - amt_intere    # 取款后金额
            if new_balance < 0:     # 金额不足
                print('\033[31;1m你的账户余额不足...\033[0m')
                return {'交易失败'}
            json_account2 = os.path.join(settings.DB_PATH, '%s.json'%tra_choice) # 获取转账用户
            if os.path.isfile(json_account2):      # 判断是否是文件
                f = open(json_account2, 'w', encoding='utf-8')      # 打开转账用户的文件
                data = json.load(json_account2)              # 读取
                last2_balance = data['balance']              # 获取余额
                new2_balance = last2_balance + amount       # 获得转账后的余额
                data['balance'] = new2_balance              # 修改余额
                json.dump(data,f)                           # 写入硬盘
                f.close()                                   # 关闭文件
        user_initial['data']['balance'] = new_balance      # 修改内存里的剩余金额
        save_db(user_initial['data'])      # 将修改保存到硬盘
        return {'msg':'交易成功','你的余额：':new_balance}
    else:
        print('\033[31;1m 暂不支持你申请的交易...\033[0m')
        return {'msg':'交易失败'}






