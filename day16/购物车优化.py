product_list = [["Iphone7",5800],#建立一个商品列表
                ["Coffee",30],
                ["Gedatang",10],
                ["PythonBook",99],
                ["bike",200]

                ]
shopping_cart = {}#建一个空字典，装东西，购物车空字典
salary = int(input("input your salary:"))#工资是数字，所以要int()
while True :#当工资是数字的时候，运行循环
    index = 0
    for product in product_list:#从商品列表中取出商品，价格列表
        print(index,product)#打印商品代号，商品和价格列表
        index += 1
    choice = input(">>:").strip()#选择商品对应的数字，stip后空格和Tab无效
    if choice.isdigit():#判断是否为数字
        choice = int(choice)#将数字转为整形
        if choice >= 0 and choice < len(product_list):#商品存在，如果数字大于等于0并且小于商品列表最大数
            product = product_list[choice]#取到商品
            if product[1] <= salary:#判断能否买得起，product包括商品和商品价格
                #买得起
                if product[0] in shopping_cart:#product[0]是商品名字，[1]是商品价格
                    shopping_cart[product[0]][1] +=1#购物车字典，以product[0]为key，value是
                else:
                    shopping_cart[product[0]]=[product[1],1]#加入购物车,创建一条商品购买记录
                salary -=product[1]#扣钱
                print("已经把"+product[0]+"加入到你的购物车，您的余额还剩"+str(salary-product[1])+"元钱")
            else:
                print("买不起，产品价格是"+ str(product[1]) +"你还差"+str(product[1]-salary)+"元钱")
        else:
            print("商品不存在!")
    elif choice == "q":
        print("-----已购买商品列表-----")
        id_counter = 1
        total_cost = 0#初始化一个总消费的变量
        print("id   商品  数量  单价  总价")
        for key in shopping_cart:
            print("%s\t%s\t%s\t%s\t%s"%(id_counter,
                                        key,
                                        shopping_cart[key][1],
                                        shopping_cart[key][0],
                                        shopping_cart[key][1]*shopping_cart[key][0]
                                        ))
            id_counter += 1
            total_cost += shopping_cart[key][1]*shopping_cart[key][0]
        print("您的总花费为：",total_cost)
        print("您的余额为：",salary)
        print("-----end-----")
        break
    else:
        print("无此选项")
