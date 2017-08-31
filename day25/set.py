# s={1,2,3,4,5,'e','f','a','b'}
# s1={'a','b''c',1,2,3}
# linux=['钢弹','小壁虎','小虎比','alex','wupeiqi','yuanhao']
# python=['dragon','钢弹','zhejiangF4','小虎比']
# s2=set(linux)
# print(s2)
# s3=set(python)
# print(s3)

# print(s2|s3)
# print(s2&s3)
# print(s2-s3)
# print(s3-s2)
# # print(s2^s3)
# print(s.add(66))
# # print(s)
# l=[1,]
# print(l.append(2))
# print(s.clear())

# import os
# def next_free(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
#
# @next_free
# def searcher(target):
#     while True:
#         file_path=yield
#         for i in os.walk(file_path):
#             for j in i[-1]:
#                 file_path=("%s\\%s")%(i[0],j)
#                 target.send(file_path)
# @next_free
# def opener(target):
#     while True:
#         file_path=yield
#         with open(file_path) as f:
#             target.send((file_path,f))
# @next_free
# def greper(word,target):
#     while True:
#         file_path,f=yield
#         for line in f:
#             if word in line:
#                 target.send(file_path)
# @next_free
# def printer():
#     while True:
#         file_path=yield
#         print(file_path)
#
# g=searcher(opener(greper("python",printer())))
# g.send("D:\\agon")

# def add(n,i):
#     return n+i
# def test():
#     for i in range(4):
#         yield i
# g=test()
# for n in [1,10]:
#     g=(add(n,i) for i in g)
# print(list(g))

# l=['adam', 'LISA', 'barT']
# print(list(map(lambda x:x.title(),l)))
# def f(x):
#     return x*x
# r=map(f,[1,2,3,4,5,6,7,8,9])
# print(list(r))
# print(list(map(str,[1,2,3,4,5,6,7,8,9])))

# l=[3,4,1,0,9,10]
# print(sorted(l))#返回值是列表，默认是升序,按ASCII码进行排
# s=sorted(l)
# print(s)
# s.append(4)
# print(s)
# p=s.__iter__()
# print(p)

# print(sorted(l,reverse=True))#降序,由大到小
# s='hello abc'
# print(sorted(s))#[' ', 'a', 'b', 'c', 'e', 'h', 'l', 'l', 'o']
# print(sorted(salaries))
# print(sorted(salaries,key=lambda k: salaries[k]))

# l=[1,2,3,7,5]
# m=map(lambda item:item**2,l)
# print(m)

# map(func, *iterables),map作用就是把一个没有用的可迭代对象加工成需要的可迭代对象，映射的方式
# l=[1,2,3,7,5]
# m=map(lambda item:item**2,l)
# print(m)
# m.n
# class Garen:
#     camp = 'Demacia'
#     def __init__(self,nickname):
#         self.nick=nickname
#     def attack(self,enemy):
#         print('attack %s' %enemy)
# class Garen:
#     camp = 'Decmacia'
#     def attack(self):
#         print('attack')
# print(Garen)
# print(int)
# g1=Garen()
# print(g1)
# g1.attack()
# print(g1.attack())


# class Garen:
#     camp = 'Decmacia'
#
#     def attack(self):
#         pass

                # class Garen:
#     camp = 'Demacia'
#     def __inter__(self):
#         pass
#     def q(self):
#         pass
#     def w(self):
#         pass
#     def e(self):
#         pass
# import os
# def next_free(func):
#     def wrapper(*args,**kwargs):
#         res=func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
#
# @next_free
# def search(target):
#     while True:
#         file_path = yield
#         for i in os.walk(file_path):
#             for j in i[-1]:
#                 file_path = ("%s\\%s") %(i[0],j)
#                 target.send(file_path)
# @next_free
# def opener(target):
#     while True:
#         file_path = yield
#         with open(file_path) as f:
#             target.send((file_path,f))
# @next_free
# def greper(word,target):
#     while True:
#         file_path,f = yield
#         for line in f :
#             if word in line:
#                 target.send(file_path)
#
# @next_free
# def printer():
#     while True:
#         file_path=yield
#         print(file_path)
# g=search(opener(greper('python',printer())))
# g.send("D:\\agon")
# d = dict(name='egon')
# print(d)
# print(d.pop('name'))
# print(d)
# class Garen:
#     pass
# g1=Garen()
# print(g1)
# print(g1.__class__)
# print(g1.__dict__)
# print(g1.__module__)

# __author__ = 'linhaifeng'
import time
# person_list = ['alex','wupeiqi','yuanhao','linhaifeng']
# def ask_way(person_list):
#     print('-'*60)
#     if len(person_list) == 0:
#         return '没人知道'
#     person = person_list.pop(0)
#     if person == 'linhaifeng':
#         return '%s 说：我知道，老男孩就在汇德商厦，下地铁就是'%person
#     print('hi 美男%s,敢问路在何方'%person)#'yuanhao'
#     print('%s回答道：我不知道，但你慧眼识珠，你等着，我帮你问问%s.....'%(person,person_list))#'yuanhao'
#     time.sleep(3)
#     res = ask_way(person_list)
#     print('%s问的结果是：%res' %(person,res))
#     return res#ask_way(person_list)
# res = ask_way(person_list)
# print(res)
# import time
# def fact(n):
#     print(n)
#     if n == 1:
#         return 111
#     n=n-1
#     res = fact(n)
#     print(n,res)
#     time.sleep(3)
#     return res
# print(fact(5))
