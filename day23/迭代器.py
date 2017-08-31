#只要对象本身有__iter__方法，那么他就是可迭代的
# d={'a':1,'b':2,'c':3}
# i=d.__iter__()
# #i=iter(d)#和上面的等式一模一样   i就是迭代器
# print(i.__next__())#等同于下面
# print(next(i))#等同于上面
# print(i.__next__())
# print(i.__next__())


# d={'a':1,'b':2,'c':3}
# i=d.__iter__()#这是一个iter函数，等同于iter(d)  i就是迭代器
# #i=iter(d)#和上面的等式一模一样   i就是迭代器
# while True:
#     try:                          #try...except捕捉异常
#         print(next(i))
#     except StopIteration:
#         break

# l=['a','b','c','d','e']
# i=l.__iter__()
# # i=iter(i)
# while True:
#     try:                        #try...except捕捉异常
#         print(next(i))
#     except StopIteration:
#         break
# f = lambda a,b,c:a+b*c
# print(f(1,2,3))
# print(f(2,3,4))

# s="hello"
# s.__iter__()
# print(isinstance(s,Iterable))


# d={'a':1,'b':2,'c':3}
# for k in d:#for循环在这里做的事可以理解为 d=d.__iter__()
#     print(k)
#而且for循环自动加了next()函数，自动next下一个，牛逼！
#而且for循环把while循环当中的try...except所做的是给做了，牛逼！

# s={1,2,3,4}#for循环列表
# for i in s:
#     print(i)
#
# with open("a.txt","r") as f:
#     for line in f:
#         print(line,end="")

# f=open("a.txt","r")
# i=f.__iter__()
# while True:
#     try:
#         print(next(i),end="")
#     except StopIteration:
#         break