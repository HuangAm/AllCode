

#Python3----------
# print("�й�")










# name = "�й�"
# print (name)
# print [name.decode("utf-8")]
# print name.d.ecode("utf-8")
# print (name.decode("utf-8").encode("GBK"))
# gbk = name.decode("utf-8").encode("GBK")
# print gbk.decode("GBK").encode("gb2312")

# n="���к�"
# # print(n.encode("utf-8"))
# # print(n)
# print(n.encode("gbk"))
# m=n.encode("gbk")
# print(m.decode("gbk"))
# b'\xc0\xcf\xc4\xd0\xba\xa2'
# ���к�
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
#         {"name":  "����",  "price":  1999},
#         {"name":  "���",  "price":  10},
#         {"name":  "��ͧ",  "price":  20},
#         {"name":  "��Ů",  "price":  998},
#     ]
# shopping_car={}
# total_amount=int(input("�����������ܽ��: "))
# while True:
#     for index,product in enumerate(goods,1):
#         print(index,goods[index-1]["name"])
#     choice=int(input("��������ѡ�����Ʒ�����кţ�"))
#     if choice>0 and choice<=len(goods):
#         if int(goods[choice-1]["price"])<=total_amount:
#             balance=total_amount-int(goods[choice-1]["price"])
#             print("����ɹ�",goods[choice]["name"],"�ѳɹ����빺�ﳵ")
#         else:
#             print("�˻�����")
#     else:
#         continue
#     if choice =="q":
#         break
f=open("D:\\����.txt",encoding="utf8")
print(f.read())