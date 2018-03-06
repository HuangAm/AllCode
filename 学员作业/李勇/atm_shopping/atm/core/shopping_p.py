
from atm.conf import setting
from atm.core import db_handler
import time


def acc_auth(user_type,account, password):

    db_api = db_handler.db_handler()
    data = db_api(account,user_type)
    if data['password'] == password:
        exp_time_stamp = time.mktime(time.strptime(data['expire_date'], "%Y-%m-%d"))
        if time.time() > exp_time_stamp:
            print("\033[31;1mAccount [%s] has expired,please contact the back to get a new card!\033[0m" % account)
            exit()
        elif data['status'] == 1:
            print("\033[31;1mAccount [%s] has locked,please contact the back to get unlock !\033[0m" % account)
            exit()
        else:
            return data
    else:
        print("\033[31;1mAccount ID or password is incorrect!\033[0m")


def acc_login(user_data, log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    user_type = user_data['user_type']
    while user_data['is_authenticated'] is not True:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(user_type,account, password)
        if auth:  # not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            return auth
        retry_count += 1
        if retry_count > setting.ERROR_MAX_COUNT-1:
            log_obj.error("account [%s] too many login attempts" % account)
            exit()
