###while循环99乘法表

# i = 0
# j=0
# while i<9:
#     i+=1
#     while j<9:
#         j+=1
#         print(j,"x",i,"=",j*i,"\t",end="")
#         if i == j:
#             j=0
#             print("")
#             break

###for循环99乘法表

for i in range(1,10):
    for j in range(1,10):
        print(j,"x",i,"=",j*i,"\t",end="")
        if i==j:
            print("")
            break

# while True:
#     score = input("please input your score:")#输入分数
#     if score.isdigit():
#         score=int(score)
#         if score==100:
#             print("very good!")
#         elif score>=90 and score<100:
#             print("优")
#         elif score>=80 and score<90:
#             print("中")
#         elif score>=70 and score<80:
#             print("良")
#         elif score>=60 and score<70:
#             print("及格")
#         elif score>=0 and score<60:
#             print("不及格")
#         else:
#             print("异常")
#             continue
#     else:
#         print("please input digit")
#         continue



# for i in range(1,5):
#     for j in range(1,5):
#         if j != i:
#             for k in range(1,5):
#                 if k!=i and k!=j:
#                     print(i,j,k,"\t",end="")
#     print("")

# def add():
#     print("add")
# def delete():
#     print("delete")
# def change():
#     print("change")
# def search():
#     print("search")
# def menu():
#     menu="""
#     add:增加
#     delete:删除
#     change:修改
#     search:查找
#     """
#     print(menu)
# menu_dict={
#     "add":add,
#     "delete":delete,
#     "change":change,
#     "search":search
# }
#
# menu()
# choice=input("please input your choice:").strip()
# if choice in menu_dict:
#     menu_dict[choice]()



















