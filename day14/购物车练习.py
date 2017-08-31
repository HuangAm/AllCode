# product_list = [
#     ["Iphone7",5800],
#     ["Coffee",30],
#     ["Gedatang",10],
#     ["PythonBook",99],
#     ["bike",200]
# ]
# shopping_cart=[]
# salary = int(input("input your salary:"))
# while True:
#     index = 0
#     for product in product_list:
#         print(index,product)
#         index +=1
#     choice = input(">>:").strip()
#     if choice.isdigit():
#         choice = int(choice)
#         if choice >= 0 and choice < len(product_list):
#             product = product_list[choice]
#             if product[1] <= salary:
#                 shopping_cart.append(product)
#                 salary -=product[1]
#                 print("已经把"+product[0]+"加入到你的购物车，您的余额还剩"+str(salary-product[1]+"元钱"))
#             else:
#                 print("买不起，产品价格是"+str(product[1])+"你还差"+str(product[1]-salary)+"元钱")
#         else:
#             print("商品不存在！")
#     elif choice == "q":
#         print("------已购买商品列表------")
#         for i in shopping_cart:
#             print(i)
#         print("您的余额为：",salary)
#         print("------end------")
#     else:
#         print("无此选项")
product_list = [["Iphone7",5800],
                ["Coffee",30],
                ["Gedatang",10],
                ["PythonBook",99],
                ["bike",200]
                ]
shopping_cart = []
salary = int(input("input your salary:"))
while True:
    index = 0
    for product in product_list:
        print(index,product)
        index += 1
        choice = input(">>:").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice < len(product_list):
                product = product_list[choice]
                if product[1] <= salary:
                    shopping_cart.append(product)
                    salary -= product[1]
                    print("...........")
                else:
                    print(".......")
            else:
                print("商品不存在")
        elif choice == "q":
            print("------已购买商品列表------")
            for i in shopping_cart:
                print(i)
            print("您的余额为：",salary)
            print("------end-------")
        else:
            print("无此选项")























