#作业一
# linux=['钢弹','小壁虎','小虎比','alex','wupeiqi','yuanhao']
# python=['dragon','钢弹','zhejiangF4','小虎比']
# l=[]
# for i in linux:
#     for j in python:
#         if i==j:
#             l.append(i)
# print(l)

# l1=[i for i in linux for j in python if i==j]
# print(l1)

# l2=[]
# for i in linux:
#     if i not in python:
#         l2.append(i)
# print(l2)

# l2=[i for i in linux if i not in python]
# print(l2)

# l3=[]
# for j in python:
#     if j not in linux:
#         l3.append(j)
# print(l3)

# l3=[j for j in python if j not in linux]
# print(l3)

#作业二
# shares={
# 	'IBM':36.6,
# 	'lenovo':27.3,
# 	'huawei':40.3,
# 	'oldboy':3.2,
# 	'ocean':20.1
# 	}

# l3=[]
# for i in shares:
#     if float(shares[i]) > 30:
#         l3.append(i)
# print(l3)

# l3=[i for i in shares if float(shares[i]) > 30]
# print(l3)

# all_price=0
# for i in shares:
#     all_price +=float(shares[i])
# print(all_price)

# all_price=sum(float(shares[i]) for i in shares)
# print(all_price)

#作业三
# l=[10,2,3,4,5,6,7]

# l1=[]
# for i in l:
#     square=float(i)*float(i)
#     l1.append(square)
#     sumer=0
#     for j in l1:
#         if float(j) > 40 :
#             sumer += float(j)
# print(sumer)

# l1=[float(i)*float(i) for i in l ]
# print(l1)
# res=sum(j for j in l1 if j > 40)
# print(res)

# res=sum(float(i)*float(i) for i in l if float(i)*float(i) > 40)
# print(res)






















