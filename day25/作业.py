#作业一
# name=['alex','wupeiqi','yuanhao']
# new_name=map(lambda na:na+"_sb",name)
# print(list(new_name))

# l=[{'name':'alex'},{'name':'y'}]
# l1=list(map(lambda d:d['name']+'sb',l))
# print(list(map(lambda d:{"name":d['name']+'sb'},l)))
# print(l1)
# l={}
# l["name"]="sb"
# print(l)
# l={'name': 'sb'}
# l['name']=l['name']+'sb'
# print(l)
# print(list((map(lambda d:d['name']+'sb',l))))

# shares={
# 	'IBM':36.6,
# 	'Lenovo':23.2,
# 	'oldboy':21.2,
# 	'ocean':10.2,
# }
# print(list(filter(lambda k:shares[k]>20,shares)))

#作业三
# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# m=map(lambda x:x['shares']*x['price'],portfolio)
# print(list(m))

# from functools import reduce
# print(reduce(lambda x,y:x+y,m))

# i=filter(lambda a:a['price']>100,portfolio)
# # print(list(i))
# for j in i:
#     print(j['name'])

# l1=[i['name'] for i in filter(lambda a:a['price']>100,portfolio)]
# print(l1)







