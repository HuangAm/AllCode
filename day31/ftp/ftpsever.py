#不影响lili代码的编写
# import ftpclient
# f1 = ftpclient.FtpClient("192.168.1.1")
# if hasattr(f1,"get"):
#     func_get=getattr(f1,"get")
#     func_get()
# print("不存在此方法")
# print("处理其他逻辑")
# 反射实现可插拔机制


# import sys
# def add():
#     print("add")
# def change():
#     print("change")
# def search():
#     print("search")
# def delete():
#     print("delete")
# this_module=sys.modules[__name__]
# while True:
#     cmd=input(">>: ").strip()
#     if not cmd:continue
#     if hasattr(this_module,cmd):
#         func=getattr(this_module,cmd)
#         func()
