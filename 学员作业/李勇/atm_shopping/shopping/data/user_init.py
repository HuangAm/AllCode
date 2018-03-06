import json
users_info = open('user.json', 'w', encoding='utf-8')
users_module = {'name': 'name', 'pwd': 'password', 'credit': '', 'log': {'0001-01-01': 'goods_h_list'}}
users_info.write(json.dumps(users_module))
users_info.close()
print('已创建用户文件')