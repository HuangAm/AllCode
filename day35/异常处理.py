# try:
#     print("====")
#     print(x)
#     print("====")
#     print("====")
# except KeyError as x:
#     print(x)
# except NameError as e:
#     print(e)
# print(111111)

# s1="hello"
# try:
#     int(s1)
# except IndexError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print("try内代码块没有异常则执行我")
# finally:
#     print("无论异常与否，都会执行就那个该模块，通常是进行清理工作")
#finally下应该加一些





try:
    #第一段代码
    num1=input('>>: ') #输入一个字符串试试
    int(num1) #我们的正统程序放到了这里,其余的都属于异常处理范畴
    #第二段代码
    num2=input('>>: ') #输入一个字符串试试
    int(num2)
    #第三段代码
    num3=input('>>: ') #输入一个字符串试试
    int(num3)
except:
    print(123)






















