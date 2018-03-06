# 商品列表
import json
goods = [
    {"name": "手机", "price": 1999},
    {"name": "耳机", "price": 100},
    {"name": "键盘", "price": 200},
    {"name": "美女", "price": 998},
    {"name": "媳妇", "price": 2998},
    {"name": "电脑", "price": 5998}
]

with open('goods_file','w') as f :
    f.write(json.dumps(goods))