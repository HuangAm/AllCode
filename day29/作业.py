# #coding:utf8
# class B(object):
#     # def test(self):
#     #     print("from B")
#     pass
# class C(object):
#     # def test(self):
#     #     print("from C")
#     pass
# class D(B,C):
#     # def test(self):
#     #     print("from D")
#     pass
# class E(B,C):
#     # def test(self):
#     #     print("from E")
#     pass
# class F(D,E):
#     # def test(self):
#     #     print("from F")
#     pass
#
#
# f=F()
# f.test()
#经典类：F-->D-->B-->C-->E
#新式类：F-->D-->E-->B-->C-->object

class file_all:
    def read(self):
        print("file_all is read")
    def write(self):
        print("file_all is write")

