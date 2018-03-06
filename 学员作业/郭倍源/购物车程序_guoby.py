#__author__：cangoolin
#date：2018/1/12
import login_interface as li

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998},
]
shopping_cart = []
exit_flag = False
user_name = input("请输入用户名:").strip()
password = input("请输入密码:").strip()
money = int(input("请输入工资:").strip())
while not exit_flag:
    # li.login_interface(user_name,password)
    print("--------商品列表--------")
    for each in goods:
        print(str(goods.index(each) + 1) + "." + each["name"] + "        " + str(each["price"]) )
    choice = input("请输入你选择的商品编号(1-4)/q(退出):")
    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice < 5:
            if goods[choice - 1]["price"] <= money:
                shopping_cart.append(goods[choice - 1])
                money = money - goods[choice - 1]["price"]
                print("\033[92m商品%s已经加入购物车\033[0m,你的余额为:\033[92m%d\033[0m"%(shopping_cart[-1]['name'],money))
            else:
                print("\033[92m金额不够,请选择其他商品.\033[0m")
        else:
            print("\033[92m无此商品!\033[0m")
    elif choice == "q":
        exit_flag = True
        print("--------购物车清单--------")
        for each in shopping_cart:
            print(str(shopping_cart.index(each) + 1) + "." + each["name"] + "        " + str(each["price"]))
        print("你的余额为:\033[92m%d\033[0m"%money)
    else:
        print("\033[92m你的输入有误!\033[0m")