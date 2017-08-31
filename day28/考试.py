#py4测试题
# 1、8<<2等于？
# print(8<<2)
# 32

#2、通过内置函数计算5除以2的余数
# print(divmod(5,2))
# (2, 1)余数为1

#3、s=[1,"h",2,"e",[1,2,3],"l",(4,5),"l",{1:"111"},"o"],将s中的5个字符提取出来并拼接成字符串。
# s=[1,"h",2,"e",[1,2,3],"l",(4,5),"l",{1:"111"},"o"]
# s1=[]
# for i in s:
#     if type(i) is str:
#         s1.append(i)
# print("".join(s1))

#4、判断"yuan"是否在[123,(1,"yuan"),{"yuan":"handsome"},"yuanhao"],如何判断以及对应结果？
# l=[123,(1,"yuan"),{"yuan":"handsome"},"yuanhao"]
# if "yuan" in l:
#     print("在")
# else:
#     print("不在")
# 不在

# 5、l=[1,2,3]
#    l2=l.insert(3,"hello")
#    print(l2)
#    执行结果并解释为什么？
#执行结果是None，因为列表是可变数据类型，是在原来的基础上进行增删改的并没有新开辟一块新的内存空间

# 6、 a=[1,2,[3,"hello"],{"egon":"aigan"}]
# 	b=a[:]
#
# 	a[0]=5
# 	a[2][0]=666
#
# 	print(a)
# 	print(b)
#     #计算结果以及为什么？
#print(a)为[5, 2, [666, 'hello'], {'egon': 'aigan'}]
#print(b)[1, 2, [666, 'hello'], {'egon': 'aigan'}]
#b=a[:]后，b和a都指向一个列表的内存地址,由于两个列表中的元素都一样，所以类表内存地址中指向元素的也是一样的，但是整形是不可变的，所以把列表a中的1换成5会改变a中的值
#但作为列表的元素就不一样了，因为指向列表后还会在指向列表中的元素所在的地址，所以列表中的元素改变会跟着改变

#7使用文件读取，找出文件中最长的行的长度（用一行代码解决）？
# print(max(len(i) for i in open("a.txt",encoding="utf8")))

#8
# def add(s, x):
#     return s + x
# def generator():
#     for i in range(4):
#         yield i
# base = generator()
# for n in [1, 11]:
#     base = (add(i, n) for i in base)
# print(list(base))

'''
生成器表达式在没有被next的时候它只是一个表达式，只是一个表达式，不是具体的值
当for n in [1, 11]运行完后，n的值就为11了，这个题可以写成以下这种
'''

# def add(s, x):
#     return s + x
# def generator():
#     for i in range(4):
#         yield i
# base = generator()
# n=1
# base = (add(i, n) for i in base)
# n=11
# base = (add(i, n) for i in base)
# print(list(base))


# 9  hello.py (gbk方式保存)：
#    ＃coding：GBK
#    print(“老男孩”)
#
#    如果用py2，py3下在cmd下运行回报错吗？为什么并提出解决方案？ （编码）
#不会报错因为已经声明用GBK编码和解码了

#10 通过函数化编程实现5的阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# def func(n,s=1):
#     for i in range(1,n+1):
#         s *=i
#     print (s)
# func(5)



#11 打印如下图案：

        #    ＊
        #   *＊*
        #  **＊**
        # ****＊**
        #  **＊**
        #   *＊*
        #    *

# s = '$'
# n = 1
# while n < 7:
#     print(s.center(n,'*').center(15))
#     n += 2
# while n > 0:
#     print(s.center(n,'*').center(15))
#     n -= 2


# def func(x,n):
#     if x == 0:
#         return
#     i="*"*n
#     print(i.center(15))
#     n += 2
#     func(x-1,n)
#     print(i.center(15))
# func(4,1)

# 12
# 		def outer():
# 	        count = 10
# 	        def inner():
# 	            count = 20
# 	            print(count)
# 	        inner()
# 	        print(count)
#         outer()
#
#         （1）分析运行结果？
#         （2）如何让两个打印都是20
#（1）outer函数中的print(count)为10，inter函数中的print(count)为20
#（2）
# def outer():
#     count = 20
#     def inner():
#         print(count)
#     inner()
#     print(count)
# outer()

#13 输入一个年份，判断是否是闰年？
# year=int(input("input a year:" ))
# if year%4 == 0:
#     print(str(year)+"年是闰年")

#14 任意输入三个数，判断大小？
# s=input("请任意输入三个数以','隔开：")
# l=s.split(",")
# print(sorted([int(i) for i in l]))

# 15 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222
#    ，几个数相加以及a的值由键盘控制。
# a=input("input a number:")
# n=int(a)
# def func(a,n):
#     n


# 16
# f=open("a")
#
# while 1:
#     choice=input("是否显示:[Y/N]:")
#     if choice.upper()=="Y":
#         for i in f:
#             print(i)
#     else:
#         break

	# 请问程序有无bug，怎么解决？
#有BUG，比如输入数字和空格都会有问题
# f=open("a")
# while 1:
#     choice=input("是否显示:[Y/N]:").strip()
#     if choice.upper()=="Y":
#         for i in f:
#             print(i)
#     elif choice.upper()=="N":
#         break
#     else:
#         continue

# 17def foo():
# 	    print('hello foo')
#         return()
# 	def bar():
#         print('hello bar')
#
#
#     （1）为这些基础函数加一个装饰器，执行对应函数内容后，将当前时间写入一个文件做一个日志记录。
#     （2）改成参数装饰器，即可以根据调用时传的参数决定是否记录时间，比如@logger(True)
# (1)
# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start_time=time.time()
#         with open("log_file","r+",encoding="utf8") as f:
#             f.write(start_time)
#         func()
#     return wrapper
# @timer
# def foo():
#     print('hello foo')
#
# @timer
# def bar():
#     print('hello bar')


# (2)
# import time
# def logger(flag):
#     def timer(func):
#         def wrapper(*args,**kwargs):
#             if flag == True:
#                 start_time=time.time()
#                 with open("log_file","r+",encoding="utf8") as f:
#                     f.write(start_time)
#                 func()
#                 return
#             else:
#                 func()
#                 return
#         return wrapper
#     return timer
# @logger(True)
# def foo():
#     print('hello foo')
# @logger(True)
# def bar():
#     print('hello bar')


# 18 三次登陆锁定：要求一个用户名密码输入密码错误次数超过三次锁定？
#在用户登录文件user_file里有 {"agon":"123","alex":"3714","sb":"456"}
# with open("user_file","r+",encoding="utf8") as f:
#     f.write('{"agon":"123","alex":"3714","sb":"456"}')
# with open("auth_file","w",encoding="utf8") as f2:
#     f2.write('{"name":None,"login":False}')
#
# def auth(func):
#     def wrapper():
#         l = []
#         while True:
#             name=input("input username:")
#             if name == "q":
#                 exit()
#             with open("black_file",encoding="utf8") as f_read,open("user_file",encoding="utf8") as f1_read:
#                 black = f_read.read()
#                 user = f1_read.read()
#                 if name not in black and name in user:
#                     password=input("input password:")
#                     with open("user_file",encoding="utf8") as f:
#                         x = eval(f.read())
#                         if name in x and password == x[name]:
#                             print("auth successful")
#                             res=func()
#                             return res
#                         else:
#                             print("auth error")
#                             l.append(name)
#                             count=l.count(name)
#                             if count==3:
#                                 print("Locked!")
#                                 with open("black_file","r+",encoding="utf8") as f_write:
#                                     f_write.write(name)
#                 if name not in black and name not in user:
#                     print("Not Found!")
#                     continue
#                 else:
#                     print("Locked!")
#                     continue
#     return wrapper
# @auth
# def home():
#     print('Welcome home page!')
# home()





