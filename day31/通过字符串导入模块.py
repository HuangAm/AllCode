#通过字符串导入模块
#把字符串变为模块名也算映射
#之前学的
# m=input("请输入您要导入的模块：")#输入time
# m1=__import__(m)
# print(m1)#<module 'time' (built-in)>
# print(m1.time())

#官方推荐的字符串作为模块的导入方法
# import importlib
# m=input("请输入您要导入的模块：")#输入time
# t=importlib.import_module(m) #这里可以用到反射
# print(t)#<module 'time' (built-in)>
# print(t.time())
#------------------------------------------------------------------------------------
# __import__("import_lib.metaclass") #这是解释器自己内部用的
# importlib.import_module("import_lib.metaclass")#与上面这句效果一样，官方建议用这个