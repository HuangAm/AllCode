# _*_ coding:utf8 _*_
import pymysql
db=input("输入要连接的数据库：")
conn=pymysql.connect(host="localhost",port=3306,user="root",passwd='',db=db,charset='utf8')
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
my="1"
while my:
    my=input("输入sql语句: ")
    try:
        cursor.execute(my)
        ret=cursor.fetchall()
        if ret:
            for i in ret:
                print(i)
        new_id=cursor.lastrowid
        if new_id:
            print(new_id)
        conn.commit()
    except Exception as E:
        print(E)
        continue
cursor.close()
conn.close()