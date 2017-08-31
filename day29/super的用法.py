#coding:utf-8
#super在Python2中的用法：
    #1.super(自己的类,self).父类的函数名字
    #2.super只能用于新式类
# class People(object):
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def walk(self):
#         print("%s is walking"%self.name)
# class Chinese(People):
#     country = "China"
#     def __init__(self,name,sex,age,language="Chinese"):
#         # self.name = name
#         # self.sex = sex
#         # self.age = age
#         #People.__init__(self,name,sex,age)
#         super(Chinese,self).__init__(name,sex,age)#不需要传self
#         self.language = language
# c = Chinese("egon","male",18)
# print (c.name,c.age,c.language)
# print (Chinese.__mro__)

# #在Python3中
# class People:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#     def walk(self):
#         print("%s is walking"%self.name)
# class Chinese(People):
#     country = "China"
#     def __init__(self,name,sex,age,language="Chinese"):
#         super().__init__(name,sex,age)
#         self.language = language
#     def walk(self,x):
#         super().walk()#walk后面不需要加参数
#         print("子类的x",x)
# c = Chinese("egon","male",18)
# print(c.name,c.age,c.sex)
# c.walk(1)
# print(Chinese.__mro__)#(<class '__main__.Chinese'>, <class '__main__.People'>, <class 'object'>)
# print(Chinese.mro())#[<class '__main__.Chinese'>, <class '__main__.People'>, <class 'object'>]

# l = [1,2,3,4,5]
# a=l.__iter__()

# a=iter(l)
# b=a.__next__()
# c=a.__next__()
# print(a)
# print(b)
# print(c)