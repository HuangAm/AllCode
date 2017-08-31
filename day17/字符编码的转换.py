

#Python3----------
# print("中国")










# name = "中国"
# print (name)
# print [name.decode("utf-8")]
# print name.d.ecode("utf-8")
# print (name.decode("utf-8").encode("GBK"))
# gbk = name.decode("utf-8").encode("GBK")
# print gbk.decode("GBK").encode("gb2312")

# n="老男孩"
# # print(n.encode("utf-8"))
# # print(n)
# print(n.encode("gbk"))
# m=n.encode("gbk")
# print(m.decode("gbk"))
# b'\xc0\xcf\xc4\xd0\xba\xa2'
# 老男孩
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print(sum)
# a={11,22,33,44,55,66,77,88,99,90}
# b={"k1":[],"k2":[]}
# for i in a:
#     if i > 66:
#         b["k1"].append(i)
#     elif i< 66:
#         b["k2"].append(i)
# print(b)
# {'k2': [33, 11, 44, 22, 55], 'k1': [99, 77, 88, 90]}
# goods  =  [
#         {"name":  "电脑",  "price":  1999},
#         {"name":  "鼠标",  "price":  10},
#         {"name":  "游艇",  "price":  20},
#         {"name":  "美女",  "price":  998},
#     ]
# shopping_car={}
# total_amount=int(input("请输入您的总金额: "))
# while True:
#     for index,product in enumerate(goods,1):
#         print(index,goods[index-1]["name"])
#     choice=int(input("请输入您选择的商品的序列号："))
#     if choice>0 and choice<=len(goods):
#         if int(goods[choice-1]["price"])<=total_amount:
#             balance=total_amount-int(goods[choice-1]["price"])
#             print("购买成功",goods[choice]["name"],"已成功加入购物车")
#         else:
#             print("账户余额不足")
#     else:
#         continue
#     if choice =="q":
#         break
f=open("D:\\问题.txt",encoding="utf8")
print(f.read())