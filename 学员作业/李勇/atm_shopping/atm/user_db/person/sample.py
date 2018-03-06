import json
credit_dic = {
    'id': 2234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': '2016-01-02',
    'expire_date': '2021-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

with open('2234.json','w') as f :
    f.write(json.dumps(credit_dic))