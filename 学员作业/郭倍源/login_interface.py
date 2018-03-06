#__author__：cangoolin
#date：2018/1/6
import pickle
import sys
import traceback

# 初始数据写入硬盘

account_list = [["alex","123",4000],
                ["alvin","123",5000],
                ["cangoolin","123",6000]]
pickle_file = open("account_list_cart.pkl","wb")
pickle.dump(account_list,pickle_file)
print("硬盘成功写入数据。。。")
pickle_file.close()


def login_interface(user_name,pass_word):
    #从硬盘读取数据
    pickle_file = open("account_list_cart.pkl","rb")
    account_list = pickle.load(pickle_file)
    print("从硬盘成功读取数据。。。")
    pickle_file.close()

    count = 3#建议10次比较合理
    while count:
        #用户名和密码一次输入后同时提交
        username = user_name
        password = pass_word

        #拿到所有用户名与输入的用户名比较
        for each in account_list:
            if username == each[0]:#用户名输入正确
                if each[2] == False:#用户状态没有被锁定
                    while not password == each[1]:#密码输入不正确
                        count -= 1
                        print("登录失败，你还有%d次机会" % count)
                        if count == 0:
                            each[2] = True
                            print("您的账户被锁定！")
                            #将锁定状态写入硬盘
                            pickle_file = open("account_list_cart.pkl","wb")
                            pickle.dump(account_list, pickle_file)
                            pickle_file.close()
                            print("退出程序！")
                            sys.exit()
                        password = input("请重新输入密码：")
                    else:
                        print("欢迎您成功登录！")
                        sys.exit()
                else:
                    print("您的账户已被锁定，无法登录！")
                    print("退出程序。。。")
                    sys.exit()

        print("用户名或密码不正确！")
        count -= 1
        print("登录失败，你还有%d次机会"% count)
        if count == 0:
            print("退出程序！")
            sys.exit()

if __name__ == "__main__":
    # 这样做的好处是双击打开时如果出现异常可以报告异常，而不是一闪而过！
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        sys.exit()
        input()