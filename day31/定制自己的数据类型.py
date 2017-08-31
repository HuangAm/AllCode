#基于继承的原理来定制自己的数据类型
#比如我要新建一个数据类型他的append方法只能增加int数据
# class List(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
#     def append(self, p_object):
#         ' 派生自己的append：加上类型检查'
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         super().append(p_object)
#     def insert(self, index, p_object):
#         ' 派生自己的insert：加上类型检查'
#         if not isinstance(p_object,int):
#             raise TypeError("must be int")
#         super().insert(index,p_object)
#     @property
#     def mid(self):
#         '新增自己的属性'
#         index=len(self)//2
#         return self[index] #查看列表中间的值
#
# l=List([1,2,3,4])
# print(l)
# l.append(5)
# print(l)
# # l.append('1111111') #报错，必须为int类型
# print(l.mid)
# #其余的方法都继承list的
# l.clear()
# print(l)

#授权实现定制自己的数据类型
#碰见像文件句柄这种不能用继承的,需要改写的自定制，需要使用默认的用getattr
# import time
# class Open:
#     def __init__(self,filepath,mode="r",encoding="utf8"):
#         self.filepath=filepath
#         self.mode=mode
#         self.encoding=encoding
#         self.x=open(filepath,mode=mode,encoding=encoding)
#     def write(self,line): #需要改写的自定制
#         t=time.strftime("%Y-%m-%d %X")
#         self.x.write("%s %s"%(t,line))
#     def __getattr__(self, item): #需要使用默认的用getattr
#         if hasattr(self.x,item):
#             return getattr(self.x,item)
#
# f=Open("b.txt","w+") #现在的f只是self
# print(f)
# f.write("11111111\n")
# f.write("11111111\n")
# f.write("11111111\n")
# f.write("11111111\n")
# f.write("11111111\n")
# f.seek(0)
# res = f.read()
# print(res)
# f.seek(0)
# print(f.read())
# f.flush()
# f.close()

# import time
# class FileHandle:
#     def __init__(self,filename,mode="r",encoding="utf8"):
#         if "b" in mode:
#             self.file=open(filename,mode)
#         else:
#             self.file=open(filename,mode=mode,encoding=encoding)
#         self.filename=filename
#         self.mode=mode
#         self.encoding=encoding
#     def write(self,line):
#         if "b" in self.mode:
#             if not isinstance(line,bytes):
#                 raise TypeError("must be bytes")
#         self.file.write(line)
#     def __getattr__(self, item):
#         return getattr(self.file,item)
#     def __str__(self):
#         if "b" in self.mode:
#             res="<_io.BufferedReader name='%s'>" %self.filename
#             return res
#         else:
#             res = "<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" % (self.filename, self.mode, self.encoding)
#             return res
# f1=FileHandle("b.txt","wb")
# # f1.write("你好啊啊啊")#自定制的write,不用再进行encode转成二进制去写了，简单大气
# f1.write("你好啊".encode("utf-8"))
# print(f1)
# f1.close()