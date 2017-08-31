
#查 www.oldboy2.org
def check():    #当用户输入www.oldboy1.org用户信息后，打印对应的server信息
    l=[]
    m=input("please input something:").strip()
    flag=False#标志位
    with open("haproxy.conf",encoding="utf-8")as f_read:
        for line in f_read:
            if line.startswith("backend")and m in line: #第一步，进行信息匹配
                flag=True   #设定一个开关
                continue
            if line.startswith("backend")and flag:  #将开关关闭，跳出循环
                break
            if flag:    #第二步，将所有信息存到列表里面去
                l.append(line.strip())
    for i in l:
        print(i)
def add():  #{"backend":"www.oldboy20.org","record":{"server":1111,"weight":2222,"maxconn":3333}}
    m = input("please input something:").strip()
    m = eval(m)
    flag = False  # 标志位
    l_add = ["\t\t""server", m["record"]["server"], "weight", m["record"]["weight"], "maxconn", m["record"]["maxconn"]]
    with open("haproxy.conf", encoding="utf-8")as f_read, open("test_add", "r+", encoding="utf-8")as f_write:
        for line in f_read:
            if line.startswith("backend") and m["backend"] in line:  # 第一步，进行信息匹配
                flag = True
            f_write.write(line)
            if 'server' in line and flag:
                for i in l_add:
                    f_write.write(i + " ")
def delete():#{"backend":"www.oldboy20.org","record":{"server":1111,"weight":2222,"maxconn":3333}}
    m=input("please input something:").strip()
    m = eval(m)
    flag=False#标志位
    with open("test_add",encoding="utf-8")as f_read,open("test_delete","w+",encoding="utf-8")as f_write:
        for line in f_read:
            if m["record"]["server"] in line and m["record"]["weight"]:
                continue
            f_write.write(line)
def change():# {"backend":"www.oldboy2.org","record":{"server":"0000","weight":"0000","maxconn":"0000"}}
    m = input("please input something:").strip()
    m = eval(m)
    flag = False  # 标志位
    l_change = ["\t\t""server", m["record"]["server"], "weight", m["record"]["weight"], "maxconn", m["record"]["maxconn"],
             "\n"]
    with open("haproxy.conf", encoding="utf-8")as f_read, open("test_change", "w+", encoding="utf-8")as f_write:
        for line in f_read:
            if line.startswith("backend") and m["backend"] in line:  # 第一步，进行信息匹配
                flag = True
            f_write.write(line)
            if 'server' in line and flag:
                for i in l_change:
                    f_write.write(i + " ")
                flag = False
                continue
def tell_msg():
    msg='''
    add:添加
    check:查找
    delete:删除
    change:修改
    q:退出
    '''
    print(msg)
menu_dict={
    "add":add,
    "delete":delete,
    "change":change,
    "check":check
}
while True:
    menu_list=["add","delete","change","check"]
    tell_msg()
    choice=input("please input your choice:")
    if choice in menu_list:
        menu_dict[choice]()
    elif choice == "q":
        exit()
    else:
        print("Not Found!")
        continue



