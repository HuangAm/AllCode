import os,sys,json
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path=os.path.join(BASE_DIR,"db","db.json")
oplog_path=os.path.join(BASE_DIR,"log","opelog")
paylog_path= os.path.join(BASE_DIR,"log","paylog")

# def db(name):
#     with open(db_path) as f:
#         for i in f:
#             print(i)
#             if name in i:
#                 return json.loads(i)[name]
#             else:
#                 print("用户名或密码错误！")
#                 exit()
# current_login = {"name": None, "login": False}
# def auth(func):
#     def wrapper(*args, **kwargs):
#         if current_login['name'] and current_login['login']:
#             res = func(*args, **kwargs)
#             return res
#         else:
#             name = input('用户名:')
#             password = int(input('密码:'))  ##intintint
#             d = db(name)
#             if password == d["pwd"]:
#                 # print('auth successful')
#                 current_login['name'] = name
#                 current_login['login'] = True
#                 res = func(*args, **kwargs)
#                 return res
#             else:
#                 print('auth error')
#
#     return wrapper
#
# import logging
# def logger(p,w):  #每次用都写这么多太麻烦，直接定义一个函数，要改需求在函数里面改就好了
#     logger = logging.getLogger() #实例化产生一个对象
#     fm=logging.Formatter("%(asctime)s %(message)s") #创建一个格式对象
#     fh=logging.FileHandler(p) #创建一个文件流handler(处理程序)，用于写入日志
#     sh=logging.StreamHandler() #创建一个屏幕流，用于输出到控制台
#
#     fh.setFormatter(fm) #文件流吸入格式对象，对象之间的交互
#     sh.setFormatter(fm) #屏幕流吸入格式对象，对象之间的交互
#
#     logger.addHandler(fh) #添加文件流，默认就是追加写
#     logger.addHandler(sh) #添加屏幕流
#
#     logger.setLevel(logging.DEBUG) #设计等级只能对logger对象进行设置，fh和sh设计了不管用
#     logger.warning(w)
# @auth
# def position():
#     "查看额度，操作日志"
#     dic=db(current_login["name"])
#     a=dic["position"]
#     b=dic["IDcard"]
#     print("您卡号为%s的信用卡所剩额度为：%s"%(b,a))
#     logger(oplog_path, "用户%s 查看信用卡余额"%current_login["name"])
# @auth
# def shopping():
#     "购物，信用卡接口，流水日志"
#     with open(db_path) as f:
#         d = json.loads(f.read())
#         a=current_login["name"]
#         print(d)
#         d[a]["position"]=10
#         print(d)
# position()
# shopping()
# d1={}
# with open(db_path,"w") as f:
#     a=f.read()
#     print(a)
#     f = "egon"
#     d[f]["position"] = 50
#     print(d)
# d1=json.dumps(d)
# with open(db_path,"w") as f:
#     f.write(d1)