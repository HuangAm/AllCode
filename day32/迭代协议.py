from collections import Iterable,Iterator
# class Foo:
#     def __init__(self,start):
#         self.start=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start > 10:
#             raise StopIteration
#         n=self.start
#         self.start+=1
#         return n
# f=Foo(0)
# for i in f:
#     print(i)
# class Range:
#     def __init__(self,stop,start=0):
#         self.start=start
#         self.stop=stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start > self.stop-1:
#             raise StopIteration
#         n=self.start
#         self.start+=1
#         return n
# r=Range(10)
# for i in r:
#     print(i)