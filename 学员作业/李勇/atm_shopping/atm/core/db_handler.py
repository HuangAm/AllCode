# _author_ : yong
# date : 2018/2/3
# _*_coding:utf-8_*_

import json, os
from conf import setting



def account_l_data(account, user_type):
    """load account file"""
    account_file = os.path.join(setting.DB_PATH, user_type, '%s.json' % account)
    if os.path.isfile(account_file):
        with open(account_file, 'r') as f:
            data = json.loads(f.read())
        return data
    else:
        exit("\033[31;1mAccount [%s] does not exist!\033[0m" % account)


def account_s_data(account_data):
    """save account file"""
    account_file = os.path.join(setting.DB_PATH, 'person', '%s.json' % account_data['id'])
    with open(account_file, 'w') as f:
        f.write(json.dumps(account_data))

def account_add(acct_data) :
    acct_id = acct_data['id']
    account_file = os.path.join(setting.DB_PATH,'person', '%s.json' % acct_id)
    if os.path.isfile(account_file):
        exit("\033[31;1mAccount [%s] does exist!\033[0m" % acct_id)
    else:
        with open(account_file, 'w') as f:
            f.write(json.dumps(acct_data))
def log_dump():
    """dump log file"""
    if os.path.isfile(setting.LOG_PATH_T):
        with open(setting.LOG_PATH_T, 'r') as f:
            data = f.read()
        return data
    else:
        exit("\033[31;1mlogfile does not exist!\033[0m" )

def db_handler():
    '''
    connect to db
    :param conn_parms: the db connection params set in settings
    :return:a
    '''
    conn_params = setting.DATABASE
    if conn_params['engineer'] == 'file':
        return account_l_data
    elif conn_params['engineer'] == 'mysql':
        pass
