#被property装饰的属性会优先于对象的属性被使用(包括数据属性和函数属性)
#而被property装饰的属性,如下面的sex，分成三种：
    #1.property  查看
    #2.sex.setter 修改
    #3.sex.deleter 删除
#@property的第一个用法，把函数属性伪装成数据属性
# import math
# class Circle:
#     def __init__(self,radius): #圆的半径
#         self.radius = radius
#     @property #在这里的area面积应该是个名词，我们要让使用者感觉到它是一个数据属性，而不是函数属性，才符合常理
#     def area(self):
#         return math.pi * self.radius**2 #计算面积
#     @property
#     def perimeter(self):
#         return 2 * math.pi * self.radius #计算周长
# c = Circle(7)
# c.radius = 10
# print(c.area)#在没有property的时候我们打印的时候是内存地址，但是加上property装饰器后，就省去了加()去运行
# print(c.perimeter)

#@property的第二个用法,装饰的是对象的数据属性,和setter,deleter连用
# class People:
#     def __init__(self,name,SEX):
#         self.name = name
#         self.sex = SEX
#     @property#查找，增加了一种查找方式
#     def sex(self):
#         print("====>")
#         return self.__sex #真正的sex存在地方
#     @sex.setter#修改，增加了一种修改方式
#     def sex(self,value):
#         if not isinstance(value,str): #还可以限定修改的类型
#             raise TypeError("性别必须是字符串类型")
#         self.__sex = value#真正存放SEX的地方是在__sex中，
#     @sex.deleter#删除，增加一种删除方式
#     def sex(self):
#         del self.__sex
# p1 = People("egon","male")#在实例化生成对象的时候property,setter,deleter,都会起到作用，因为实例化的过程也会做数据封装，别忘了property的作用
# print(p1.name,p1.sex)
# del p1.sex
# print(p1.sex)
# p1.sex="femal"
#p1.sex  找sex的时候先去找有没有property修饰的sex如果有的话先找他
#p1.sex = ""  第一步也是先找，然后返回self.__sex他的值就是value，而value会自己传进去
#del p1.sex 删的是self.__sex







# class Foo:
#     def bar(self):
#         pass
#     @classmethod#把一个方法绑定给一个类：类.绑定到类的方法(),会把类本身当做第一个参数自动传给绑定到类的方法
#     def test(cls,x):
#         print(cls,x)#拿到一个类的内存地址后，就可以实例化或者引用类的属性了
# print(Foo.bar)#<function Foo.bar at 0x000000000116E1E0>
# print(Foo.test)#<bound method Foo.test of <class '__main__.Foo'>>
# Foo.test(123)
# f=Foo()
# print(f.bar)#<bound method Foo.bar of <__main__.Foo object at 0x0000000001181668>>
# print(f.test)#<bound method Foo.test of <class '__main__.Foo'>>

#类的设计者
# class Room:
#     def __init__(self,name,owner,width,length,high):
#         self.name = name
#         self.owner = owner
#         self.__width = width
#         self.__length = length
#         self.__high = high
#     def tell_area(self):#对外提供的接口，隐藏了内部的实现细节，此时我们想求的是面积
#         return self.__width * self.__length
#
# #使用者
# r1 = Room("卧室","egon",20,20,20)
# print(r1.tell_area())#使用者调用接口tell_area #400

# #类的设计者，扩展功能，而类的使用者完全不需要改变自己的代码
# class Room:
#     def __init__(self,name,owner,width,length,high):
#         self.name = name
#         self.owner = owner
#         self.__width = width
#         self.__length = length
#         self.__high = high
#     def tell_area(self):#对外提供的接口，隐藏内部实现，此时我们想求得是体积，内部逻辑变了，我们只需要修改下边这行代码就可以了，而外部调用感知不到，仍然使用该方法，但是功能已经变了
#         return self.__high * self.__width * self.__length
# with open("user_file","w")as f_write:
#     f_write.write(str({
#        "egon":{"password":"123","status":False,"timeout":0},
#        "alex":{"password":"456","status":False,"timeout":0}
#     }))
# with open("user_file",encoding="utf8")as f_read:
#     d = eval(f_read.read())
#     # print(d)
#     print(d["egon"]["password"])
#     print(d["alex"]["status"])
#     print(d["alex"]["timeout"])
# class User:
#     db_path = "user.db"
#     def __init__(self,username):
#         self.username = username
#     @property
#     def db(self):
#         with open("user_file",encoding="utf8")as f_read:
#             d = eval(f_read.read())
#             return d
# u = User("egon")
# print(u.db["egon"]["password"])
# print(u.db["egon"]["status"])
# with open("user.db","w",encoding="utf8")as write_file:
#     write_file.write(str({
#         "egon":{"password":"123","status":False,"timeout":0},
#         "alex":{"password":"456","status":False,"timeout":0},
#     }))
# with open("user.db",encoding="utf8") as read_file:
#     d=eval(read_file.read())
#     print(d)
#     print(d["egon"]["password"])
#     print(d["egon"]["status"])
#     print(d["egon"]["timeout"])
# class User:
#     db_path = "user.db"
#     def __init__(self,username):
#         self.username = username
#     @property
#     def db(self):
#         with open("user.db",encoding="utf8") as f_read:
#             d=f_read.read()
#         return d
# u = User("egon")
# print(u.db)

# import time
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

# u1=User("egon")
# u1.login()
#
# u2=User("alex")
# u2.login()

# def func(n):
#     if n == 1:
#         return
#     print(n)
#     n -= 1
#     func(n)
#     print(n)
#
# func(5)

# class Foo:
#     def __init__(self,val):
#         self.__name=val
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("%s must be str" %value)
#         self.__name=value #通过类型检查后，将值value存放到真实的位置self.__name
#     @name.deleter
#     def name(self):
#         del self.__name

# class Foo:
#     def __init__(self,val):
#         self.__name = val#隐藏数据属性，但是外部并不知道
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("%s must be str" %value)
#         self.__name=value
#     @name.deleter
#     def name(self):
#         del self.__name
'''
外部还是正常调用属性，但是并不知道内部已经隐藏，通过property提供的接口访问
真正的val所在的_A__name然后就找到了，修改和删除也一样
'''
# def index_words(text):
#     result=[]
#     if text:
#         result.append(0)
#     for index,letter in enumerate(text,1):
#         if letter == " ":
#             result.append(index)
#     return result
# print(index_words("hello alex da sb"))

# def index_words(text):
#     if text:
#         yield 0
#     for index,letter in enumerate(text,1):
#         if letter == " ":
#             yield index
# g=index_words("hello alex da sb")
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def test():
#     for i in range(4):
#         yield i
# g=test()
# g1=(i for i in g)
# g2=(i for i in g1)
# print(list(g1))#0,1,2,3
# print(list(g2))#[]

# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g=test()
# for n in [1,10]: #n=10,且执行两次
#     #g=(add(n, i) for i in g) #本来是n=1，但是现在是n=10
#     g=(add(n,i) for i in g) #n=10
# print(list(g))

# import os
# def init(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
# @init
# def searcher(target):
#     while True:
#         file_path=yield
#         for i in os.walk(file_path):
#             for j in i[-1]:
#                 file_path="%s\\%s"%(i[0],j)
#                 target.send(file_path)
# @init
# def opener(target):
#     while True:
#         file_path=yield
#         with open(file_path,encoding="utf8") as f:
#             for line in f:
#                 target.send((file_path,line))
#
# @init
# def grep(word,target):
#     while True:
#         file_path,line=yield
#         if word in line:
#             target.send(file_path)
#
# @init
# def printer():
#     while True:
#         file_path=yield
#         print(file_path)
#
# g=searcher(opener(grep("python",printer())))
# g.send("D:\\agon")


# print(abs(-1))
# print(abs(0))
# print(all([])),
# print(any({})),
# print(bin(3))
# def func():
#     pass
# print(callable(func))
# print(chr(67))
# print(ord("C"))
# print(ord("c"))
# x=complex(1-2j)
# x=1-2j
# print(x.real)
# print(x.imag)

# x=list(i for i in range(10))
# print(x)
# d=dict(x=1,y=2,z=3)
# print(d)
# s1={"he",1,2,3,"go","to"}
# s2={"to","la","shi",2,3,4}
# print(s2-s1)
# print(s1-s2)
# print(s1&s2)
# print(s1^s2)
# print(s1|s2)
# print(s1.difference(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(dir(s1))
# for i,j in enumerate("hello",10):
#     print(i,j)
# print(max(1,2,3,4,10,3))
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# print(max(salaries))#比的是字典，结果也是字典
# print(max(salaries,key=lambda k:salaries[k]))
# print(max(salaries.values()))
# l1=[1,2,3]
# s="hel"
# res=zip(l1,s)
# for i in res:
#     print(i)
# res = zip(salaries.values(),salaries.keys())
# print(max(res))
# print(sorted(salaries,key=lambda k:salaries[k],reverse=True))

# l=[1,2,3,7,5]
# n=map(lambda x:str(x)+"sb",l)
# for i in n:
#     print(i)

# from functools import reduce
# print(reduce(lambda a,b:a+b,l))
# print(reduce(lambda a,b:a+b,(i for i in range(1,101))))

