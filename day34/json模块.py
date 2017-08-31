#只要符合json规则的字符串就是json字符串，不一定非要json.dumps后才是json字符串
#json处理的是json字符串，如果字符串是json里面有的可以直接拿来处理，如果没有需要先dumps一下转为json字符串，在loads出来操作
#json.dumps和json.loads是结合起来用的，而json.dump(d,f)完成了两步:dumps和f.write()
#json.dumps 转储成json字符串,也叫序列化
#json.loads 装载json字符串,也叫反序列化
#json.dump 往文件中倾倒json字符串
import json
#当json碰见中文
#d={'河北': ['廊坊', '保定']}
#s=json.dumps(d)
# print(s)#结果是一堆Unicode字节，要看明文需要打印一下这个Unicode数据
#print(json.loads(s))
# print({"\u6cb3\u5317": ["\u5eca\u574a", "\u4fdd\u5b9a"]})

# d1={"name":"egon"}
# s1=json.dumps(d1)
# print(type(s1))#<class 'str'>,其实是json字符串因为python中也有str所以直接就是str了
# f=open("new","w")
# f.write(s1)
# f=open("new")
# d2=json.loads(f.read())
# print(d2["name"])

# f=open("new1","w")
# json.dump(d1,f)  #完成两步，第一步把d1转成json字符串，第二步把json字符串进行f.write操作
# f.close()


# i=10
# s='hello'
# t=(1,4,6)
# l=[3,5,7]
# d={"name":"alex"}
# json_str1=json.dumps(i)
# json_str2=json.dumps(s)
# print(json_str1) #'10'
# print(json_str2) #'"hello"'
# f=open("new1")
# json.dump(str(l),f)
# f.write(str(l))
# res=f.read()
# ret=json.loads(res)
# print(res[0])
#json
