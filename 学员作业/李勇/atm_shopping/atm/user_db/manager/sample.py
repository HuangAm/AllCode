import json
acc_dic = {
    'name': 'super',
    'password': 'abc',
    }


with open('super.json','w') as f :
    f.write(json.dumps(acc_dic))