# import abc
# class Animal(metaclass=abc.ABCMeta):#同一类事物：动物
#     @abc.abstractmethod
#     def talk(self):
#         pass
# class People(Animal):#动物形态之一：人
#     def talk(self):
#         print("say hello")
# class Dog(Animal): #动物形态之二：狗
#     def talk(self):
#         print("say wangwang")
# class Pig(Animal):#动物形态之三：猪
#     def talk(self):
#         print("say aoao")
# def func(animal): #参数animal就是多态性的体现
#     animal.talk()
# people = People()#产生一个人的对象
# pig=Pig()#产生一个住的对象
# dog=Dog()#产生一个狗的对象
# func(people)
# func(pig)
# func(dog)











# import abc
# class File(metaclass=abc.ABCMeta): #同一类事物：文件
#     @abc.abstractmethod
#     def click(self):
#         pass
# class Text(File): #文件的形态之一：文本文件
#     def click(self):
#         print("open file")
# class ExeFile(File): #文件的形态之二：可执行文件
#     def click(self):
#         print("execute file")













