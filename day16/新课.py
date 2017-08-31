# account = {
#     "name":"qinzhen",
#     "id":1234,
#     "info": [200,10]
# }
# account2 = account.copy()
# account2["name"] = "pianzi"
# account["info"][1] += 30
# print(account,account2)
account = {
    "name":"qinzhen",
    "id" : 1234,
    "info" : [200,10]
}
# account2 = account.copy()
# account2["name"] = "pianzi"#改K对应的值，K是独一无二的
# account["info"][1] += 20#info（key）对应的值[200,10]中的10+20，最后变为[200,30]
# print(account,account2)
account["fuck"] = "you"
print(account)
# account.pop("fuck")
# del account["fuck"]
#account.popitem()#随机删除一个，括号里面不能加key或value
#account["fuck"] = "lalal"#修改Key对应的value

#print("fuck" in account)#查看"fuck"在不在字典里，如果在那就打印出True，如果不在那就是False
#print(account.get("fuck"))#获取“fuck”对应的value，如果key不存在只会返回None
#print(account["fuck"])#用字典和列表找东西都是中括号，但是如果key不存在就会报错

# print(account.values())
# print(account.keys())

# print(account.setdefault("alex","AAALLLLXXXSSS"))#增加key值对，并返回value
# print(account)

# b = {1:2,3:4,"dell":"youxia7000"}
# b.update(account)
# print(b)
#print(account)
#print(account.items())#把字典转换成list
print(dict.fromkeys([1,2,3],"test"))#重新生成一个新的列表
# for key in account:
#     print(key,account[key])

# for k,v in account.items():#会先把dict转成list，数据里大时莫用
#     print(k,v)
