#abs()绝对值函数
# print(abs(-1))
# print(abs(0))

#all()函数如果后面跟的可迭代对象为空，返回true
# 如果后面跟的可迭代对象不为空，all会把他变成迭代器，取一个值进行一次bool判断，全为真才返回真
# print(all(''))
# print(all((1,'',2)))
# print(all((1,"",2,None)))

#any函数，正好与all函数相反
# print(any(""))#空格也算值，不算空，什么也不写才算空
# print(any([]))
# print(any([None,0,[],{},1]))#True

#bin()把数字转换成二进制
# print((bin(3)))

#callable()判断是否可以被调用，如果能被调用就返回True否则返回False
# def test():
#     pass
# print(callable(test))
# print(callable(sum))

#chr()和ord()是根据ASCII码互相转换的东西
# print(chr(67))
# print(ord("C"))

#compile()把字符串编译为字节码

#complex()复数的内置函数，和list类似
# x=1-2j
# print(x.real)
# print(x.imag)
# x=complex(1-2j)
# print(x.real)
# print(x.imag)

#数据类型
#int()
# num=1 #num=int(1)
# print(type(num))          #查看num的类型
# print(isinstance(num,int))#两种判断类型的方式通用，判断num是否为int类型
# print(num is 1)#is是身份运算，根据id去判断身份
#float
#bool

#str()
# x='asdf'#x=str('asdf')
# print(str(1))
# print(str({'a':1}))

#list()
# x=[]
# x=list(i for i in range(10))
# print(x)

#tuple()

#dict()
# d={'a':1}
# d=dict(x=1,y=2,z=3)
# print(d)

#set()
# s={1,2,3,4}
# print(s)
# s.add(5)
# print(s)

# frozenset()#加可迭代对象变为不可变的集合，当然不全
# f=frozenset({1,2,3,4})
# print(type(f))#没有add和remove方法是一个不可变集合
# f=frozenset((1,2,3,4))
# print(type(f))

#dir()可以看到对象能够调用哪些方法
# print(dir(sum))

#divmod()#"" Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """
# print(divmod(10,3))#用于前端分页功能

#enumerate(iterable,start=0)#参数先是可迭代对象，然后是初始值
# for i in enumerate(['a','b','c','d']):
#     print(i)
# for i in enumerate(['a', 'b', 'c', 'd'],10):
#     print(i)
# for i in enumerate({'x':1,'y':2}):
#     print(i)

#hash()#哈希算法，映射，用于校验数据的完整性
# print(hash('asdf'))
# print(hash('asdf'))

#hex()十进制转十六进制
# print(hex(10))

#id()查看身份相当于省份证号
#0到256包括256都是相等的，从257开始就变了
#字符串都是一样的

#max(args,key=function,default)和min()
# print(max(1,2,3,4,10,3))
# print(min(1,2,3,4,10,3))
# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# print(max(salaries))#默认比的是key
# print(max(salaries.values()))
# def get_value(k):
#     return salaries[k]
# print(max(salaries,key=get_value))#直接写函数名而不是函数名+()
#max把可迭代对象salaries变为迭代器，next一次的一个值，并将这个值传给后面的函数，用函数的运行结果进行比较，但是最终排序的时候还是以默认的(key)方式排
#在这里我们只是改变了比较大小时的比较依据，打印结果的依据没有改变

#zip(iter1,iter2)拉链,两个参数都是可迭代对象
# l1=[1,2,3]
# s='hel'
# res=zip(l1,s)#res是迭代器
# for i in res:
#     print(i)  #取出i是元组形式的
# pp=zip(salaries.values(),salaries.keys())#pp是迭代器
# print(max(pp)) #打印出的结果也是元组形式

#sorted()#Return a new list containing all items from the iterable in ascending order.(升序）
# l=[3,4,1,0,9,10]
# print(sorted(l))#返回值是列表，默认是升序,按ASCII码进行排
# print(sorted(l,reverse=True))#降序,由大到小
# s='hello abc'
# print(sorted(s))#[' ', 'a', 'b', 'c', 'e', 'h', 'l', 'l', 'o']
# print(sorted(salaries))
# print(sorted(salaries,key=lambda k: salaries[k]))

#map(func, *iterables),map作用就是把一个没有用的可迭代对象加工成需要的可迭代对象，映射的方式
# l=[1,2,3,7,5]
# m=map(lambda item:item**2,l)
# print(m)
# for i in m :
#     print(i)
# print(list(m))
# name_l=['alex','zhejiangF4','yuanhao','wupeiqi']
# m=map(lambda name:name+"SB",name_l)
# print(list(m))

# reduce(function, sequence, initial=None)#合并
# from functools import reduce
# l=list(range(100))
# print(l)
# print(reduce(lambda x,y:x+y,l))#默认初始值为0，看到的并不是真的，他还是直窜一个值，只是最开始有个默认的0
# print(reduce(lambda x,y:x+y,l,100))#默认初始值为100

#filter(function or None, iterable)#功能就是过滤,左边函数的返回值如果是True的话才算过滤出来的结果
#左边函数的参数是有右边可迭代对象变为迭代器next出来后传过去的
# name_l=[
#     {'name':'egon','age':18},
#     {'name':'dragon','age':100},
#     {'name':'gaoluchuan','age':9000},
#     {'name':'fsw','age':10000},
# ]
# f=filter(lambda d: d['age'] > 100,name_l)
# print(f)
# for i in f:
#     print(i)

#pow(x,y,z)Equivalent to x**y (with two arguments) or x**y % z (with three arguments)
# print(pow(3,2))#3**2
# print(pow(3,2,2))#3**2%2

#reversed()反转，结果是一个迭代器

#round()五舍六入
# print(round(5.5))
# print(round(5.6))

#slice()
# l=[1,2,3,4,5,6,7,9]
# print(l[2:4:2])
# s=slice(2,5,2)
# print(l[s])

#vars()Without arguments, equivalent to locals().With an argument, equivalent to object.__dict__.
# print(vars())
# print(vars() is locals())

#__import__()#可以把字符串形式的模块导入
# import time
# print(time)
# m=__import__("time")
# print(m)
# m.sleep(3)#因为不是内置的所以没有TAB功能了




















