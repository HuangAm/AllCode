
f=open("uptest",encoding="utf8")#打开账户信息文件
f1=open("uptest1","a+",encoding="utf8")#打开黑名单文件
up_input=[]#创建一个装输入过用户名的列表
while True:
    username = input("please input usrname:").strip()  # 输入用户名
    password = input("please input password:").strip()  # 输入密码
    up_input.append(username)#将输入过的用户名放入列表
    count=up_input.count(username)#查同一个用户名登了几次
    if count == 4:#同样的用户名输入三次后锁定
        print("Goodbye!")
        f1.write(username)
    for line1 in f1:
        if username==line1.strip():
            print("Goodbye!")
            exit()
    for line in f :
        name=line.strip().split("---")[0]
        pwd=line.strip().split("---")[1]
        if name == username and pwd == password:
            print("Welcome baby!")
        else:
            continue



