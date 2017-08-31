import pymysql
#在Python3只有pymysql  在Python2中有mysqldb和pymysql
user = input("username:")
pwd = input("password:")
#用pymysql建立连接要指定host,user,password,database
conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
cursor=conn.cursor() #cursor叫游标相当于seek
sql="select * from userinfo WHERE username='%s' and password='%s'" %(user,pwd,)#%s一定要加引号
cursor.execute(sql)
result=cursor.fetchone() #fetchone就是取一个,result是返回值,就是查到的东西,没有返回none
cursor.close()#先close,cursor
conn.close()#在close,conn
print(result)
if result:
    print('登陆成功')
else:
    print("登录失败")
#sql语句注入尝试输入,为啥我的sql注入成功不了啊~~~,因为--后面没有加空格
    # alex' -- (--后面要+空格)
    # yuan' or 1=1 -- （--后面+空格）
#------------------------------------------------------------------------------------------
#上面的代码会出现sel注入问题,很容易被黑
#不用自己拼字符串pymsql会帮我们做字符串拼接