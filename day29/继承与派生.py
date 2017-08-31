# class ParentClass1:#定义父类
#     pass
# class ParentClass2:#定义父类
#     pass
# class SubClass1(ParentClass1):#单继承，基类是ParentClass1,派生类是SubClass
#     pass
# class SubClass2(ParentClass1,ParentClass2):#python支持多继承，用逗号分隔开多个继承的类
#     pass
#
# print(ParentClass1.__bases__)
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def walk(self):
#         print('%s is walking'%self.name)
#     def say(self):
#         print('%s is saying'%self.name)
# class People(Animal):
#     pass
# class Pig(Animal):
#     pass
# class Dog(Animal):
#     pass
# p1 = People('obama',50)
# print(p1.name)
# print(p1.age)
# p1.walk()

# class Hero:
#     def __init__(self,nickname,aggressivity,life_value):
#         self.nickname=nickname
#         self.aggressivity=aggressivity
#         self.life_value=life_value
#     def attack(self,enemy):
#         enemy.life_value -= self.aggressivity



# class Teacher:
#     def __init__(self,name,sex,course):
#         self.name=name
#         self.sex=sex
#         self.course=course
# class Student:
#     def __init__(self,name,sex,course):
#         self.name=name
#         self.sex=sex
#         self.course=course
# class Course:
#     def __init__(self,name,price,period):
#         self.name=name
#         self.price=price
#         self.period=period
# python_obj=Course('python',15800,'7m')
# t1=Teacher('egon','male',python_obj)
# s1=Student('cobila','male',python_obj)
#
# print(s1.course.name)
# print(t1.course.name)


# class Teacher:
#     def __init__(self,birth):
#         self.birth=birth
# class Student:
#     def __init__(self,birth):
#         self.birth=birth
# class Birth:
#     def __init__(self,year,mouth,day63):
#         self.year=year
#         self.mouth=mouth
#         self.day63=day63
# t1=Teacher()
# class Interface:
#     def read(self):
#         pass
#     def write(self):
#         pass
# class Txt(Interface):
#     def read(self):
#         print ("dududu")
#     def write(self):
#         print ("xiexiexie")
# class Sata(Interface):
#     def read(self):
#         print ("yinpandudud")
#     def write(self):
#         print ("yingpanxiexie")
# class Process(Interface):
#     def read(self):
#         print ("jinchengdudu")
#     def write(self):
#         print ("jincengxiexi")
# def add(s,x):
#     return s+x
# def generator():
#     for i in range(4):
#         yield i
# base = generator()
# for n in [1,11]:
#     base = (add(i,n) for i in base)
# print(list(base))

# def add(s, x):
#     return s + x
# def generator():
#     for i in range(4):
#         yield i
# base = generator()
# n = 1
# base1 = (add(i, n) for i in base)
# n=11
# base2 = (add(i, n) for i in base1)
# print(list(base2))
#原谅我还是不会













