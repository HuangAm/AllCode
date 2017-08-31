# def age(n):
#     if n == 1:
#         return 10
#     else:
#         return age(n-1)+2
#
# print(age(5))
#
# def x(n):
#     if n == 1:
#         return 1
#     else:
#         return n*x(n-1)
#
# print(x(5))
# data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
#
# def search(num,data):
#     print(data)
#     x = int(len(data) // 2)
#     n=data[x]
#     if num > n:
#         data=data[x:]
#         search(num,data)
#     elif num < n:
#         data = data[:x]
#         return search(num, data)
#     else:
#         print('find')
#         return 1111

# search(9,data)
# print(search(9,data))

# def search(num,data):
#     print(data)
#     if len(data) > 1:
#         mid_index=int(len(data)/2)
#         mid_value=data[mid_index]
#         if num > mid_value:
#             data = data[mid_index:]
#             search(num,data)
#         elif num < mid_value:
#             data = data[:mid_index]
#             search(num,data)
#         else :
#             print('find it')
#             return
#     else:
#         if data[0] == num:
#             print('find it')
#         else:
#             print('not find')
#
# data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
# def search(num,data):
#     print(data)
#     if len(data) > 1:
#         mid_index=int(len(data)/2)
#         mid_value=data[mid_index]
#         if num > mid_value:
#             data = data[mid_index:]
#             return search(num,data)
#         elif num < mid_value:
#             data = data[:mid_index]
#             return search(num,data)#这里的return是下一个search函数的return值
#         else:
#             print('find it')
#             return 666   #要想这个地方的return的值能有每个函数上面所有的search前面都要加return因为，这是一个递归函数，
#     else:
#         if data[0] == num:
#             print('find it')
#             return 777
#         else:
#             print('not found')
#             return 888
# search(19,data)
# print(search(19,data))
#利用递归函数移动汉诺塔：
# def move(n,a,b,c):
#     if n == 1:
#         print('move',a,"--->",c)
#         return
#     move(n-1,a,c,b)#'A','B',
#     print('move',a,'--->',c)
#     move(n-1,b,a,c)
# move(3,'A','B','C')



