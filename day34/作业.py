import re
def func(a):
    while True: #这个循环的作用就是用来四则运算的
        if '*' in a:
            c = a.split('*')
            if '/' in c[0]:
                a = div(a)
            else:
                a = mul(a)
        elif '/' in a:
            a = div(a)
        else:
            a = add(a)
            return a
def mul(a):
    b = re.search(r'\d+\.?\d*\*-?\d+\.?\d*', a)
    if b:
        b = b.group()
        l=b.split("*")
        c=float(l[0])*float(l[1])
        res = re.sub(r'\d+\.?\d*\*-?\d+\.?\d*', str(c), a,1)
        return res
def div(a):
    b = re.search(r'\d+\.?\d*/-?\d+\.?\d*', a)
    if b:
        b = b.group()
        l=b.split("/")
        c=float(l[0])/float(l[1])
        res = re.sub(r'\d+\.?\d*/-?\d+\.?\d*', str(c), a,1)
        return res
def add(a):
    if '--' in a:
        a = a.replace('--', '+')
    if "-+" in a:
        a = a.replace("-+","-")
    b = re.findall(r'-?\d+\.?\d*', a) #把负数两个字符看成一个整体
    c=0
    for i in b:
        c+=float(i)
    return c
def caculate():
    a = ''.join(input('你要算啥：').split())#把输入字符串以空格切片然后在拼接
    while True:
        if '(' in a: #如果有括号就把括号里面的东西算出来替换掉
            b = re.search(r'\([^()]+\)', a) #把最里面的(...）作为一个对象拿到
            if b: #怕有二货输个空括号
                c = b.group() #把(...)拿出来赋给c
                d = func(c) #包括号里面表达式计算出来
                a = re.sub(r'\([^()]+\)', str(d), a, 1) #操操操，这个狗比1,害老子蒙圈一下午，用结果替换(...)
        else: #没要括号直接进行四则运算运算
            print(func(a))
            break
caculate()