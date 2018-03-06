goods = [
    ("电脑", 1999),
    ("鼠标", 10),
    ("游艇", 20),
    ("美女",998)]

goods_cart = []
budget = input("请输入你的预算：")

while False:
    if budget.isdigit():#验证预算是否为数字
        print("请重新输入：")

budget = int(budget)

while True:
    print("商品列表".center(30,"-"))
    print("编号","名称","价格")
    for i in enumerate(goods):
        print(str(i[0]),str(i[1][0]),str(i[1][1]))

    choice = input("请输入你的选择：")
    if choice.isdigit():#验证选择是否为数字
        choice = int(choice)
        if choice >= 0 and choice < len(goods):#选择>0且<列表长度
            if budget - goods[choice][1] >=0:#预算减去所选商品
                goods_cart.append(goods[choice])#购物车增加所选商品
                budget -= goods[choice][1]#新预算=预算-所选商品
                print("余额还有%d" % budget)
            else:
                print("余额不足")
        else:
            print("该商品不存在")
    elif choice =="q":
        break
    else:
        print("你的输入有误")

print("\033[1m余额还有%d" %budget)
print("购物车商品信息".center(30,"-"))

for i in enumerate(goods_cart):
    print(str(i[0]), str(i[1][0]), str(i[1][1]))