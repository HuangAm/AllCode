# a=(1,2)[0]
# print(a)
import os
# print(os.walk("D://agon"))  #生成器对象
# for i in os.walk("D://agon"):
#     print(i)

'''
结果：
('D://agon', ['aa'], ['a.txt', 'b.txt', 'Inspiron_7559_1.2.2.EXE'])
('D://agon\\aa', [], ['a1.txt'])
'''
# s=os.listdir("D://agon")
# print(s)

dic={"egon123":123}
for i in dic:
    if "egon" in i:
        print(dic)
