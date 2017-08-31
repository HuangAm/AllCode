# import time
# def timmer(func):       #闭包函数
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('run time is %s'%(stop_time-start_time))
#     return wrapper
# @timmer #index = timmer(index)    装饰器语法
# def index():                    ##
#     time.sleep(3)               ##被装饰对象
#     print("welcome to oldboy")##
# index() #-------->wrapper()
#
# import time
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print('run time is %s'%(stop_time-start_time))
#     return wrapper
# @timmer
# def index():
#     time.sleep(3)
#     print("welcome to oldboy")
# index()





# import time
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print(stop_time-start_time)
#     return wrapper
# @timmer  #index=timmer(index)
# def index():
#     time.sleep(3)
#     print("welcome to oldboy")
# index()

# import  time
# def timmer(func):
#     def warpper():
#         star=time.time()
#         func()
#         stop=time.time()
#         print(stop-star)
#     return warpper
# @timmer
# def index():
#     time.sleep(3)
#     print("welcome")
# index()


# import time
# def timmer(func):
#     def wrapper(*args,**kwargs):
#         star_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print(stop_time-star_time)
#         return res
#     return wrapper
# @timmer
# def index():
#     time.sleep(3)
#     print("welcome")
# @timmer
# def auth(name,pwd):
#     print(name,pwd)
# index()
# auth("agon","123")
# @timmer
# def my_max(x,y):
#     n = x if x>y else y
#     return n
# res=my_max(1,2)
# print("==>",res)
# def auth2(auth_type):
#     def auth(func):
#         def wrapper(*args,**kwargs):
#             if auth_type == "file":
#                 name=input('username:')
#                 password=input('password:')
#                 if name == "zhejiangF4" and password == 'sb945':
#                     print("auth successful")
#                     res = func(*args,**kwargs)
#                     return res
#                 else:
#                     print("auth error")
#             elif auth_type == "sql":
#                 print("还他妈不会玩")
#         return wrapper
#     return auth
# @auth2(auth_type="sql")
# def index():
#     print('welcome to index page')
#
# def aaa(func):
#     def bbb(*args,**kwargs):
#         res = func(*args,**kwargs)
#         return res
#     return bbb


# import time
# from functools import wraps
# def timmer(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         '000'
#         start_time=time.time()
#         res=func(*args,**kwargs)
#         stop_time=time.time()
#         print('run time is %s'%(stop_time-start_time))
#         return res
#     return wrapper
# @timmer
# def index():
#     "dashabi"
#     print("from index")
# index()
# print(index.__doc__)







