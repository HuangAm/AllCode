#反射当前模块的属性
#这个文件为test
#模块就是文件，定义文件也是定义一堆名字，一切皆对象，只要是对象就能.出来名字
#名字就对应属性的概念
import sys
#导入一个模块名
x=1111
class Foo:  #定义一个类名
    pass

def s1():  #定义一个函数名
    print("s1")

def s2():  #定义一个函数名
    print("s2")

# print(__name__)#__main__
# __name__能够用来区分文件(模块)是直接运行(作为脚本)文件还是作为模块被导入
#如果是脚本的话，打印__main__，如果作为模块被导入时，打印模块名
#脚本：把一个文件当成一个独立的程序去运行
#如何在自己模块获取自己模块(要结合上面的__name__知识点去理解)
    #不能再自己模块中导入自己模块
    #下面就是正确用法，需要借助sys模块
this_module=sys.modules[__name__] #这就相当于拿到当前的模块test作为对象
print(this_module)#<module '__main__' from 'D:/py_fullstack_s4/day31/test.py'>
print(hasattr(this_module,"s1"))
print(getattr(this_module,"s2"))

#如何在当前模块调用其他模块(比较简单)
    #比如我现在有两个文件，在同一级目录，test和test1我在test1中调用test会出现下面的情况
