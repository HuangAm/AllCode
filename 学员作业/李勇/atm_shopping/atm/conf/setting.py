# _author_ : yong
# date : 2018/2/3
# _*_coding:utf-8_*_
import os, sys, logging
from datetime import datetime

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)
# 数据库信息
DATABASE = dict(engineer="file", dbpath=os.path.join(BASE_DIR, "database"))
# 用户数据存放目录
DB_PATH = os.path.join(BASE_DIR, 'user_db')
# 日志文件
LOG_LEVEL = logging.INFO
LOG_PATH_T = os.path.join(BASE_DIR, "logs", "transactions.log")
LOG_PATH_A = os.path.join(BASE_DIR, "logs", "access.log")
LOG_TYPES = {
    'transaction': LOG_PATH_T,
    'access': LOG_PATH_A,
}
# 账单报表文件路径
REPORT_PATH = os.path.join(BASE_DIR, "transaction")
# 用户登录失败最大次数
ERROR_MAX_COUNT = 3
# 转账、提现手续费
FETCH_MONEY_RATE = 0.05
# 冻结时间
FROZEN_ACCOUNT = 7

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},

}
# 日期
DATE = datetime.now().strftime('%Y-%m-%d')
WEEK = datetime.now().strftime('%A')
TIMESTAMP = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
