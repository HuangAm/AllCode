# l=['egg%s'%i for i in range(100) if i > 50]
# print(l)

# egg_list=[]
# for i in range(100):
#     egg_list.append("egg%s"%i)
# print(egg_list)
# import os
# g=os.walk('D:\\agon')
# file_path_list=[]
# for i in g:
#     for j in i [-1]:
#         file_path_list.append('%s\\%s' %(i[0],j))
# print(file_path_list)
#
# g=os.walk('D:\\agon')
# l1=['%s\\%s' %(i[0],j)for i in g for j in i[-1]]
# print(l1)

# egg_list=[]
# for i in range(100):
#     egg_list.append('egg%s'%i)
# print(egg_list)
# l=['egon%s'%i for i in range(100)]
# print(l)
# l=[1,2,3,4]
# s='hello'
# l1=[(num,s1)for num in l if num > 2 for s1 in s]
# print(l1)
# import os
# g=os.walk('D:\\agon')
# file_path_list = []
# for i in g:
#     for j in i[-1]:
#         file_path='%s\\%s' %(i[0],j)
#         file_path_list.append(file_path)
# print(file_path_list)

# l=['%s\\%s'%(i[0],j)for i in g for j in i[-1]]
# print(l)

# print(sum([1,2,3,4]))
# num_g=(i for i in range(3))
# print(sum(num_g))
# print(list(range(1,4)))
# print(list([1,2,3,4]))
# print(list({1,2,3,4}))
# print(list((1,2,3,4)))
# a=[x * x for x in range(1,11)]
# print(a,type(a))
# a=[x * x for x in range(1,11) if x % 2 == 0]
# print(a)
# a=[m + n for m in "ABC" for n in "XYZ"]
# print(a)
# import os
# print([d for d in os.listdir('.')])#os.listdir可以列出文件和目录
# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k,v in d.items():
#     print(k,"=",v)
# s=[k + "=" + v for k,v in d.items()]
# print(s)
# L=['Hello','World','IBM','Apple']
# l=[i.lower() for i in L]
# print(l)















