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

current_layer =menu
layer = []

while True:
    for i in current_layer:#将当前层赋值给i
        print(i)
    choice = input (">:").strip()
    if not choice:continue
    if choice in current_layer:
        layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == "b":
        if len(layer) !=0:
            current_layer= layer.pop()
        else:
            print("到顶了")
    elif choice =="q":
        exit("offer")
