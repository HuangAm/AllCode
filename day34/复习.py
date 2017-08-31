#常用模块
#Python中只有类函数模块能够建立自己的名称空间
'''
time模块
在Python有时间戳，元组，格式化时间
'''
# import time
# print(time.time())
# print(time.localtime())#的对象可以调用他的数据属性
# print(time.strftime("%Y-%m-%d %H %M %S"))
# print(time.strftime("%Y-%m-%d %X"))
# print(time.strptime("2017-5-1","%Y-%m-%d"))
# print(time.asctime(time.localtime()))#把元组格式化输出
# print(time.ctime(123456789))#把时间戳变为格式化

# import random
# print(random.random()) #大于0小于1之间的小数
# print(random.randint(1,5))
# print(random.randrange(1,5))
# print(random.choice((1,2,3))) #多选一,参数是seq
# print(random.sample((1,2,3),2))#随机选两个以列表的形式返回
# print(random.uniform(1,3))#大于1小于3的浮点数
# item=[1,2,34,5]
# random.shuffle(item)#随机打乱次序
# print(item)
# import random
# def jkcode():
#     code=""
#     for i in range(5):
#         a=random.randint(0,9)
#         b=chr(random.randint(65,90))
#         c=random.choice([a,b])
#         code="".join([code,str(c)])#字符串的拼接保证是字符串，str(c)
#     return code
# print(jkcode())
# import random
# def v_code():
#     "随机取五个值，字母数字随机"
#     d=""
#     for i in range(5):
#         a=random.randint(0,9)#随机去一个数，在随机取一个字母，在随机组合
#         b=chr(random.randint(65,90))
#         c=random.choice([a,b])
#         d=d+str(c)
#     return d
# print(v_code())

#摘要算法,是十六进制的数值
# import hashlib
# md5=hashlib.md5()#括号中加盐
# # print(md5)
# # help(md5)
# md5.update("how to use md5 in python?".encode("utf8"))
# print(md5.hexdigest())#读取哈希值的方式
# print(md5.hexdigest())
# print(md5.hexdigest())
# md5.update("how to use md5 in python?".encode("utf8"))
# md5.update("lalalaalal".encode("utf8"))
# print(md5.hexdigest())#读取哈希值的方式29e26c50c7584a6a432c3f680c847cdf
# md5.update("lalalaalal".encode("utf8"))
# print(md5.hexdigest())#e3d33fb911bc1d1a1ba21de87bd3907e

#Python中os模块封装了操作系统的目录和文件操做要注意的是，这些函数有的在
#os模块中，有的在os.path模块中。
#Python内置的os模块也可以直接调用操作系统提供的接口函数
import os
'''
os.getcws()获取当前工作目录，即当前Python脚本工作的目录路径
os.chdir("dirname") 改变当前脚本共做目录了 cd
os.curdir   返回.
os.pardir  ..
os.makedirs(r"dir1/dir2") 可生成多层递归目录
os.removedirs("dirname1") 若目录为空，则无法删除，报错；相当于shell中rmdir
os.mkdir('dirname') 生成单击目录
os.rmdir("dirname") 删除单机空目录，若目录不为空则无法删除，报错
os.listdir("dirname") 列出指定目录下得所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove() 删除一个文件
os.rename("oldname","newname") 重命名文件/目录
os.stat("path/filename") 获取文件/目录信息
os.sep  当前系统的路径分割符
os.linesep 行终止符
os.pathsep 分割文件路径的字符串
os.name 输出字符串当前地使用平台
os.system("bash command") 运行shell命令直接显示
os.environ 获取系统环境变量
os.path.abspath(path) 返回path规范化的绝对路径
os.path.split(path) 将path分割成目录和文件名按元组返回

'''
# print(os.environ)
# print(os.path.abspath("day33\os模块.py"))
# print(os.path.split('D:\py_fullstack_s4\day34\day33\os模块.py'))
# print(os.path.basename('D:\py_fullstack_s4\day34\day33\os模块.py'))
# print(os.path.exists(r"day33\os模块.py"))
# print(os.path.isabs(r"D:\py_fullstack_s4\day34\day33\os模块.py"))
# print(os.path.isfile(r"D:\py_fullstack_s4\day33\os模块.py"))
# print(os.path.join("day34","D:\py_fullstack_s4","day33\os模块.py"))
# print(os.path.getatime("D:\py_fullstack_s4\day33\os模块.py"))

#sys模块包含了与Python解释器和它的环境有关的函数
import sys,time
# print(sys.version)
# print(sys.platform)
# print(sys.path)
# print(sys.maxsize)
# print(sys.argv)
# username=sys.argv[1]
# password=sys.argv[2]
# print(username,password)
# for i in range(10):
#     sys.stdout.write("#")
#     time.sleep(1)
#     sys.stdout.flush()
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(filename)s [line:%(lineno)d %(levelname)s %(message)s]",
#                     datefmt="%Y-%m-%d %H:%M:%S",
#                     filename="alex",
#                     filemode="a"
#                     )
# logging.debug("debug message")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

# import logging
#
# logger=logging.getLogger() #实力话出一个对象
# fh=logging.FileHandler("egon") #创建一个流对象
# sh=logging.StreamHandler()#创建一个屏幕流对象
# # fm=logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)")
# fm=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s") #不要少了s
# fh.setFormatter(fm)
# sh.setFormatter(fm)
# logger.addHandler(fh)
# logger.addHandler(sh)
# logger.setLevel(logging.DEBUG)
# logger.debug("logger debug message")
# logger.info("logger info message")
# logger.warning("logger hjkl")
# logger.error("logger ghjk")
# logger.critical("logger hjk")






