import os,time
#os模块是完成操作系统调用功能的
# print(os.getcwd()) #获取当前的工作目录，即当前Python脚本工作的目录

# print(os.chdir("D:\py_fullstack_s4\day32")) #修改路径,修改路径后下面跟着的文件操作等同于在新的目录中进行
# f=open("11.txt","w")#11.txt被建到了day32里

# print(os.curdir)#currentdir当前目录，返回.
# print(os.pardir)#获取当前目录的父目录字符串名：..
# os.makedirs("aaa/bbb/ccc")#可生成多层递归目录
# os.removedirs("aaa/bbb/ccc")#递归删，空的就删
# print(os.listdir(r"D:\py_fullstack_s4\day33"))#以列表的形式打印day33目录下的内容
# r=os.stat(r"D:\py_fullstack_s4\day32\11.txt")
# print(time.ctime(r.st_atime))
# "yuan"+os.sep+"image"
# print(os.name)
# abs=os.path.abspath("11.txt")
# print(os.path.basename(abs))
# print(os.path.dirname(abs))
# s1="D:\py_fullstack_s4"
# s2=r"day32\11.txt"
# print(s1+os.sep+s2)
# print(os.path.join(s1,s2))
# print(os.environ)