#coding:utf-8
#super在Python2中的用法：
    #1.super(自己的类，self).父类的函数名
    #2.super只能用于新式类
# class People(object):
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def walk(self):
#         print("%s is walking"%self.name)
# class Chinese(People):
#     country = "China"
#     def __init__(self,name,sex,age,language="Chinese"):
#         # self.name=name
#         # self.sex=sex
#         # self.age=age
#         super(Chinese,self).__init__(name,sex,age)#不需要传self
#         self.language=language
#     def walk(self):
#         # print("%s is walking"%self.name)
#         super(Chinese,self).walk()
# c=Chinese("egon","male","18")
# c.walk()

# class People:
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age=age
#     def walk(self):
#         print("%s is walking"%self.name)
# class Chinese(People):
#     country="China"
#     def __init__(self,name,sex,age,language="Chinese"):
#         super().__init__(name,sex,age)
#         self.language=language
#     def walk(self):
#         super().walk()
# c=Chinese("alex","female","19")
# c.walk()

#super的用法
    #1.super只能用于新式类，在Python2 中super(自己的类,self)
# class People:
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age=age
#     def walk(self):
#         print("%s is walking"%self.name)
# class Chinese(People):
#     country="China"
#     def __init__(self,name,sex,age,language="China"):
#         super(Chinese,self).__init__(name,sex,age)
#         self.language=language
#     def walk(self):
#         super(Chinese,self).walk()
# c=Chinese("alex","male","19")
# c.walk()
