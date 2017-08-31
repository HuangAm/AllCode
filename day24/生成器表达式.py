# l=['egg%s'%i for i in range(100)]
# print(l)

# g=('egg%s'%i for i in range(100))
# print(g)
# print(next(g))
# print(next(g))

# f=open("a.txt")
# l=[]
# for line in f:
#     line=line.strip()
#     l.append(line.strip())
# print(l)
# l=[line.strip() for line in f]
# g=(line.strip() for line in f)

#声明式表达式应用实例
# a.txt内容如下：
# apple 10 3
# tesla 1000000 1
# mac 3000 2
# chicken 10 3


# money_l=[]
# with open("a.txt") as f:
#     for line in f:
#         goods = line.split()
#         res = float(goods[-1])*float(goods[-2])
#         money_l.append(res)
# print(money_l)

# f=open('a.txt')
# g=(float(line.split()[-1])*float(line.split()[-2]) for line in f)
# print(sum(g))

# res=[]
# with open("a.txt") as f:
#     for line in f :
#         l=line.split()
#         d={}
#         d["name"]=l[0]
#         d["price"]=l[1]
#         d["count"]=l[2]
#         res.append(d)
# print(res)

# with open('a.txt') as f:
#     res = (line.split() for line in f)
#     print(res)
#     dic_g=({'name':i[0],'price':i[1],'count':i[2]} for i in res)
#     print(dic_g)
#     # print(next(dic_g))
#     apple_dict=next(dic_g)
#     print(apple_dict['count'])












