#作业一
# import time
# def timmer(func):
#     def wrapper():
#         start_time=time.time()
#         func()
#         stop_time=time.time()
#         print("run time is %s"%(stop_time-start_time))
#     return wrapper
# @timmer
# def index():
#     time.sleep(2)
#     print("Hello world!")
# index()
#作业二
with open("user_file","r+",encoding="utf8") as f:
    f.write('{"agon":"123","alex":"3714","sb":"456"}')
# with open("auth_file","w",encoding="utf8") as f2:
#     f2.write('{"name":None,"login":False}')
def auth2(auth_type):
    def auth(func):
        def wrapper():
            l = []
            while True:
                name=input("input username:")
                if name == "q":
                    exit()
                with open("black_file",encoding="utf8") as f_read,open("user_file",encoding="utf8") as f1_read:
                    black = f_read.read()
                    user = f1_read.read()
                    if name not in black and name in user:
                        password=input("input password:")
                        if auth_type=="file":
                            with open("user_file",encoding="utf8") as f:
                                x = eval(f.read())
                                if name in x and password == x[name]:
                                    print("auth successful")
                                    res=func()
                                    return res
                                else:
                                    print("auth error")
                                    l.append(name)
                                    count=l.count(name)
                                    if count==3:
                                        print("Locked!")
                                        with open("black_file","r+",encoding="utf8") as f_write:
                                            f_write.write(name)
                        elif auth_type=="ldap":
                            print("还没有学啊，老师快教教")
                    if name not in black and name not in user:
                        print("Not Found!")
                        continue
                    else:
                        print("Locked!")
                        continue
        return wrapper
    return auth
@auth2("file")
def home():
    print('Welcome home page!')
home()



