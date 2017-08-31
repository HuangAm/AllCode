from conf import setting
from lib import shop
from lib import manage
import logging
import json
#opelog记录ATM操作日志
#paylog记录每月日常流水消费
def run():
    def db(name):
        with open(setting.db_path) as f:
            i=f.read()
            if name in i:
                return json.loads(i)[name]
            else:
                print("用户名或密码错误！")
                exit()
    current_login = {"name": None, "login": False}
    def auth(func):
        def wrapper(*args, **kwargs):
            if current_login['name'] and current_login['login']:
                res = func(*args, **kwargs)
                return res
            else:
                name = input('用户名:')
                password = int(input('密码:'))  ##intintint
                d = db(name)
                if password == d["pwd"]:
                    # print('auth successful')
                    current_login['name'] = name
                    current_login['login'] = True
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('用户名或密码错误！')
        return wrapper

    @auth
    def position():
        "查看额度，操作日志"
        dic = db(current_login["name"])
        a = dic["position"]
        b = dic["IDcard"]
        print("您卡号为%s的信用卡所剩额度为：%s" % (b, a))
        logger(setting.oplog_path, "用户%s 查看信用卡余额"%current_login["name"])

    @auth
    def shopping():
        "购物，信用卡接口，流水日志"
        with open(setting.db_path) as f:
            d_target = json.loads(f.read())
        d = d_target
        a = current_login["name"]
        shop.shop(d,a)

    @auth
    def withdraw():
        "提现，流水日志，操作日志"
        dic = db(current_login["name"])
        a = dic["position"]
        b = dic["IDcard"]
        c = 0.95*dic["position"]
        print("您卡号为%s的信用卡所剩额度为：%s" % (b, a))
        print("您可提现额度为：%s" %c)
        e=input("输入金额：").strip()
        while True:
            if int(e) <= c:
                with open(setting.db_path,"r",encoding="utf8") as f:
                    d = json.loads(f.read())
                    f = current_login["name"]
                    d[f]["position"]-=int(e)*1.05
                d_new=d
                with open(setting.db_path,"w") as f:
                    f.write(json.dumps(d_new))
                    print("提款成功")
                    logger(setting.oplog_path, "用户%s 提款%s" %(current_login["name"],e))
                break
            elif e=="q":
                break
            else:
                print("提不了")



    @auth
    def transfer():
        "转账，流水日志，操作日志"
        dic = db(current_login["name"])
        a = dic["position"]
        name2=input("请输入对方姓名：")
        obj = input("请输入对方的卡号：")
        with open(setting.db_path, "r", encoding="utf8") as f:
            d = json.loads(f.read())
        if name2 in d and obj==dic["name2"]:
            num_money=int(input("请输入金额："))
            if num_money <= a:
                with open(setting.db_path,"r",encoding="utf8") as f:
                    d = json.loads(f.read())
                    f = current_login["name"]
                    d[f]["position"]-=num_money
                d_new = d
                with open(setting.db_path, "w") as f:
                    f.write(json.dumps(d_new))
                    print("转账成功")
                    logger(setting.oplog_path, "用户%s 向%s转账%s" % (current_login["name"],name2,num_money))
        else:
            print("账户不存在")



    @auth
    def lspay():
        "查看日常消费流水，操作日志"
        for line in  setting.db_path:
            if current_login["name"] and "支出"in line:
                print(line)

    @auth
    def repay():
        "还款"
        dic = db(current_login["name"])
        a = dic["position"]
        need_money=15000-a
        if need_money > 0:
            while  True:
                print("需还额度为：%s" % (need_money))
                repay_money = int(input("请输入所还金额："))
                if repay_money <= need_money:
                    new_position=need_money-repay_money
                    with open(setting.db_path, "r", encoding="utf8") as f:
                        d = json.loads(f.read())
                        f = current_login["name"]
                        d[f]["position"] = new_position
                    d_new = d
                    with open(setting.db_path, "w") as f:
                        f.write(json.dumps(d_new))
                        print("还款成功")
                        logger(setting.oplog_path, "用户%s 还款%s" % (current_login["name"],repay_money))
                        break
                else:
                    print("您输入的金额不符，请重新输入")
                    continue
        else:
            print("您当前无需还款")

    def manager():
        "管理接口，添加账户，用户额度，冻结账户"
        mana_dic={
            "添加账户":"adduser",
            "管理额度":"change_limit",
            "冻结账户":"frozen"
                  }
        while True:
            print(main_dic)
            choice=input("请输入你的选择：")
            if not choice:continue
            if hasattr(manage,main_dic[choice]):
                getattr(manage,main_dic[choice])()
            else:continue

    def login():
        "登录"
        name = input('用户名:')
        password = int(input('密码:'))  ##intintint
        d = db(name)
        if password == d["pwd"]:
            # print('auth successful')
            current_login['name'] = name
            current_login['login'] = True
            logger(setting.oplog_path, "用户%s 登录"%name)
            if name == "admin":
                manager()

    def logger(w,q=setting.oplog_path):  # 每次用都写这么多太麻烦，直接定义一个函数，要改需求在函数里面改就好了
        logger = logging.getLogger()  # 实例化产生一个对象
        fm = logging.Formatter("%(asctime)s %(message)s")  # 创建一个格式对象
        fh = logging.FileHandler(q)  # 创建一个文件流handler(处理程序)，用于写入日志
        # sh = logging.StreamHandler()  # 创建一个屏幕流，用于输出到控制台

        fh.setFormatter(fm)  # 文件流吸入格式对象，对象之间的交互
        # sh.setFormatter(fm)  # 屏幕流吸入格式对象，对象之间的交互

        logger.addHandler(fh)  # 添加文件流，默认就是追加写
        # logger.addHandler(sh)  # 添加屏幕流

        logger.setLevel(logging.DEBUG)  # 设计等级只能对logger对象进行设置，fh和sh设计了不管用
        logger.warning(w)

    main_dic={"查额度":position,
              "去购物":shopping,
              "去提现":withdraw,
              "去转账":transfer,
              "查流水":lspay,
              "去还款":repay,
              "登录":login
              }
    while True:
        print('''
        -------------------------------
              "查额度":position,
              "去购物":shopping,
              "去提现":withdraw,
              "去转账":transfer,
              "查流水":lspay,
              "去还款":repay,
              "登录":login
        -------------------------------
        ''')
        choice=input("请输入您的选择：").strip()
        if choice in main_dic:
            main_dic[choice]()
        elif choice == "退出":break
        else:continue
run()