# 把对象操作属性模拟成字典的格式
# 之前是用.属性名的形式触发__attr__系列，现在是用[key]去触发__item__系列
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __getitem__(self, item):
#         print("getitem",item)
#         return self.__dict__
#     def __setitem__(self, key, value):
#         print("setitem")
#     def __delitem__(self, key):
#         print("del obj[key]时，我执行")
# f=Foo("egon")
# print(f.name)
# f["age"]=18
# del f["age"]
# print(f.__dict__)
# print(f["name"])

# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __getitem__(self, item):
#         return self.__dict__[item]
#     def __setitem__(self, key, value):
#         self.__dict__[key]=value
#     def __delitem__(self, key):
#         self.__dict__.pop(key)
# f=Foo("egon")
# f["agon"]="alex"
# print(f.__dict__)

# class Foo:
#     def __init__(self,x):
#         self.x=x
#     def __getattribute__(self, item):
#         print("不管是否存在，我都会执行")
#         return 22
# f=Foo(1)
# print(f.x)
# print(f.y)

class Foo:
    def __get__(self,instance,owner):
        print("触发get")
    def __set__(self,instance,value):
        print("触发set")
    def __delete__(self, instance):
        print("触发delete")
#包含这三个方法的新式类称为描述符，由这个类产生的实例进行属性的调用/赋值/删除，并不会触发这三个方法
f1=Foo()
f1.name="egon"
f1.name
del f1.name
#我靠，都不触发，什么鬼


