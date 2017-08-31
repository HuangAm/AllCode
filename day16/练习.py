
# count = 1
# while count <= 3:
#     user_name = input("input your username: ")
#     password = int(input("input your password: "))
#     if user_name == "seven"or"alex" and password == 123:
#         print ("登陆成功")
#         break
#     else:
#         print ("登录失败")
#     count += 1
#     continue
# print("hello boy!")
# a=0
# b=0
# sumi=0
# for i in range(1,100):
#     if i%2 == 0:
#         i=0-i
#         #print(i)
#         sumi=a+i
#         a=sumi
#     #print(a)
#     else:
#         sumji=b+i
#         b=sumji
# sum=sumi+sumji
# print(sum)
# count = 1
# a=0
# b=0
# while count < 100:
#     count += 1
#     if count%2 == 0:
#         oushu = count
#         sumoushu=a+count
#         a=sumoushu
#     else:
#         jushu = count
#         sumjishu=b+count
#         b=sumjishu
# sum=a-b
# print(sum)
# i=0
# b=0
# while i<12:
#     i+=1
#     if i ==6 :
#         continue
#     if i ==10:
#         continue
#     print(i)
#
# a  =  "alex"
# b  =  a.capitalize()
# print(a)
# print(b)
# name = " aleX"
# print(name.strip())
# print(name.startswith("al"))
# print(name.endswith("X"))
# print(name.replace("l","p"))
# print(name.split("l"))
# print(type(name.split("l")))
# print(name.upper())
# print(name.lower())
# print(name[2])
# print(name[:3])
# print(name[3:])
# print(name.index("e"))
# name="alex"
# for i in "alex":
#     print (i)
#print(name.split("e"))
# li = ["alex","eric","rain"]
# print("_".join(li))
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(1,"Tony")
# print(li)
# li[2]="Kelly"
# li.remove("eric")
# print(li.pop(2))
# del li[2:4]
# print(li.reverse())
# for i in li:
# #print(li)
#     print(i)
# for i in li:
#     print(i)
# li  =  ["hello",  'seven',  ["mon",  ["h",  "kelly"],  'all'],  123,  446]
# # print(li[2][1][1])
# print(li[2].index("all"))
# li[2][2]="ALL"
# print(li)
# tu = ('alex',  'eric',  'rain')
# print(len(tu))
# print(tu[1])
# print(tu[0:2])
# for i,number in enumerate(tu,10):
#     print(i,number)
# tu  =  ("alex",  [11,  22,  {"k1":  'v1',  "k2":  ["age",  "name"],  "k3":  (11,22,33)},  44])
# li=list(tu)
# # print(li)
# # li[0]="aaa"
# # tu=tuple(li)
# # print(tu)
# print(type(tu[1][2]["k2"]))
# li[1][2]["k2"].append("seven")
# print(li)
# dic  =  {'k1':  "v1",  "k2":  "v2",  "k3":  [11,22,33]}
# for key in dic:
#     print(key,dic[key])
# dic["k4"]="v4"
# print(dic)
# dic["k1"]="alex"
# print(dic)
# {'k3': [11, 22, 33], 'k1': 'alex', 'k2': 'v2'}
# dic["k3"].append(44)
# print(dic)
# {'k3': [11, 22, 33, 44], 'k2': 'v2', 'k1': 'v1'}
# dic["k3"].insert(0,18)
# print(dic)
# {'k1': 'v1', 'k2': 'v2', 'k3': [18, 11, 22, 33]}
# s  =  "alex"
# list(s)
# print(type(list(s)))
# li  =  ["alex",  "seven"]
# tu = [10,11]
# print(dict(zip(li,tu)))
# {'alex': 10, 'seven': 11}

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
exit_flag = False
current_layer = menu
layers = [menu]
while not exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:").strip()
    if choice == "b":
        current_layer = layers[-1]
        layers.pop()
    elif choice not in current_layer:continue
    else:
        layers.append(current_layer)
        current_layer = current_layer[choice]




































