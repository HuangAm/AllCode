# class Foo:
#     @staticmethod
#     def spam(x,y,z):#类中的一个函数，千万不要懵逼，self和x没有什么区别，都是形参
#         print(x,y,z)
#     # spam = staticmethod(spam) #把spam函数做成静态方法
# print(type(Foo.spam))#<class 'function'>类型的本质就是函数
# Foo.spam(1,2,3)#调用函数应该有几个参数就传几个参数
# f1 = Foo()
# f1.spam(3,3,3)#实例也可以使用，但通常静态方法都是给类用的，实例在使用时丧失了自动传值的机制
# print(f1.spam)
# import time
# class Data:
#     def __init__(self,year,month,day63):
#         self.year = year
#         self.month = month
#         self.day63 = day63
#     @staticmethod
#     def now(): #用Date.now()的形式去产生实例，该实例用的是当前时间
#         t=time.localtime() #获取结构化的时间格式
#         return Data(t.tm_year,t.tm_mon,t.tm_mday)#新建实例并且返回
#     @staticmethod
#     def tomorrow(): #
#         t=time.localtime(time.time()+86400)
#         return Data(t.tm_year,t.tm_mon,t.tm_mday)
# a=Data(1987,11,27)
# b=Data.now()
# c=Data.tomorrow()
# print(b.year,b.month,b.day63)
# print(a.year,a.month,a.day63)
# print(c.year,c.month,c.day63)


# class A:
#     x = 1
#     @classmethod
#     def test(cls):
#         print(cls,cls.x)
# class B(A):
#     x=2
# B.test()

# import time
# class Date:
#     def __init__(self,year,month,day63):
#         self.year=year
#         self.month=month
#         self.day63=day63
#     @staticmethod
#     def now():
#         t=time.localtime()
#         return Date(t.tm_year,t.tm_mon,t.tm_mday)
# class EuroDate(Date):
#     def __str__(self):
#         return "year:%s month:%s day63:%s"%(self.year,self.month,self.day63)
# e=EuroDate.now()
# print(e) #我们的意图是想触发EuroDate.__str__,但是结果为Date object

import time
class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @classmethod
    def now(cls):
        t=time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)
class EuroDate(Date):
    def __str__(self):
        return "year:%s month:%s day63:%s"%(self.year,self.month,self.day)
e=EuroDate.now()
print(e)







