#只要是由对象出发的就有自动传值的功能，实例化和调用绑定方法都是有对象引发的，所以都有自动传值的功能
#方法跟类没有关系，跟类扯关系的是函数
# class Garen:
#     camp = 'Demacia'  #类的特征
#     def attack(self):  #共同的技能
#         print('attack')
# print(Garen)#<class '__main__.Garen'>Garen是一个类
# print(int)#<class 'int'>int是一个类

#如何使用类
#一：实例化
# x=int(10)
# print(x)
# print(type(x)
# y=int()
# print(int())weiweiwieiweshenmee

# obj=Garen() #实例化
# print(obj)#<__main__.Garen object at 0x00000000011E1438>

#二：引用类的特征(类的变量)和技能（类的函数）
# print(Garen.camp)
# Garen.attack(11)#类调用类的函数，就按函数走，有参就要传
# print(Garen.attack)#<function Garen.attack at 0x000000000115E1E0>说明现在这是个函数，不是方法


#如何使用实例
# class Garen:
#     camp = 'Demacia'  #类的特征
#     def __init__(self,nickname):  #像__init__这种__开头，__结尾的函数，都是Python内置的函数
#         self.nick=nickname    #记住形式，
#     def attack(self,enemy):  #共同的技能
#         print('attack %s'%enemy)
# g1=Garen("草丛伦")#类加括号就是实例化，实例化过程会自动触发类内部的__init__()函数
# g2=Garen("猥琐伦")#别名属于同一类对象的不同特性，语法Garen.__init__(g2,"猥琐伦")
# print(g1)
# print(g1.nick)#草丛伦  由self.nick=nickname得到输出什么
# print(g2.nick)#猥琐伦

# print(g1)#<__main__.Garen object at 0x0000000000A914E0>
# print(g2)#<__main__.Garen object at 0x0000000000A91518>与上面的不相等
# print(g1.attack)#绑定方法<bound method Garen.attack of <__main__.Garen object at 0x0000000000AC14E0>>
# print(Garen.attack)#函数<function Garen.attack at 0x0000000000ABE268>
#
# Garen.attack("g1")#调用的是函数，不传参会报错,有几个参数传几个
# g1.attack("alex")#应为除了self外还有一个参数enemy我们这里传的"alex"就是传给enemy的
#函数只要定义参数调用时就必须传值，没有传必然是Python帮我传了，在这里我们调用的是绑定方法把绑定对象作为参数self传入方法

#总结
#类：1、实例化，2、引用名字（类名.变量名，类名.函数名）
#实例：1、实例是类的实例化对象   2、引用名字（实例名.类的变量，实例名.绑定方法，实例名.实例自己的变量名）


# class Garen:
#     camp = 'Demacia'  #类的特征
#     def __init__(self,nickname):  #像__init__这种__开头，__结尾的函数，都是Python内置的函数
#         self.nick=nickname    #记住形式，
#     def attack(self,enemy):  #共同的技能
#         print('attack %s'%enemy)

#类的特征(变量)增删该查
# print(Garen.camp)#查，查看变量值
# Garen.camp='aaaa'#改，修改变量值
# print(Garen.camp)#

# del Garen.camp#删除，删除类的特征，这里可以说变量
# print(Garen.camp)

# Garen.x=1#增加，增加类的特征， 变量
# print(Garen.x)

#实例的特征(变量)增删改查，当然必须得先产生实例
# g1=Garen('alex')
# print(g1.nick)#查看属性,__init__函数定义的属性这里的属性是别名
# g1.nick='asb'#修改属性
# print(g1.nick)
# del g1.nick #删除属性
# g1.sex='female'#增加一个特性，变量名，但是加到哪里了呢？？？
# print(g1.sex)


# class Room:
#     def __init__(self,name,owner,width,length,heigh):
#         self.name = name
#         self.owner = owner
#         self.width = width
#         self.length = length
#         self.heigh = heigh
#
# r1=Room('厕所','alex',100,100,10000)
# print('%s住的%s总面积是%s'%(r1.owner,r1.name,r1.width*r1.length))

# class Room:
#     def __init__(self,name,owner,width,length,heigh):
#         self.name=name
#         self.owner=owner
#         self.width=width
#         self.length=length
#         self.heigh=heigh
#     def cal_area(self):
#         print('%s住的是%s总面积是%s' % (self.name, self.owner, r1.width * r1.length))
#
#
# r1=Room('厕所','alex',100,100,1000000)
# print('%s住的是%s总面积是%s' %(r1.name,r1.owner,r1.width*r1.length))


#在Python3中所有类都是新式类
# class A:pass
# print(A.__base__)#默认继承object，在Python2中不会默认继承，没有写的话就是经典类
#
# #在Python2中的新式类
# class B(object):pass
# class C(B):pass
#
# print(B.__base__)
# print(C.__base__)

# class Student:
#     country = 'China'
#     def __init__(self,ID,NAME,SEX,PROVINCE):
#         self.id=ID
#         self.name=NAME
#         self.sex=SEX
#         self.province=PROVINCE
#     def search_score(self):
#         print('tell score')
#     def study(self):
#         print('study',self)
# s1 = Student('3185525654654','cobila','female','shanxi')
# print(Student.__dict__)#查看类的名称空间，字典形式
# print(s1.__dict__)#查看实例的，字典形式
# print(s1.id)
# print(s1.x)#实例找属性的时候现在他自己的dict里面找，没有的话再去类的dict里面找，如果类里面也没有的话就报错
# s1.x=123# 实例的属性在哪里定义都一样，他属与实例域
# print(id(s1.country))#18528216
# print(id(Student.country))#18528216,说明类的变量是类和实例共用的
# print(s1.study,id(s1.study))#4814280，既然是绑定方法，就是把s1和study方法绑到一起看，因为s1是对无二的所以s1.study也是独一无二的
#所以绑定方法是唯一绑定到一个确定的对象上的
# print(Student.study,id(Student.study))#11985648


#类属性：特征（变量）和技能（函数）
#类的用法：实例化，属性引用
# s1 = Student('3185525654654','cobila','female','shanxi')
# s1=Student.__init__(s1,'3185525654654','cobila','female','shanxi')
# print(s1)
# s1=Student.__init__('3185525654654','cobila','female','shanxi')
# Student.x = 1
# print(Student.x)
# del Student.x
# print(Student.x)

# class Student:
#     country = 'China'
#     def __init__(self,ID,NAME,SEX,PROVINCE):
#         self.id=ID
#         self.name=NAME
#         self.sex=SEX
#         self.province=PROVINCE
#     def search_score(self):
#         print('tell score')
#     def study(self):
#         print('study',self)
# s1 = Student('3185525654654','cobila','female','shanxi')
# print(s1.__dict__)
# print(s1.id)

#OOD
# '''
#     找对象：student  共同的特征：country
#                   独有的特征：name sex age
#                   共有的函数：study
#
#     归类：class Student
#
#     找对象: school  共同的特征：education
#                     独有的特征：name address
#                     共有的函数：enrollment
#     归类：class School
#
#     找对象: teacher  共同的特征：teach
#                     独有的特征：name height
#                     共有的函数：classroom
#     归类：class Teacher
# '''

#OOP
# class Student:
#     country = "China"
#     def __init__(self,name,sex,age):
#         self.name=name
#         self.sex=sex
#         self.age=age
#     def study(self):
#         pass
#
# class School:
#     education = 'education'
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def enrollment(self):
#         pass
#
# class Teacher:
#     teach = "teach"
#     def __init__(self,name,height):
#         self.name = name
#         self.height = height
#     def classroom(self):
#         pass
# wuyongqing=Student("武勇强","male","23")
# laonanhai=School("老男孩教育",'沙河')
# egon=Teacher("egon",'180cm')


# class Riven:
#     camp = 'Noxus'
#     def __init__(self,nickname,aggressivity=54,life_value=414):
#         self.nickname = nickname
#         self.aggressivity = aggressivity#英雄的攻击力
#         self.life_value = life_value#英雄的生命值
#     def attack(self,enemy):#英雄的普通攻击技能
#         enemy.life_value-=self.aggressivity#敌人的生命值等总值减去英雄的攻击力
#
# class Garen:
#     camp = 'Demaxiya'
#     def __init__(self,nickname,aggressivity=54,life_value=414):
#         self.nickname = nickname
#         self.aggressivity = aggressivity#英雄的攻击力
#         self.life_value = life_value#英雄的生命值
#     def attack(self,enemy):#英雄的普通攻击技能
#         enemy.life_value-=self.aggressivity#敌人的生命值等总值减去英雄的攻击力

# r1=Riven('瑞问问')
# g1=Garen('草丛伦')
# g1.attack(r1)#对象之间的交互,就是一个对象把另一个对象作为参数运行方法
# print(r1.life_value)

class Student:
    def __init__(self,ID,name,sex):
        self.id=ID
        self.name=name
        self.sex=sex
        self.course_list=[]
    def search_score(self):
        pass
    def hanin(self):
        pass
class Course:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

s1=Student('12123123123','colabi','famle')
print(s1.id,s1.name,s1.sex)
print(s1.course_list)
# s1.course_list.append('python')
# print(s1.course_list)
python_obj=Course('python',15800,'7m')
linux_obj = Course('linux',19800,'2m')
s1.course_list.append(python_obj)
s1.course_list.append(linux_obj)
print('''
    student name is :%s
    student course is :%s
    course price is :%s
'''%(s1.name,s1.course_list[0].name,s1.course_list[0].price))













#严格遵守下面流程
# '''
# 面向对象程序设计OOD：
#     找对象------>找类（归纳对象共同的特征与技能，还有每个对象独有的特征）
# 面向对象编程OOP：
#     先定义类------>实例化出对象
# '''
#注意#1.应用场景，比如老男孩教育共同的特征就是商标都一样，太大了就写找不到共同特征了
     #2.找不到共同特征就不用写了
#OOD：定义学生类
    #共同特征：country = 'China'
    #技能：查看成绩
    #独有特征：ID,NAME,SEX,PROBINCE
#OOP:编写程序
# class Student:
#     country = 'China'
#     def __init__(self,ID,NAME,SEX,PROVINCE):
#         self.ID=ID
#         self.name=NAME
#         self.sex=SEX
#         self.province=PROVINCE
#     def search_score(self):
#         print('tell score')
#     def study(self):
#         print('study')


