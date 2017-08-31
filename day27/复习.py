# import getpass
# username = input('alex')
# password = input('alex123')
# if username == 'alex' and password == 'alex123':
#     print('Welcome dear alex!')

# age = 56
# user_guess = int(input('please input your guess:'))
# if user_guess < age:
#     print("try smaller...")
# elif user_guess > age:
#     print("try bigger...")
# else:
#     print("you got it!")

# score = int(input("please input score:"))
# if score >= 90 and score <= 100:
#     print("A")
#     choice = input("什么奖励想要：")
#     if choice == "大保健":
#         print("qinzhengzhuanshu")
# elif score >= 80:
#     print("B-")
# elif score >= 60:
#     print("C")
# else:
#     print("D")

# for i in range(10):
#     if i > 5:
#         print(i)
#     else:
#         print("------")
#         continue

# for i in range(10):
#     print("i",i)
#     if i > 5:
#         for j in range(10):
#             if j == 3:
#                 break
#             print("--j",j)

# break_flag = False
# for i in range(10):
#     print("第一层",i)
#     for j in range(10):
#         print("第二层",j)
#         if j == 3:
#             break_flag = True
#             break
#         for k in range(10):
#             print("第三层",k)
#             if k == 2:
#                 break_flag = True
#                 break
#         if break_flag:
#             print("第三层没了，第二层也不行了")
#             break
#     if break_flag:
#         print("第二层没了，第一层也不行了...")
#         break
# else:
#     print("keep going")

# break_flag = False
# for i in range(10):
#     print("第一层",i)
#     for j in range(10):
#         print("第二层",j)
#         for k in range(10):
#             print("第三层",k)
#             if k == 3:
#                 break_flag = True
#                 break
#         if break_flag:
#              print("第二层也跳")
#              break
#     if break_flag:
#         print("第一层也跳")
#         break

# break_flag = False
# count = 0
# while break_flag == False:
#     print("aaa")
#     while break_flag == False:
#         print("bbb")
#         while break_flag == False:
#             print("ccc")
#             break_flag = True
# name = "suhaozhi,qinzhen,lizhi"
# print(name.index("h"))
# print(name[0:8])
# print(name[:8])
# print(name[9:16])
# print("--->",name[9:])
# print(name[-6:])
# print(name[-5:])
# print(name[-1])
# name = "\n\t  Alex  ;  li  \t"
# print(name)
# print(name.strip())
# name = name.strip()
# print(name.split())
# print(name.split(";"))
# print(len(name))
# name1 = "suhaozhi,qinzhen,lizhi"
# print(name1[9:16])
# print(name1[-6:-1])
# print(name1[0::2])
# print(name1.split(","))
# name2="suhaozhi"
# print(name2.split())
# name = {"agin":31,"alex":33,"rain":22}
# print(name["agin"])
# print(name.get("USE",False))
# s="hello"+"world"+"i"+"am"+"python"
# print(s)
# print("--".join("hello"))
# print("-".join("hello"))
# print(name2.capitalize())
# print(name2.title())
# print(name1.index("i",5))
# print(name1.replace("suhaozhi","yuanshuai"))
# print(name1)
# print(name1.find("i"))
# print(name1.index("x"))
# print("hello world".center(50,"*"))
# print("hello world".ljust(50,"*"))
# print("hello %s"%"sb")
# print("hello %.4f"%100000)
# print("hello{0},his age is {1}".format("alex",34))
# print("hello{name},his age is {age}".format(name="alex",age=34))
# print("hello world".capitalize())
# print("HellO".casefold())
# print("HHHHH".lower())
# l=[1,"hello",[4,5],{"name":"egon"}]
# print(l[0])
# print(l.index("hello"))
# l.insert(1,"kk")
# print(l)
# print(l.remove("kk"))
# print(l)
# l[0]=2
# print(l)
# l.clear()
# print(l)
# l.sort()
# l=[1,2,3]
# print(l.append(4))
# s1={"hello",1,2,3}
# s2={1,2,("a","b")}
# print(s1.union(s2))
# print(s1|s2)
# print(s1.intersection(s2))
# print(s1&s2)
# print(s1.difference(s2))
# print(s1-s2)
# print(s2-s1)
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))
# print(s1^s2)
# t=("a",1,"b",2)
# print(t[0])
# print(t[:3])
# names_class1=['张三','李四','王五','赵六',[1,2,3]]
# names_class1_copy=names_class1.copy()

# names_class1[0]="zhangsan"
# print(names_class1)
# print(names_class1_copy)

# names_class1[4][2]=5
# print(names_class1)
# print(names_class1_copy)

def int2(x,base=2):
    return int(x,base)
# print(int2('10'))
print(int2('10'))












