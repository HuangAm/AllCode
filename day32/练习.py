#面向对象的程序设计只能解决扩展性
#创建一个类就会创建一个名称空间，用来存储类中定义的所有名字，这些名字称为类的属性
#类有两种属性数据属性和函数属性
#软件重用的重要方式，除了继承之外还有另外一种方式，即：组合
#组合指得是，在一个类中以另外一个类的对象作为数据属性，称为类的组合
#组合指的是有的关系，继承指得是是的关系
#接口，函数的组合体
#继承的两种用途继承基类的方法，并作出自己的改变或者扩展，声明某个子类兼容于某个基类，定义一个接口类interface，接口类中定义了一些接口名（就是函数名）并未实现接口的功能，子类继承接口类，并且实现接口中的功能
#归一化设计
#抽象类是一个特殊的类，它的特殊之处在于只能被继承，不能被实例化

# import abc
# class All_file(metaclass=abc.ABCMeta):
#     all_type="file"
#     @abc.abstractmethod
#     def read(self):
#         "子类必须定义读功能"
#         pass
#     @abc.abstractmethod
#     def write(self):
#         pass
#
# class Txt(All_file):#子类继承抽象类，但是必须定义read和write方法
#     def read(self):
#         print("文本数据的读取方法")
#         # pass
#     def write(self):
#         print("文件数据的读取方法")
#         # pass
# a=Txt()
# a.read()
#抽象类是一个介于类和接口之间的一个概念，同时具备类和接口的部分特性，可以用来实现归一化设计
#继承顺序，新式类广度优先，经典类深度优先，super只用于心事类，__mro__
#封装分为两个层面，创建类和对象的时候就会创建二者的名称空间，我们只能用类名.或者obj.的方式去访问里面的名字，这本身就是一种封装
#对于这一层面的封装(隐藏)，类名.和实例名.就是访问隐藏的属性的接口
#第二个层面的封装：类中把某些属性和方法隐藏起来(或者说定义成稀有的)只有在类的内部可以直接使用，外部无法访问，或者留下少量接口（函数）公外部访问
#用property，尊寻统一访问的原则

# class Foo:
#     def __init__(self,val):
#         self.__NAME=val #将所有的数据属性都隐藏起来
#     @property
#     def name(self):
#         return self.__NAME
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("%s must be str"%value)
#         self.__NAME=value
#     @name.deleter
#     def name(self):
#         # del self.__NAME
#         raise TypeError("Can not delete")
#
# f = Foo("egon")
# print(f.name)

#staticmethod静态方法 classmethod 类方法  property
# class Foo(object):
#     pass
# obj=Foo()
# class Bar(Foo):
#     pass
# print(isinstance(obj,Foo))
# print(issubclass(Bar,Foo))

# class BlackMedium:
#     feature="Ugly"
#     def __init__(self,name,addr):
#         self.name=name
#         self.addr=addr
#     def sell_house(self):
#         print("%s sb"%self.name)
#     def rent_house(self):
#         print("%s sssb"%self.name)
# b1=BlackMedium("www","huihiu")
#
# print(hasattr(b1,"sell_house"))
# print(getattr(b1,"feature"))
# setattr(b1,"age",18)
# setattr(b1,"func",lambda self:self.name+"sb")
# print(b1.func(b1))
#
# print(b1.__dict__)

#类也是对象可以反射
#在Python中反射通过字符串的形式操作对象相关的属性。字符串一般都是外部传进来的，反射就是把这些字符串与属性属性对应起来
#程序可以访问、检测、修改他本身状态或行为的一种能力
#程序可以访问、检测、修改他本身状态或行为的一种能力

# import sys
# def s1():
#     print("s1")
# def s2():
#     print("s2")
# x=1
#
# this_module=sys.modules[__name__]
# print(this_module)
# print(hasattr(this_module,"s1"))
# print(hasattr(this_module,"s2"))
# print(getattr(this_module,"x"))
# import sys
# def add():
#     print("add")
# def delete():
#     print("delete")
# def change():
#     print("change")
# def search():
#     print("search")
# this_module=sys.modules[__name__]
# # print(this_module)
# while True:
#     cmd=input(">>:").strip()
#     if not cmd:continue
#     if hasattr(this_module,cmd):
#         getattr(this_module,cmd)()

#实现可插拔机制
#动态导入模块
# import importlib
# m=input(">>:")
# t=importlib.import_module(m)
# print(t.time())
# class Foo:
#     x = 1
#     def __init__(self,y):
#         self.y = y
#     def __getattr__(self, item):
#         print("----------->",)
# date_dic={
#     'ymd':'{0.year}:{0.month}:{0.day63}',
#     'dmy':'{0.day63}/{0.month}/{0.year}',
#     'mdy':'{0.month}-{0.day63}-{0.year}',
# }
# class Date:
#     def __init__(self,year,month,day63):
#         self.year=year
#         self.month=month
#         self.day63=day63
#
#     def __format__(self, format_spec):
#         if not format_spec or format_spec not in date_dic:
#             format_spec='ymd'
#         fmt=date_dic[format_spec]
#         return fmt.format(self)
#
# d1=Date(2016,12,29)
# print(format(d1))
# print('{:mdy}'.format(d1))
#__slots__:是一个类变量，变量值可以是列表，元组，或者可迭代对象，也可以是一个字符串（意味着所有实例只有一个数据属性）
#使用了__slots__后我们不能再给实例添加新的属性了，比如多继承，大多素情况下，你应该只在那些被经常使用到的用做数据结构的类上定义
#比如在程序中需要创建某个类的几百万个实例对象
#更多的是作为一个内存优化工具
# class Foo:
#     def __init__(self,x):
#         self.x=x
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.x >= 10:
#             raise StopIteration
#         n=self.x
#         self.x +=1
#         return self.x
# f=Foo(3)
# for i in f:
#     print(i)

# class Range:
#     def __init__(self,stop,start=0):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         n=self.start
#         self.start +=1
#         return n
# f=Range(10)
# for i in f:
#     print(i)


# class Range:
#     def __init__(self,stop,start=0):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         n=self.start
#         self.start+=1
#         return n
# for i in Range(10):
#     print(i)

# class Fib:
#     def __init__(self):
#         self.__a=0
#         self.__b=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__a,self.__b=self.__b,self.__a+self.__b
#         return self.__a
# f1=Fib()
# print(f1.__next__())
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# class Foo:
#     pass
# class Bar(Foo):
#     pass
# b=Bar()
# print(b.__module__)
# print(Bar.__module__)
# print(Bar.__class__)
# print(b.__class__)

#析构方法，当对象内存中被释放时，自动触发执行
# class Foo:
#     def __del__(self):
#         print("执行我了")
# f1=Foo()
# del f1
# print("---->")

# class Open:
#     def __init__(self,filepath,mode="w+",encoding="utf-8"):
#         self.filepath=filepath
#         self.mode=mode
#         self.encoding=encoding
#         self.f=open(filepath,mode=mode,encoding=encoding)
#     def write(self,line):
#         if not isinstance(line,str):
#             raise TypeError("%s must be str" %line)
#         self.f.write(line)
#     def __getattr__(self, item):
#         return getattr(self.f,item)
#     def __enter__(self):
#         return self  #如果是self.f的话write和getattr就没有用了
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("exit")
#         print("exc_type",exc_type)
#         print("exc_val",exc_val)
#         print("exc_tb",exc_tb)
#         return True  #这里如果没有return true的话脚本到这里就崩了，有了他就正常走了
# with Open("a.txt") as f:
#     f.write("hello")
#     f.seek(0)
#     print(f.read())
#     raise TypeError("我下边的这个prient就不运行了")
#     print("hello 看不到我了") #我上变有raise我就永远不会被执行
# print("lalallaala")#如果没有return True 我就不会被执行

# class Foo:
#     def __init__(self):
#         pass
#     def __call__(self, *args, **kwargs):
#         print("__call__")
# obj = Foo()
# print(callable(obj))
# print(callable(Foo))
# print(callable(Foo()))
# print(isinstance(Foo,type))#True
# print(Foo.__class__)#<class 'type'>








































































