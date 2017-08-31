# salaries={
#     'egon':3000,
#     'alex':100000000,
#     'wupeiqi':10000,
#     'yuanhao':2000
# }
# def get_value(k):
#     return salaries[k]
# print(max(salaries,key=get_value))
# f=lambda k: salaries[k]
# print(f("egon"))
# print(max(salaries,key=f))
# print(max(salaries,key=lambda k: salaries[k]))
# def get_value(k):
#     return salaries[k]
# print(min(salaries,key=get_value))
# lambda k: salaries[k]
# print(min(salaries,key=lambda k: salaries[k]))
# l1=[1,2,3,4]
# s='hello'
# for i in zip(l1,s):
#     print(i)
# for i in zip(salaries.values(),salaries.keys()):
#     print(i)
# zip=zip(salaries.values(),salaries.keys())
# print(max(zip))
# print(sorted(salaries,key=lambda k:salaries[k]))

#map
# l=[1,2,3,7,5]
# m=map(lambda item:item**2,l)
# print(m)
# for i in m:
#     print(i)
# name_l=['alex','zhejiangF4','yuanhao','wupeiqi']
# m=map(lambda name:name+'SB',name_l)
# for i in m:
#     print(i)
# print(list(m))
#filter
# name_l=[
#     {"name":'egon','age':18},
#     {"name":'alex','age':19},
#     {"name":'aggo','age':20},
#     {"name":'dddd','age':21},
# ]
# f = filter(lambda d:d['age'] > 18,name_l)
# # print(f)
# for i in f:
#     print(i)


# def get_value(k):
#     return salaries[k]
# lambda k:salaries[k]
# print(max(salaries,key=lambda k:salaries[k]))

s='{"a":1,"b":2,"c":3}'
print(eval(s)['a'])



