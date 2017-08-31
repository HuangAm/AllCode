# s = '**hello,world!**'
# s=s.strip("*")
# print(s) #hello,world!

# num=int(input("请输入任意数字："))
# if num >1:
#     for i in range(2,num): #[2,num-1]
#         if i%2 != 0:
#             print(i)
# elif num < 1:
#     for i in range(num+1,1):
#         if i%2!=0:
#             print(i)
# else:
#     print("不能输入1")

# s = 'hskakhlkshfkskjakf'
# s1={"h",}
# for i in s:
#     s1.add(i)
# s=""
# for i in s1:
#     s="".join([s,i])
# print(s) #ahjflsk

# s = '123.33sdhf3424.34fdg323.324'
# import re
# s1=re.split("[a-z]+",s)
# summ=0
# for i in s1:
#     summ += float(i)
# print(summ) #3870.994

# d={'k1':'v1','k2':[1,2,3],('k','3'):{1,2,3}}
# l=list(d.values())
# print(l) #[{1, 2, 3}, 'v1', [1, 2, 3]]
#
# for key in d:
#     if isinstance(key,tuple):
#         print(d[key]) #{1, 2, 3}
#
# print(type(d[('k','3')])) #<class 'set'>



# def wrapper(func):
#     def inner(*arg, **kwargs):
#         func(*arg, **kwargs)
#     return inner
#
# @wrapper # a=wrapper(a)
# def a(arg):
#     print(arg)
#
# a()

# with open("7th_questions",encoding="utf8") as f:
#     for line in f:
#         if line.startswith("T"):
#             print(line,end="")


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# p1=Person("egon1","18")
# p2=Person("egon2","19")
# p3=Person("egon3","20")
# p4=Person("egon4","21")
# p5=Person("egon5","22")
# p6=Person("egon6","23")
# p7=Person("egon7","24")
# p8=Person("egon8","25")
# p9=Person("egon9","26")
# p10=Person("egon10","27")
# p11=Person("egon11","28")
# print(p11.name) #egon11


# class Police:
#     flag = "police"
#     def __init__(self,name,lifevalue,arm,sex):
#         self.name=name
#         self.lifevalue=lifevalue
#         self.arm=arm
#         self.sex=sex
#     def attack(self,enemy):
#         if isinstance(enemy,Terrorist):
#             enemy.lifevalue -= 100
#             print("一枪爆头")
#         else:
#             print("下不了手")
#
#
#
# class Terrorist:
#     flag = "terrorist"
#     def __init__(self,name,lifevalue,arm,sex):
#         self.name = name
#         self.lifevalue = lifevalue
#         self.arm = arm
#         self.sex = sex
#     def attack(self,enemy):
#         if isinstance(enemy,Police):
#             enemy.lifevalue -= 100
#             print("一枪爆头")
#         else:
#             print("下不了手")
#
# p1= Police("egon",100,"M4A1","male")
# t1= Terrorist("alex",100,"AK47","male")
# p1.attack(t1) #egon一枪爆头
# print(t1.lifevalue) #0

# class Role:
#     def __init__(self,name,lifevalue,arm,sex):
#         self.name = name
#         self.lifevalue = lifevalue
#         self.arm = arm
#         self.sex = sex
# class Police(Role):
#     flag = "police"
#     def attack(self,enemy):
#         if isinstance(enemy,Terrorist):
#             enemy.lifevalue -= 100
#             print("一枪爆头")
#         else:
#             print("下不了手")
# class Terrorist(Role):
#     flag = "terrorist"
#     def attack(self,enemy):
#         if isinstance(enemy,Police):
#             enemy.lifevalue -= 100
#             print("一枪爆头")
#         else:
#             print("下不了手")
# p1= Police("egon",100,"M4A1","male")
# t1= Terrorist("alex",100,"AK47","male")
# p1.attack(t1) #egon一枪爆头
# print(t1.lifevalue) #0

# class Base:
#     def f1(self):
#         self.f2()
#
#     def f2(self):
#         print('...')
#
# class Foo(Base):
#     def f2(self):
#         print('9999')
#
# obj = Foo()
# obj.f1()


# import socket
# import selectors
# sock=socket.socket()
# sock.bind(("127.0.0.1",8080))
# sock.listen(5)
# sel=selectors.DefaultSelector()
#
# def read(fd,mask):
#     try:
#         data=fd.recv(1024)
#         print(data.decode("utf8"))
#         msg=input(">>:")
#         fd.send(msg.encode("utf8"))
#     except Exception as e:
#         sel.unregister(fd)
#     return
# def accept(fd,mask):
#     conn,addr=fd.accept()
#     sel.register(conn,selectors.EVENT_READ,read)
#
# sel.register(sock,selectors.EVENT_READ,accept)
# while True:
#     events=sel.select()
#     for key,mask in events:
#         func=key.data
#         fd=key.fileobj
#         func(fd,mask)

# import queue
# p=queue.Queue()
# def producer():
#     count=0
#     while count<5:
#         p.put(count)
#         count+=1
#
# def consumer():
#     p.get()







