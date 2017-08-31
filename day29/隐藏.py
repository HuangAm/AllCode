# class A:
#     __N=0 #类的数据属性就应该是共享的，但是语法上是可以把类的数据属性设置成私有的如__N,会变形成_A__N
#     def __init__(self):
#         self.__X=10 #变形为self._A__X
#     def __foo(self):#变形为_A__foo
#         print("from A")
#     def bar(self):
#         self.__foo()#只有在类内部才可以通过__foo的形式访问到
#
# a = A()
# # print(a.__dict__)#{'_A__X': 10}
# # print(A.__dict__)#可以查看属性名有没有被改为_*__*的形式
# print(a._A__N)
# print(a._A__X)
# a._A__foo()
# a.bar()


# #正常情况
# class A:
#     def fa(self):
#         print("from A")
#     def test(self):
#         self.fa()#b.fa
# class B(A):
#     def fa(self):
#         print("from B")
# b = B()
# b.test()#from B
#
#把fa定义成私有的，即__fa
# class A:
#     def __fa(self): #_A__fa
#         print("from A")
#     def test(self):
#         self.__fa() #_A__fa
# class B(A):
#     def __fa(self):
#         print("from B")
# b = B()
# print(b.__dict__)
# print(b._B__fa())
# b.test()#from A