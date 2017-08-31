# import time#调用time模块
# def timer(func):#1#3#定义timmer函数，这一整个函数就是个闭包
#     def wrapper():#4#7#
#         start_time=time.time()#8#
#         func()#9#
#         stop_time=time.time()#13
#         print('run time is %s'%(stop_time-start_time))#14
#     return wrapper#5#直接返回wrapper
# @timer#2#10   @语法：index=timer(index)
# def index():
#     time.sleep(3)#11#
#     print('welcome to oldboy')#12
# index()#6#调用index就相当一调用wrapper，即wrapper()

# import time
# def timmer(func):
#     def wrapper (*args,**kwargs):
#         start_time=time.time()
#         func(*args,**kwargs)
#         stop_time=time.time()
#         print("run time is %s"%(stop_time-start_time))
#     return wrapper
# @timmer
# def home(name):
#     time.sleep(2)
#     print("welcome to %s home page"%name)
#
# @timmer
# def auth(name,password):
#     print(name,password)
#
# @timmer
# def tell():
#     print('=======')
# home('dragon')
# auth('egon','123')
# tell()


# import time
# current_login={'name':None,'login':False}
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print(stop_time-start_time)
#     return wrapper
# def auth2(auth_type):
#     def auth(func):
#         def wrapper(*args,**kwargs):
#             if current_login['name'] and current_login['login']:
#                 res = func(*args,**kwargs)
#             elif auth_type == 'file':
#                 name=input('username:')
#                 password=input('password:')
#                 if name=='zhejiangf4'and password == 'sbasb':
#                     print('auth successful')
#                     res=func(*args,**kwargs)
#                     current_login['name']=name
#                     current_login['login']=True
#                     return res
#                 else:
#                     print('auth error')
#             elif auth_type =="sql":
#                 print("还他妈不会玩")
#         return wrapper
#     return auth
# @timmer
# @auth2(auth_type="file")#
# def index():
#     print('Welcome to index page!')
# @auth2
# def home():
#     print("home good")
#
# index()
# home()


#先把大体的概念说一下：
# def aaa()：#装饰函数
# @aaa
# def func():#被装饰函数
#     pass
#
# func=aaa(func)

# @ccc
# @bbb
# @aaa
# def func():
#     pass
#
# func=ccc(bbb(aaa(func)))

#
# @ccc('c')
# @bbb('b')
# @aaa('a')
# def func():
#     pass
#
# func=ccc('c')(bbb('b')(aaa('a')(func)))

#上边的例子是下边这个规律
# founc=bbb(aaa('a')(func))
#index=timmer(auth2(auth_type="list")(func))
#index=timmer(auth(func))
#index=timmer(wrapper_dixia)
#index=wrapper_shangbian
#index()=wrapper_shangbian()
#index()=wrapper_dixia()


# m={"agon":"123","alex":"234","liuliu":"345"}
# n=input(">>:")
# print(n in m)

# l=[]
# while True:
#     m=input(">>:")
#     l.append(m)
#     print(l)
#     print(l.count(m))

import time
current_login={'name':None,'login':False}
def timmer(func):
    def wrapper():
        start_time=time.time()
        func()
        stop_time=time.time()
        print('run time is %s'%(stop_time-start_time))
    return wrapper
def auth2(auth_type='file'):
    def auth(func):
        def wrapper(*args,**kwargs):
            if current_login['name'] and current_login['login']:
                res=func(*args,**kwargs)
                return res
            if auth_type == 'file':
                name = input('username:')
                password = input('password:')
                if name == 'zhejiangF4' and password == 'sb945':
                    print('auth successful')
                    res = func(*args,**kwargs)
                    current_login['name']=name
                    current_login['login']=True
                    return res
                else:
                    print('auth error')
            elif auth_type == "sql":
                    print("haibuhui")
        return wrapper
    return auth
@timmer
@auth2(auth_type="file")
def index():
    print('welcome to index page')
@auth2("file")
def home():
    print("welcome to home page")

index()
home()

















