#！/usr/bin/env python3
#-*- coding:utf-8 -*-
import json,os
base_path = os.path.dirname(os.path.abspath(__file__))
def shop():
    '''
     购物商城，可反复购买，直到退出
    :return: 选择购买的商品信息
    '''
    exit_flag = False
    while not exit_flag:
        list_account = os.path.join(base_path, 'goods.json' )
        #print(list_account)
        f = open(list_account,'r',encoding='utf-8')
        data = json.load(f)
        print('Shopping List'.center(30,'-'))
        for i,index in enumerate(data):
            print(i,data[i])
        choice = input('请输入你想购买的商品前对应的序号>>:').strip()
        if not choice:continue
        elif choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < 5:
                #print(data[choice])
                return data[choice]
            else:
                print('\033[31;1m你要购买的商品暂时不存在\033[0m')
        elif choice == 'b':
            exit_flag = True
        elif choice == 'q':
            exit('bye')
        else:
            print('\033[31;1m你的输入不合法，请核对后再输入！')
#shop()
