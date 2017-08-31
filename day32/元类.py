# class Foo:
#     x=1
#     def run(self):
#         pass
# print(type(Foo))
#
# #type称为元类，是所有类的类，利用type模拟class关键字的创建的过程
# def run(self):
#     print("%s is runing" %self.name)
# class_name="Bar"
# bases=(object,)
# class_dict={
#     "x":1,
#     "run":run
# }
# Bar=type(class_name,bases,class_dict)
# print(Bar)
# print(type(Bar))

# class Foo:
#     x=1
#     def run(self):
#         pass
# print(type(Foo))
#
# #type称为元类，是所有类的类，利用type模拟class关键字的创建类的过程
# def run(self):
#     print("%s is runing" %self.name)
# class_name="Bar"
# bases=(object,)
# class_dic={
#     "x":1,
#     "run":run
# }
# Bar=type(class_name,bases,class_dic)
# print(Bar)
# print(type(Bar))

class Mymeta(type):
    def __init__(self,class_name,class_bases,class_dic):
        for key in class_dic:
            if not callable(class_dic[key]):continue
            if not class_dic[key].__doc__:
                raise TypeError("小子，你没有写注释，赶紧去写")
        #type.__init__(self,class_name,class_bases,class_dic)
class Foo(metaclass=Mymeta):
    x=1
    def run(self):
        # "run function"
        print("running")
# print(Foo.__dict__)
# print(Foo.run.__doc__)







