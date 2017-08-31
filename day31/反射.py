class People:
    country="China"
    def __init__(self,name):
        self.name=name
    def walk(self):
        print("%s is walking" %self.name)
p=People("egon")
# 检测是否含有某属性
# print(hasattr(p,"name"))#判断对象p有没有这个属性
# 相当于if "name" in p.__dict__

#获取属性,通过__dict__的key值获取value
# x=getattr(p,"name")#由下面的打印结果看，她就相当于p.name
# print(x)#egon,相当于print(p.name)
# y=getattr(p,"xxx","找不到")
# print(y)#找不到,getattr可以自定义返回值

#设置属性,__dict__的增，改
# setattr(p,"name","alex")
# setattr(p,"sb",True)
# setattr(p,"bs",lambda self:self.name+"sb")#可以增加函数属性
# s=getattr(p,"bs")#调用增加的函数属性
# print(s(p))
# print(p.__dict__)#就是加到这个字典里面了

#删除属性
# delattr(p,"bs")#删除函数属性就是删除函数名
# delattr(p,"sb")#删除数据属性
# print(p.__dict__)

# 总结----------------------------------------------------------------
#hasattr(object,"name") #查看，object可以是对象，类，模块，name是属性名
#相当于判断能不能找的到"name" 这个名字，如果可以找到print返回True

# getattr(object,"name",default=None) #获取,object可以是对象，类，模块
# p.name

# setattr(x,"y","v") #修改，x可以是对象，类，模块，y是属性名，v是新值
# p.name="alex"

# delattr(x,"y")#删除，x可以对象，类，模块，y是属性名
# del p.name
# -----------------------------------------------------------------








# import sys
# x=1111
# class Foo:
#     pass
# def s1():
#     print("s1")
# def s2():
#     print("s2")
# this_module = sys.modules[__name__]
# print(this_module)
# print(hasattr(this_module,"s1"))
# print(hasattr(this_module,"s2"))
# print(getattr(this_module,"s2"))
# print(this_module.s2)
# print(this_module.s1)
# class People:
#     country="China"
#     def __init__(self,name):
#         self.name=name
#     def walk(self):
#         print("%s is walking" %self.name)
# p = People("egon")
# print("name" in p.__dict__)
# print(hasattr(p,"name"))
# print(hasattr(p,"name123"))
# print(hasattr(p,"country"))
# print(hasattr(People,"country"))
# print(hasattr(People,"country"))

#getattr(object,"name",default=None)
#p1.name
# res = getattr(p,"country")
# print(res)
# f=getattr(p,"walk")
# print(f)
# f1=getattr(People,"walk")
# print(f1)
# f()
# f1(p)
# print(getattr(p,"xxx","none"))
# if hasattr(p,"walk"):
#     func=getattr(p,"walk")
#     func()
# p.sex="male"
# print(p.sex)
# print(p.__dict__)
# # print(p.age)
# print(getattr(p,"age",18))

# delattr(x,y)
#del p.name
# delattr(p,"name")
# print(p.__dict__)

# ------------------------------------------------------------------------------------------------------------------------
#hasattr(object,"name") #查看，object可以是对象，类，模块，name是属性名
# getattr(object,"name",default=None) #获取,object可以是对象，类，模块
# p.name
# setattr(x,"y","v") #修改，x可以是对象，类，模块，y是属性名，v是新值
# p.name="alex"
# delattr(x,"y")#删除，x可以对象，类，模块，y是属性名
# del p.name
# ------------------------------------------------------------------------------------------------------------------------

# m=input("请输入你要导入的模块：")
# m1=__import__(m)
# print(m1)#<module 'time' (built-in)>
# print(m1.time())
#推荐使用方法
# import importlib
# m=input(">>: ")
# t=importlib.import_module(m)
# print(t.time())
# class Bar:
#     pass
# class Foo(Bar):
#     pass
# f=Foo()
# print(Foo.__bases__)
# print(isinstance(f,Foo))
# print(issubclass(Foo,Bar))
