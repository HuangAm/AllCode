# import time
# class Foo:
#     pass
# x=1
# def funname():
#     x=100
#     print(x)
# funname()
# print(x)
#内置名称空间
#全局名称空间
#局部名称空间
# def foo():
#     print("from foo")
#     bar()
# def bar():
#     print("from bar")
# foo()


#嵌套定义
# x=1111111111111111111111111
# def f1():
#     # x=1
#     print("----->f1",x)
#     def f2():
#         # x=2
#         print("--->f2",x)
#         def f3():
#             # x=3
#             print("-->f3",x)
#         f3()
#     f2()
# f1()


#嵌套调用
# def my_max(x,y):
#     res=x if x>y else y
#     return res
# print(my_max(10,100))
# def my_max1(a,b,c,d):
#     res1=my_max(a,b)
#     res2=my_max(res1,c)
#     res3=my_max(res2,d)
#     return res3
# print(my_max1(1,23,3,4))

# def foo():
#     print('foo')
# print(foo)
#
# #函数可以被赋值
# f=foo
# print(f)
# f()
#
# #把函数当成参数传递
# def bar(func):
#     print(func)
#     func()
# bar(foo)
#
# #把函数当成返回值
# def bar(func):
#     print(func)
#     return func
# f=bar(foo)
# print(f)
# f()


#闭包
# x=1000000000
# def f1():
#     x=1
#     y=2
#     def f2():
#         print(x)
#         print(y)
#     return f2
# f=f1()
# print(f)
# print(f.__closure__)
# print(f.__closure__[0].cell_contents)
# print(f.__closure__[1].cell_contents)
# ----------------------------------------------------------------------------------------------------------------------------------
# <function f1.<locals>.f2 at 0x0000000000A7E1E0>
# (<cell at 0x0000000000686D08: int object at 0x000000005E5522D0>, <cell at 0x0000000000686D38: int object at 0x000000005E5522F0>)
# 1
# 2
#

# x=1
# def f1():
#     def f2():
#         print(x)

#爬虫
from urllib.request import urlopen
def get(url):
    return urlopen(url).read()
print(get('http://www.baidu.com'))


#专门爬百度页面
def f1(url):
    def f2():
        s=urlopen(url).read()
        print(s)
    return f2
baidu=f1('http://www.baifu.com')
baidu()






