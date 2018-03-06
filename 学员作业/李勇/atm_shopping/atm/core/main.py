'''
main program handle module , handle all the user interaction stuff
'''
from core import auth
from conf import display
from conf import setting
from core import log
from core import db_handler
from core import transaction
from core.auth import login_required

# transaction logger
trans_logger = log.logger('transaction')
# access logger
access_logger = log.logger('access')


def account_info(acc_data):
    acc_data = acc_data['account_data']
    account_info = display.card_info.format(
        id=acc_data['id'],
        enroll_date=acc_data['enroll_date'],
        expire_date=acc_data['expire_date'],
        credit=acc_data['credit'],
        balance=acc_data['balance'],
        pay_day=acc_data['pay_day'],
        status=acc_data['status']
    )
    print(account_info)


@login_required
def repay(acc_data):
    '''
    print current balance and let user repay the bill
    :return:
    '''
    account_data = acc_data['account_data']
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        repay_amount = input("\033[33;1mInput repay amount:\033[0m").strip()
        if len(repay_amount) > 0 and repay_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'repay', repay_amount)
            if new_balance:
                print('''New Balance:%s''' % (new_balance['balance']))
        elif repay_amount == 'b':
            back_flag = True

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % repay_amount)


@login_required
def withdraw(acc_data):
    '''
    print current balance and let user do the withdraw action
    :param acc_data:
    :return:
    '''
    account_data = acc_data['account_data']
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("\033[33;1mInput withdraw amount:\033[0m").strip()
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            new_balance = transaction.make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)
            if new_balance:
                print('''New Balance:%s''' % (new_balance['balance']))

        elif withdraw_amount == 'b':
            back_flag = True

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % withdraw_amount)


@login_required
def transfer(acc_data):
    account_data = acc_data['account_data']
    current_balance = ''' --------- BALANCE INFO --------
        Credit :    %s
        Balance:    %s''' % (account_data['credit'], account_data['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        transfer_amount = input("\033[33;1mInput transfer amount:\033[0m").strip()
        if len(transfer_amount) > 0 and transfer_amount.isdigit():
            transfer_card = input("\033[33;1mInput transfer card:\033[0m").strip()
            db_api = db_handler.db_handler()
            data = db_api(transfer_card, user_type='person')
            new_balance = transaction.make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
            transfe_balance = transaction.make_transaction(trans_logger, data, 'repay', transfer_amount)
            if new_balance:
                print('''New Balance:%s''' % (new_balance['balance']))
                print('''Transfe_balance:%s''' % (transfe_balance['balance']))

        elif transfer_amount == 'b':
            back_flag = True

        else:
            print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % transfer_amount)


@login_required
def pay_check(acc_data):
    log_transaction = db_handler.log_dump()
    print(log_transaction)


def logout(acc_data):
    access_logger.info('user exit')
    exit()


def add_account(acc_data):
    print('----begin add user-----')
    id = input('id:').strip()
    password = input('password:').strip()
    credit = input('credit:' ).strip()
    balance = input('balance:' ).strip()
    enroll_date = setting.DATE
    y=setting.DATE[:4]
    z=int(y) + 3
    expire_date = setting.DATE.replace(y,str(z))
    pay_day = input('pay_day:' ).strip()
    status = input('status:' ).strip()
    account_data = dict(
        id=int(id),
        password=password,
        credit=int(credit),
        balance=int(balance),
        enroll_date=enroll_date,
        expire_date=expire_date,
        pay_day=int(pay_day),
        status=int(status)
    )
    db_handler.account_add(account_data)

def a_credit(acc_data):
    account_id = input('please entry account :')
    account_data = db_handler.account_l_data(account_id,user_type='person')
    current_credit = account_data['credit']
    print('current credit is %d ' % current_credit)
    _credit = input('please entry modify credit :')
    account_data['credit'] = _credit
    db_handler.account_s_data(account_data)
def lock_account(acc_data):
    account_id = input('please entry account :')
    account_data = db_handler.account_l_data(account_id,user_type='person')
    current_status = account_data['status']
    if current_status == 0 :
        print('current account status normal')
    else:
        print('current account have locked!')
        _credit = input('please entry modify credit :')
    account_data['credit'] = _credit
    db_handler.account_s_data(account_data)

def interactive(acc_data):
    '''
    interact with user
    :return:
    '''
    if acc_data['user_type'] == 'person':
        menu_dic = {
            '1': account_info,
            '2': repay,
            '3': withdraw,
            '4': transfer,
            '5': pay_check,
            '6': logout
        }
        print(display.index_ATM)
    else:
        menu_dic = {
            '1': add_account,
            '2': a_credit,
            '3': lock_account,
            '4': logout
        }
        print(display.index_admin)
    exit_flag = False
    while not exit_flag:
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print("\033[31;1mOption does not exist!\033[0m")


def run(user_type):
    '''

    :return:
    '''
    user_data = {
        'account_id': None,
        'is_authenticated': False,
        'account_data': None,
        'user_type': user_type
    }
    acc_data = auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        access_logger.info('user logon')
        user_data['account_data'] = acc_data
        interactive(user_data)
