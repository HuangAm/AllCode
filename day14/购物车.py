product_list = [["Iphone7",5800],
                ["Coffee",30],
                ["Gedatang",10],
                ["PythonBook",99],
                ["bike",200]

                ]
shopping_cart = []
salary = int(input("input your salary:"))
while True :
    index = 0
    for product in product_list:
        print(index,product)
        index += 1
    choice = input(">>:").strip()
    if choice.isdigit():#判断是否为数字
        choice = int(choice)
        if choice >= 0 and choice < len(product_list):#商品存在
            product = product_list[choice]#取到商品
            if product[1] <= salary:#判断能否买得起
                #买得起
                shopping_cart.append(product)#加入购物车
                salary -=product[1]#扣钱
                print("已经把"+product[0]+"加入到你的购物车，您的余额还剩"+str(salary-product[1])+"元钱")
            else:
                print("买不起，产品价格是"+ str(product[1]) +"你还差"+str(product[1]-salary)+"元钱")
        else:
            print("商品不存在!")
    elif choice == "q":
        print("-----已购买商品列表-----")
        for i in shopping_cart:
            print(i)
        print("您的余额为：",salary)
        print("-----end-----")
    else:
        print("无此选项")
