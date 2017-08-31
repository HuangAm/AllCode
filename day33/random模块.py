# import random
# print(random.random()) #大于0且小于1之间的浮点数
# print(random.randint(1,5)) #1 <= x <= 5
# print(random.randrange(1,5)) #1 <= x <5
# print(random.choice([1,["23"],[4,5]]))#随机三取一
# print(random.sample([1,["23"],[4,5]],2))#随机三取二
# print(random.uniform(1,3)) #大于1小于3的数

# import random
# print(random.random()) #大于0且小于1之间的小数
# print(random.randint(1,5)) #大于等于1且小于等于5之间的整数
# print(random.randrange(1,3)) #大于等于1且小于3之间的整数
# print(random.choice([1,"23",[4,5]])) #三个里面随机选一个
# print(random.sample([1,"23",[4,5]],2)) #列表中任意2个组合
# print(random.uniform(1,3)) #大于1小于3的小数浮点数
# item=[1,3,5,7,9]
# random.shuffle(item)#随机打乱次序
# print(item)

#练习：生成验证码
# import random
# def v_code():
#     code="" #先定一个空字符串，用来装验证码
#     for i in range(5): #确定验证码的位数为5位，循环五次
#         num=random.randint(0,9) #随机取一个整数
#         alf=chr(random.randint(65,90)) #通过ascii码表取出65-90，即a-z中的任意一个
#         add=random.choice([num,alf]) #在数字和字母中随机取一个,注意choice的参数用[]包起来
#         code="".join([code,str(add)]) #完成字符串的拼接，并赋值给code，初始的code为空为了保证正常拼接
#     return code  #返回拼接好的5位字符串
# print(v_code())
