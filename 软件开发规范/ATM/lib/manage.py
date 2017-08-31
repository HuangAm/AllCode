import os
import json
Basedir = os.path.dirname(os.path.dirname(__file__))
db_file_path = os.path.normpath(os.path.join(Basedir,r'db',r'db.json'))

def adduser():
    add_dic = input('输入添加的用户信息：').strip()
    alter_file = os.path.normpath(os.path.join(Basedir, 'db','accountinfomation2.json'))
    f_write = open(alter_file, 'w',encoding = 'utf8')
    f_read = open(db_file_path,'r',encoding = 'utf8')
    for line in f_read:
        dic = json.loads(line)
        f_write.write(json.dumps(dic)+"\n")
    f_write.write(add_dic+"\n")
    f_read.close()
    f_write.close()
    os.remove(db_file_path)
    os.rename(alter_file,db_file_path)
def change_limit():
    user = input('修改哪个账户的额度：').strip()
    change_money_now = input('修改额度为：').strip()
    alter_file = os.path.join(Basedir, 'db','accountinfomation2.json')
    f_write = open(alter_file, 'w',encoding = 'utf8')
    f_read = open(db_file_path,'r',encoding = 'utf8')
    for line in f_read:
        dic = json.loads(line)
        if user == dic["username"]:
            dic['money_now'] = change_money_now
            f_write.write(json.dumps(dic)+"\n")
        else:
            f_write.write(json.dumps(dic)+"\n")
    f_read.close()
    f_write.close()
    os.remove(db_file_path)
    os.rename(alter_file,db_file_path)
def frozen():
    user = input('输入想要冻结的用户名称：').strip()
    alter_file = os.path.join(Basedir, 'db','accountinfomation2.json')
    f_write = open(alter_file, 'w',encoding = 'utf8')
    f_read = open(db_file_path,'r',encoding = 'utf8')
    for line in f_read:
        dic = json.loads(line)
        if user == dic['username']:
            dic['level'] = 2
            f_write.write(json.dumps(dic)+"\n")
        else:
            f_write.write(json.dumps(dic)+"\n")
    f_read.close()
    f_write.close()
    os.remove(db_file_path)
    os.rename(alter_file,db_file_path)

