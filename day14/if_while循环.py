# for i in range(10):
#     if i > 5:
#         print (i)
#     else:
#         continue#跳出本次循环
#         print("-----")
# for i in range(10):
#     print("i",i)
#     if i > 5:
#         for j in range (10):
#             if j == 3:
#                 break
#             print("--j",j)


# for i in range(10):
#     print(i)
#     if i == 5:
#         break
# else:#当循环正常结束时，走else
#     print("done")
# print("done2")



# break_flag = False
# for i in range(10):
#     print("第一层",i)
#     for j in range(10):
#         print("第二层",j)
#         if j == 3:
#             break_flag = True
#             break
#         for k in range(10):
#             print ("第三层",k)
#             if k == 2:
#                 break_flag = True
#                 break
#         if break_flag:
#             break
#     if break_flag:
#         print("第三层么了，第二层也不行了...")
#         break
# else:
#     print("keep going")

# break_flag = False
# count = 0
# while break_flag == False:
#     print("aaa")
#     while break_flag == False:
#         print("bbb")
#         while break_flag == False:
#             count += 1
#             if count < 10:
#                 print("ccc")
#                 break_flag == True








