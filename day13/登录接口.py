# import getpass
# username =  input("alex")
# password = input ("alex123")
# if username == "alex" and password == "alex123"
#     print("Welcome dear alex!")
# n=1

# s='This is is a string.\
# This continues the string.'
# print (s)

# s = "k:1|k1:2|k2:3|k3:4"
# s1 = s.split('|')
# d={}
# for i in s1:
#     l = i.split(':')
#     d.setdefault(l[0],l[1])
# print(d)

# li = "k:1|k1:2|k2:3|k3:4"
# import re
# print({i[0]:i[1] for i in re.findall(r"(\w+):(\w+)",li)})

# s = "k:1|k1:2|k2:3|k3:4"
# dic = {x.split(':')[0]: int(x.split(':')[1]) for x in [item for item in s.split('|')]}
# print(dic)

# class LiuGeng:
#     def __init__(self,name):
#         self.name = name
#     def __call__(self, *args, **kwargs):
#         print('刘庚是帅哥')
#         return self.name
# a=LiuGeng('LLL')
# print(a)
# a()
# print(a())