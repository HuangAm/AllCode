#调用方式1
# import threading
# import time
# def tingge():
#     print("tingge")
#     time.sleep(3)
#     print("tinggejieshu")
# def xieboke():
#     print("xieboke")
#     time.sleep(5)
#     print("xieboke")
#     print(time.time()-s)
# s=time.time()
# t1=threading.Thread(target=tingge)
# t2=threading.Thread(target=xieboke)
# t1.start()
# t2.start()
# print("ending")

#调用方式二
# import threading
# import time
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#     def run(self):
#         print("running on number:%s" %self.num)
#         time.sleep(3)
# t1=MyThread(56)
# t2=MyThread(78)
# t1.start()
# t2.start()
# print("ending")

# import threading
# import time
# def countNum(n): #定义某个线程要运行的函数
#     print("running on number:%s" %n)
#     time.sleep(3)
# if __name__=="__main__":

# l=[1,2,3,4]
# l2=(1,2)
# def hh(*args,**kwargs):
#     print(args,kwargs)
# hh(*l,l2)

# class People:
#     # pass
#     def __init__(self,name,age,high):
#         self.name=name
#         self.age=age
#         self.high=high
#     def a(self,x):
#         print(self,"dale",x)
#     def __str__(self):
#         return "123"
# p=People("egon")
# p2=People("gon")
# p.name="egon"
# print(p.name)
# print(p)
# a=int("5")
# print(a)

# import threading  #线程模块
# import time
# def countNum(n): #定义某个线程要运行的函数
#     print("running on number:%s" %n)
#     time.sleep(3)
# if __name__ == '__main__':
#     t1=threading.Thread(target=countNum,args=(23,)) #生成一个线程实例
#     t2=threading.Thread(target=countNum,args=(34,)) #生成第二个线程实例
#     t1.start() #启动线程
#     t2.start() #启动线程
#     print("ending!") #在这个进程有三个线程，一个主线程两个子线程


#继承Thread式创建
# import time
# import threading
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#     def run(self):
#         print("runing on number:%s" %self.num)
#         time.sleep(3)
# t1=MyThread(56)
# t2=MyThread(78)
#
# t1.start()
# t2.start()
# print("ending")


# import time
# import threading
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num=num
#     def run(self):
#         print("running on number:%s" %self.num)
#         time.sleep(3)
# t1=MyThread(56)
# t2=MyThread(78)
#
# t1.start()
# t2.start()
# print("ending")
#join()


# import threading
# import time
# from time import ctime,sleep
# def Music(name):
#     print("Begin listening to {name} {time}".format(name=name,time=ctime()))
#     sleep(5)
#     print("end listening {time}".format(time=ctime()))
# def Blog(title):
#     print("Begin recording the {title} {time}".format(title=title,time=ctime()))
#     sleep(3)
#     print("end recording {time}".format(time=ctime()))
# threads=[]
# t1=threading.Thread(target=Music,args=("FILL ME",))
# t2=threading.Thread(target=Blog,args=("python",))
# threads.append(t1)
# threads.append(t2)
# if __name__ == '__main__':
#     t2.setDaemon(True)
#     for t in threads:
#         t.start()
#     t1.join()
#     t2.join()
#     print("all over %s" %ctime())


# import threading
# from time import ctime,sleep
# import time
# def Music():
#     print("Begin listening music {time}".format(time=ctime()))
#     sleep(3)
#     print("End listening {time}".format(time=ctime()))
#
# def Blog():
#     print("Begin Blog {time}".format(time=ctime()))
#     sleep(5)
#     print("End Blog {time}".format(time=ctime))
#
# threads=[]
# t1=threading.Thread(target=Music)
# t2=threading.Thread(target=Blog)
#
# threads.append(t1)
# threads.append(t2)
# if __name__ == '__main__':
#     t2.setDaemon(True)
#     # t1.setDaemon(True)
#     for t in threads:
#         t.start()
#     # t1.join()
#     # t2.join()
#     print("all over %s" %ctime())






























