# python login.py -u alex -p 123456
# with open('user.db','w') as write_file:
#     write_file.write(str({
#         "alex":{"password":"123456",'status':False,'timeout':0},
#         }))
import sys,time
print(sys.argv) #[ ,-u,alex,-p,123456]
# username=sys.argv[2]
# password=sys.argv[4]
# class User:
#     db_path="user.db"
#     def __init__(self,name):
#         self.name=name
#     @property #优先级高于对象正常调用自己的属性，对象找属性先找他
#     def db(self):
#         with open(self.db_path,encoding="utf8") as read_file:
#             info=read_file.read()
#             return eval(info) #返回的就是文件的字典内容
#     @db.setter #优先级高于对象正常调用自己的属性，对象做修改先找他
#     def db(self,value): #修改 self.db=
#         with open(self.db_path,"w",) as write_file: #w覆盖写
#             write_file.write(str(value))
#             write_file.flush() #会立刻将文件内容从内从写入磁盘
#
#     def login(self):
#         data=self.db #data=eval(info)
#         if data[self.name]["status"]:
#             print("已经登录")
#             return True
#         if data[self.name]["timeout"] < time.time():#首先判断上次登出时间是不是小于现在的时间
#             count=0
#             while count<3:
#                 passwd=input("password>>:")
#                 if not passwd:continue
#                 if passwd == data[self.name]["password"]: #密码正确时,重置数据
#                     data[self.name]["status"]=True
#                     data[self.name]["timeout"]=0
#                     self.db=data #将data作为实参传给形参value，通过w覆盖源文件内容
#                     break #密码正确跳出while循环
#                 count+=1 #入错密码错误，计数一次当count的值为3是跳出循环
#             else:#输入三次密码不正确后，while循环正常跳出走else
#                 data[self.name]["timeout"]=time.time()+10 #将登出时间推迟10秒，字典是可变的,只改了登录时间，其他数据没有改
#                 self.db=data #这里又是在修改方法属性，还是把data的值传给value，字典是可变的，达到修改的目的
#         else:
#             print("账号已经锁定10秒")
# u=User(username)
# u.login()




#
#     @property
#     def locktime(self):
#         data = self.db
#         if data[self.name]["timeout"] > time.time():
#             l_time=data[self.name]["timeout"] - time.time()
#             print("账号锁定时间还剩%s秒"%l_time)
#         else:
#             print("已经登录")
#     @property
#     def out(self):
#         data = self.db
#         if data[self.name]["status"]:
#             data[self.name]["status"] = False
#             self.db=data
#             print("成功退出")
#         else:
#             print("没有登录不能退出")
