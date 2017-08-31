#抱着抱着抱着我的小鲤鱼的我的我的我
# def foo(x):
#     if x == 0:
#         print('我的小鲤鱼',end='')
#         return
#     else:
#         print('抱着',end='')
#         foo(x-1)
#         print('的我',end='')
# foo(3)


#时间复杂度
# print('Hello World')        #O(1)

# for i in range(n):          #O(n)
#     print('Hello World')

# for i in range(n):          #O(n^2)
#     for j in range(n):
#         print('Hello World')

# for i in range(n):          #O(n^3)
#     for j in range(n):
#         for k in range(n):
#             print('Hello World')

# while n>1:                  #O(logn)
#     print(n)
#     n = n//2

"""***********************************"""

"""
时间复杂度 O
时间复杂度是用来估计算法运行时间的一个式子(单位)。
一般来说，时间复杂度高的算法比复杂度低的算法慢
常见的时间复杂度(按效率排序)
    O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^2logn)<O(n3)
不常见的时间复杂度
    O(n!) O(2^n) O(n^n) ...

如何一眼判断时间复杂度？(一般情况下)
    循环减半的过程→O(logn)
    几次循环就是n的几次方的复杂度
"""

"""
空间复杂度 S(n)=>space
空间复杂度：用来评估算法内存占用大小的一个式子
几个变量O(1)
一维数组或列表是O(n)
二维数组或列表是O(n^2)
三维数组或列表是O(n^3)
空间换时间
"""

"""
列表查找
列表查找：从列表中查找指定元素
    输入：列表、待查找元素
    输出：元素下标或未查找到元素
顺序查找：
    从列表第一个元素开始，顺序进行搜索，直到找到为止
二分查找：(有序)
    从有序列表的候选区data[0:n]开始，通过对待查找的值与候选
    区中间值的比较，可以是候选区减少一半。
"""

#函数的渐进界

# import random
# n = 10000
# li = list(range(n))
# random.shuffle(li)
# print(li)

#二分不递归版
# def bin_search(li,val): #li是列表，val是要找的值的索引
#     low = 0
#     high = len(li)-1
#     while low <= high: #循环比递归效率高
#         mid = (low+high)//2  #O(logn)
#         if li[mid] == val:
#             return mid
#         elif li[mid]<val:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None

#二分递归版
# def bin_search_rec(data_set,value,low,high):
#     if low <= high:
#         mid = (low + high) // 2
#         if data_set[mid] == value:
#             return mid
#         elif data_set[mid] > value:
#             return bin_search_rec(data_set,value,low,mid-1)
#         else:
#             return bin_search_rec(data_set,value,mid+1,high)
#     else:
#         return

#列表查找练习
"""
现有一个学员信息列表（按id增序排列），格式为：
[
{id:1001, name:"张三", age:20},
{id:1002, name:"李四", age:25},
{id:1004, name:"王五", age:23},
{id:1007, name:"赵六", age:33}
]
要求：修改二分查找代码，输入学生id，输出该学生在列表中的下标，
并输出完整学生信息。
"""
l = [
    {'id': 1001, 'name': "张三", 'age': 20},
    {'id': 1002, 'name': "李四", 'age': 25},
    {'id': 1004, 'name': "王五", 'age': 23},
    {'id': 1007, 'name': "赵六", 'age': 33}
]
def searchInfo(li,id):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (low + high) // 2
        if li[mid]["id"] == id:
            return li[mid]
        elif li[mid]["id"] <= id:
            low = mid + 1
        else:
            high = mid -1
    return "not have"

print(searchInfo(l,1002))
# def bin_search(li,val): #li是列表，val是要找的值的索引
#     low = 0
#     high = len(li)-1
#     while low <= high: #循环比递归效率高
#         mid = (low+high)//2  #O(logn)
#         if li[mid] == val:
#             return mid
#         elif li[mid]<val:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None





