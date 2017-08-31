#这个文件事test1
#如何在当前模块调用其他模块(比较简单)
    #比如我现在有两个文件，在同一级目录，test和test1我在test1中调用test会出现下面的情况
import test
print(test)#<module 'test' from 'D:\\py_fullstack_s4\\day31\\test.py'>
#会把test模块的完整路径打印出来
#现在我们把test模块作为一个对象
print(test.x)
print(test.s1)
test.s1()