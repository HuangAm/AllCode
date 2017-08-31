# f = open("test1",encoding="utf-8") #打开文件
# data = f.read()#获取文件内容
# print(data)
# data = f.readlines()
# print(data)
# f.close()#关闭文件
# print(f.read())
#
# count = 0
# for line in f.readlines():
#     if count == 3:
#         line="".join([line.strip(),"岳飞"])
#     print(line.strip())
#     count+=1
# count=0
# for line in f:
#     if count == 2 :
#         line = "".join([line.strip(),"sdf"])
#     print(line.strip())
#     count+=1
#w，覆盖加
# f = open("test",mode="w",encoding="utf-8") #打开文件
# f.write("hello")#覆盖写，把原来的东西覆盖掉
# f.write("hello\nworld")#在文件没有关闭之前，可以可以继续追加
#a，追加
# f = open("test",mode="w",encoding="utf-8")
# f.write("hello")#追加写，在原来的东西后面写
#r+
# f=open("test3,"r+",encoding="utf-8")
# print(f.read())
# f.write("where is xialv?")#一定是追加写
# #w+
# f=open("test","w+",encoding="utf-8")
# print(f.read())#什么都读不到，因为首先会覆盖，读的时候一定要记住光标的位置
# f.write("where is xialv?")
# f.seek(0)#将光标移到开始位置，参数是按字节，字节，字节,read的参数是字符
# print(f.read())
# print(f.tell())#tell是用来查看当前光标的位置，seek是用来调光标位置的，tell参数也是字节
# #a+
# f=open("test","a+",encoding="utf-8")
# print(f.read())#读不到，他一开始光标就默认在最后
# f.write("where is xialv?")#a+默认追加到最后
# f=open("test","rb")
# print(f.read())
# f=open("text","w")
# f.write("11111111111\n")
# f.write("11111111111\n")

# m='{"backend":"www.oldboy20.org","record":{"server":"1111","weight":"2222","maxconn":"3333"}}'
# m=input("please input something:").strip()
# m = eval(m)
# l=[]
# for i in m:
#     print(i)
# m=input("please input something:").strip()
# m = eval(m)
# flag=False#标志位
# l_add=["\t\t""server",m["record"]["server"],"weight",m["record"]["weight"],"maxconn",m["record"]["maxconn"]]
# with open("haproxy.conf",encoding="utf-8")as f_read,open("test_add","r+",encoding="utf-8")as f_write:
#     for line in f_read:
#         if line.startswith("backend")and m["backend"] in line: #第一步，进行信息匹配
#             flag=True
#         f_write.write(line)
#         if 'server'in line and flag:
#             for i in l_add:
#                 f_write.write(i+" ")

# m=input("please input url:").strip()
# m = eval(m)
# flag=False#标志位
# with open("test_add",encoding="utf-8")as f_read,open("test_delete","w+",encoding="utf-8")as f_write:
#     for line in f_read:
#         if m["record"]["server"] in line and m["record"]["weight"]:
#             continue
#         f_write.write(line)
# m='{"backend":"www.oldboy20.org","record":{"server":"1111","weight":"2222","maxconn":"3333"}}'
# s='{"backend":"www.oldboy2.org","record":{"server":"0000","weight":"0000","maxconn":"0000"}}'
# m=input("please input something:").strip()#{"backend":"www.oldboy2.org","record":{"server":"0000","weight":"0000","maxconn":"0000"}}
# m = eval(m)
# flag=False#标志位
# l_add=["\t\t""server",m["record"]["server"],"weight",m["record"]["weight"],"maxconn",m["record"]["maxconn"],"\n"]
# with open("haproxy.conf",encoding="utf-8")as f_read,open("test_change","w+",encoding="utf-8")as f_write:
#     for line in f_read:
#         if line.startswith("backend") and m["backend"] in line:  # 第一步，进行信息匹配
#             flag = True
#         f_write.write(line)
#         if 'server' in line and flag:
#             for i in l_add:
#                 f_write.write(i + " ")
#             flag = False
#             continue
# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)
# print(fact(5)
# with open("text","rb")as f:
#     # f.seek(2,2)
#     print(f.read())
#     f.seek(2)
#     print(f.read())
#     print(f.tell())
#     f.seek(-3,2)
#     print(f.tell())
#     print(f.read())



















