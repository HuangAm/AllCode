#这里和之前的那四个东西，就多了触发运行
#三个attr本质上都是对__dict__去操作
#一碰到给对象设置(增,改)属性就会触发__setattr__(self, key, value)
#一碰到给对象删除属性就会触发__delattr__(self, item)
#属性不存在的情况下才会触发 __getattr__(self, item)
#内置函数都是操作的内置的东西，__attr__操作__dict__

# class Foo:
#     x=1
#     def __init__(self,y):
#         self.y=y
#
#     def __getattr__(self, item):
#         print('----> from getattr:你找的属性不存在')
#
#
#     def __setattr__(self, key, value):
#         print('----> from setattr')
#         # self.key=value #这就无限递归了,你好好想想
#         # self.__dict__[key]=value #应该使用它
#
#     def __delattr__(self, item):
#         print('----> from delattr')
#         # del self.item #无限递归了
#         self.__dict__.pop(item)
#
# #__setattr__添加/修改属性会触发它的执行
# f1=Foo(10)
# print(f1.__dict__) # 因为你重写了__setattr__,凡是赋值操作都会触发它的运行,你啥都没写,就是根本没赋值,除非你直接操作属性字典,否则永远无法赋值
# f1.z=3
# print(f1.__dict__)
#
# #__delattr__删除属性的时候会触发
# f1.__dict__['a']=3#我们可以直接修改属性字典,来完成添加/修改属性的操作
# del f1.a
# print(f1.__dict__)
#
# #__getattr__只有在使用点调用属性且属性不存在的时候才会触发f1.xxxxxx

# class Foo:
#     def __init__(self,x):
#         self.name=x
#     #属性不存在的情况下才会触发
#     def __getattr__(self, item): #item就是属性名
#         print("getattr--->%s %s" %(item,type(item)))
# f = Foo("egon")
# print(f.name)
# print(f.xxxx)#会触发getattr

# class Foo:
#     def __init__(self,x):
#         self.name=x
#     def __setattr__(self, key, value): #f.name="alex" ==> self.key=value
#         if not isinstance(value,str):
#             raise TypeError("must be str")
#         self.__dict__[key]=value
#     def __delattr__(self, item):
#         self.__dict__.pop(item)

# class List(list):
#     def append(self, p_object):
#         if not isinstance(p_object,int):
#             raise TypeError("must be int")
#         super().append(p_object)
#     def insert(self, index, p_object):
#         if not isinstance(p_object,int):
#             raise TypeError("must be int")
#         super().insert(index,p_object)
#
# l=List([1,2,3])
# print(l)
# l.append(4)
# print(l)
# l.insert(0,-1)
# print(l)

