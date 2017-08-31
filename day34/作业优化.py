# import re
# def caculate():
#     a = "".join(input("你要算啥：").split())
#     while True:
#         if "(" in a:
#             b=re.search(r"\([^()]+\)",a)
#             if b:
#                 c=b.group()
#                 d=func(c)
#                 a=re.sub(r"\([^()]+\)",str(d),a,1)
#         else:
#             print(func(a))
#             break
# def func(a):
#     while True:
#         if "*" in a:
#             l=a.split("*")
#             if "/" in l[0]:
#                 a=div(a) #a=res
#             else:
#                 a=mul(a) #a=res
#         elif "/" in a:
#             a = div(a) #a=res
#         else:
#             a=add(a) #d
#             return a
#
# def mul(a):
#     b=re.search(r"\d+\.?\d*\*-?\d+\.?\d*",a)
#     if b:
#         c=b.group()
#         l=c.split("*")
#         d=float(l[0])*float(l[1])
#         res=re.sub(r"\d+\.?\d*\*-?\d+\.?\d*",str(d),a,1)
#         return res
#
# def div(a):
#     b = re.search(r"\d+\.?\d*/-?\d+\.?\d*", a)
#     if b:
#         c = b.group()
#         l = c.split("/")
#         d = float(l[0]) / float(l[1])
#         res = re.sub(r"\d+\.?\d*/-?\d+\.?\d*", str(d), a, 1)
#         return res
#
# def add(a):
#     while True:
#         if "--" in a:
#             a=a.replace("--","+")
#         if "-+" in a:
#             a=a.replace("-+","-")
#         else:
#             break
#     c=re.finditer("-?\d+\.?\d*",a)
#     d=0
#     for i in c:
#         d +=float(i.group())
#     return d
# caculate()




# import re
# def math(dic):
#     x, y = float(dic['x']), float(dic['y'])
#     return x + y if dic['mark'] == '+' else x - y if dic['mark'] == '-' else x * y if dic['mark'] == '*' else x / y
#     # if dic['mark'] == '+': return x + y
#     # elif dic['mark'] == '-': return x - y
#     # elif dic['mark'] == '*': return x * y
#     # else: return x / y
# def suansu(re_str):
#     ret4 = re.search(r'(?P<x>\d+\.?\d*)(?P<mark>[*/])(?P<y>-?\d+\.?\d*)', re_str)
#     try:
#         while ret4.group():
#             re_str = re_str.replace(ret4.group(), str(math(ret4.groupdict())))
#             if '--' in re_str: re_str = re_str.replace('--', '')
#             ret4 = re.search(r'(?P<x>-?\d+\.?\d*)(?P<mark>[*/])(?P<y>-?\d+\.?\d*)', re_str)
#     except AttributeError: pass
#     if '++' in re_str: re_str = re_str.replace('++', '+')
#     ret4 = re.search(r'(?P<x>-?\d+\.?\d*)(?P<mark>[+\-])(?P<y>-?\d+\.?\d*)', re_str)
#     try:
#         while ret4.group():
#             re_str = re_str.replace(ret4.group(), str(math(ret4.groupdict())))
#             ret4 = re.search(r'(?P<x>-?\d+\.?\d*)(?P<mark>[+\-])(?P<y>-?\d+\.?\d*)', re_str)
#     except AttributeError: return re_str
# def main(user_inp):
#     while True:
#         if not re.search('\([+*/\d.\-]*\)', user_inp): return suansu(user_inp)
#         else:
#             for i in re.findall('\([+*/\d.\-]*\)', user_inp):
#                 user_inp = user_inp.replace(i, suansu(i.replace('(', '').replace(')', '')))
# while True: print(main('0'+input('>>>').replace(" ", "")))
# # 这个0主要是为了输入--1这种情况不会输出1而是默认输出--1,但是坏处是输入1会返回01