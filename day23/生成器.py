# def test():
#     print("first")
#     yield 1#return 1
#     yield 2
#     yield 3
# g=test()#g是生成器,是可迭代对象是迭代器
# print(g)
# next(g)
# next(g)#next超出范围还是会报错
# print(next(g))#next可以触发迭代器往下走
# #运行原理如下：
# #print(next(g))
# #print(next(test())
# #运行test()先print("first")然后碰到yield返回1
# #然后结束运行
#
# #用for循环输出g
# for i in g:#
#     print(i)
#
# def countdown(n):
#     print("start")
#     while n>0 :
#         yield n
#         n-=1
#     print("done")
# g=countdown(5)#g是生成器,是可迭代对象是迭代器
# #用next一步一步输出g
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))#超出范围，打印done后报错StopIteration
# # 用for循环g
# for i in g:
#     print(i)
# #用while循环输出g
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break
#因为迭代器是一次性的，所以上边三种循环输出方式只能同时用一种