import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)
from atm.core import auth
from atm.core import transaction
from atm.core import log


def credit_b(account):
    password = input('please the password:').strip()
    data = auth.acc_auth(user_type='person', account=account, password=password)
    return data


def credit_s(account_data, amount):
    trans_logger = log.logger('transaction')
    transaction.make_transaction(trans_logger, account_data, 'withdraw', amount)
