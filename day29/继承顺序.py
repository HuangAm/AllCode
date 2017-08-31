# class A(object):
#     def test(self):
#         print('from A')
# class B(A):
#     def test(self):
#         print("from B")
# class C(A):
#     def test(self):
#         print("from C")
# class D(B):
#     def test(self):
#         print("from D")
# class E(C):
#     def test(self):
#         print("from E")
# class F(D,E):
#     def test(self):
#         print("from F")
#     pass
#
# f1=F()
# f1.test()
# print()

# class People:
#     def __init__(self,name,sex,age):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def walk(self):
#         print('%s is walking'%self.name)
# class Chinese(People):
#     country = "China"
#     def __init__(self,name,sex,age,language="Chinese"):
#         super().__init__(name,sex,age)
#         self.language = language
#     def walk(self,x):
#         super().walk()
#         print('子类的X',x)
# c=Chinese('egon','male',18)
# c.walk(123)

# class A:
#     __x=1
#     def __test(self):
#         print("from A")
# print(A.__x)
# print(A._A__x)
# a = A()
# print(a._A__x)
# A.__y=2
# print(A.__y)
# a.__z=3
# print(a.__z)
# class A(object):
#     def test(self):
#         print("from A")
# class B(A):
#     def test(self):
#         print("from B")
# class C(A):
#     def test(self):
#         print("from C")
# class D(B):
#     def test(self):
#         print("from D")
# class E(C):
#     def test(self):
#         print("from E")
# class F(D,E):
#     def test(self):
#         print("from F")
# f1 = F()
# f1.test()
# print(F.__mro__)#__mro__可以查看所有的线性元组，经典类没有这个属性，只有新式类有
#新式类继承顺序：F-->D-->B-->E-->A-->object
#经典类继承顺序：F-->D-->B-->A-->E-->C
#Python3中统一都是新式类




























