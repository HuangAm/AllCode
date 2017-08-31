# 1 小程序：根据用户输入选择可以完成以下功能：
#     创意文件，如果路径不存在，创建文件夹后再创建文件
#     能够查看当前路径
#     在当前目录及其所有子目录下查找文件名包含指定字符串的文件
# import os,sys
# def creatfile(fp):
#     if os.path.isdir(fp):
#         open("qw.txt","w")
#     else:
#         os.mkdir(fp)
#         os.chdir(fp)
#         open("qw.txt","w")
#
# def filepath(fp):
#     # print(fp)
#     print(os.getcwd())
# def cat(fp):
#     for i in os.walk(fp):
#         for j in i[-1]:
#             file_path="%s//%s"%(i[0],j)
#             for line in file_path:
#                 if "python" in line:
#                     print(file_path)
#
# this_module=sys.modules[__name__]
# while True:
#     fp=input("please input dir:").strip()
#     choice = input("please input choice:").strip()
#     if not choice:continue
#     if hasattr(this_module,choice):
#         getattr(this_module,choice)(fp)
#         break
#     else:continue
# 2 将三次登陆锁定的作业改为：python login.py -u alex -p 123456 输入的形式（-u,-p是固定的，分别代表用户名和密码）
#在login.py中
# 3
#
# 	层级结构：
#
# 	dir1
# 	---hello.py
#
# 	dir2
# 	---main.py
#
#
# 	其中，hello.py：
#
# 	def add(x,y):
# 	     return x+y
#
#
#
# 	main.py如何能调用到hello.py中的add函数。
#form dair1 import hello
#
# 4 显示当前时间三天后是星期几？
# import time
# t=time.localtime(time.time()+3600*24*3)
# print(t.tm_wday+1) #从0计数