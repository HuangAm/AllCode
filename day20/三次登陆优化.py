f = open("uptest", encoding="utf8")  # 打开账户信息文件
f1 = open("uptest1", "r+", encoding="utf8")  # 打开黑名单文件
up_input = []  # 创建一个装输入过用户名的列表
while True:
    username = input("please input usrname:").strip()  # 输入用户名
    up_input.append(username)  # 将输入过的用户名放入列表
    count = up_input.count(username)  # 查同一个用户名登了几次
    if count >= 4:  # 同样的用户名输入三次后锁定,
        print("Locking!")#已锁定的意思
        f1.write(username)
        break
    for line1 in f1:#检查黑名单中是否有输入的用户名
        if username in line1:
            print("Locking!")#已经锁定
            exit()
    password = input("please input password:").strip()  # 输入密码
    for line in f:#核对登录信息
        name = line.strip().split("---")[0]
        pwd = line.strip().split("---")[1]
        if name == username and pwd == password:
            print("Welcome baby!")
            break
        else:
            continue
