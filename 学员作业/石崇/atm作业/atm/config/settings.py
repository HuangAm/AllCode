#！/usr/bin/env python3
#-*- coding:utf-8 -*-

import os,sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_PATH = '%s/db/account'%BASE_DIR
#print(DB_PATH)

TRANSACTION_TYPE ={
    'repay':{'action':'plus','interest':0},
    'withdraw':{'action':'minus','interest':0.05},
    'transfer':{'action':'minus','interest':0.05,'action2':'plus'},
    'consume':{'action':'minus','interest':0},
}
'''   
    交易类型分别为还款，取款，转账，消费
    action和interest分别表示金额的增加减少和利息
'''