import pymysql
user=input("username:")
pwd=input("password:")

conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
cursor=conn.cursor() #建立连接后获取光标
sql="select * from userinfo where username=%s and password=%s"
#sql="select * from userinfo where username=%(u)s and password=%(p)s"
cursor.execute(sql,(user,pwd,)) #最普通的是元组形式的,执行结果实际上是拿到一个表
# cursor.execute(sql,[user,pwd])
# cursor.execute(sql,{"u":user,"p":pwd})
result=cursor.fetchone() #拿到cursor.execute执行结果的第一行语句
cursor.close()
conn.close()
if result:
    print("登录成功")
else:
    print("登录失败")