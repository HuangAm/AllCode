'''
今日重点：
	isinstance，issubclass
	反射：getattr,setattr,delattr,hasattr
	内置attr：__getattr__,__setattr__,__delattr__(很明显，都是对属性的操作，比上面多了触发)

	定制自己的数据类型：
		1.继承的方式（包装）
		2.授权的方式（包装的一种形式）



作业：
	基于授权定制自己的列表类型，要求定制的自己的__init__方法，
	定制自己的append：只能向列表加入字符串类型的值
	定制显示列表中间那个值的属性（提示：property）
	其余方法都使用list默认的（提示：__getattr__加反射）
'''
# class List:
#     def __init__(self,x):
#         self.x=eval(x)#eval(x)必须是一个列表
#     def append(self, p_object):
#         if not isinstance(p_object,str):
#             raise TypeError ("must be str")
#         self.x.append(p_object)
#     def __getattr__(self, item):
#         return getattr(self.x,item)
#     @property
#     def mid(self):
#         index=len(self.x)//2
#         print(self.x[index])
#     def __str__(self):
#         return str(self.x)
# l=List("[]")
# l.append("hello")
# print(l)
# l.mid










