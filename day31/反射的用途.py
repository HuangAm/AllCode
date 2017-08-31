#之前我们学的是判断字典里有没有key，有的话字典["key"]去运行
# def add():
#     print("add")
# def change():
#     print("change")
# def search():
#     print("search")
# def delete():
#     print("delete")
# func_dic={
#     "add":add,
#     "change":change,
#     "search":search,
#     "delete":delete
# }
# while True:
#     cmd=input(">>: ").strip()
#     if not cmd:continue
#     if cmd in func_dic: #hasattr()
#         func=func_dic.get(cmd)  #func=getattr()
#         func()

#######################################################################################################################

#学完面向对象后，可以通过反射搞
#思想是：借用sys，导入当前模块判断输入的字符串在不在模块中(hasattr)，在的话执行(getattr获取后运行)
# import sys
# def add():
#     print("add")
# def change():
#     print("change")
# def search():
#     print("search")
# def delete():
#     print("delete")
# this_moudle=sys.modules[__name__]#导入当前模块
# while True:
#     cmd=input(">>: ").strip()
#     if not cmd:continue
#     if hasattr(this_moudle,cmd): #判断有没有cmd
#         func=getattr(this_moudle,cmd) #获取属性
#         func() #运行属性