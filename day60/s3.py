#进行增加删除和修改一定需要 conn.commit() 语句,一定得提交不然数据是提交不到数据库的
#这相当于事务
#查询的时候返回值是由fetch和excute产生的,代表你想看到的行的内容,后者代表受影响的行
#增删改的时候返回值是由excute返回的,代表受影响的行号
import pymysql

#增加
#写死的
# conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
# cursor=conn.cursor()
# sql="insert into userinfo(username,password) values('root1',123)"
# cursor.execute(sql)
# conn.commit()
# cursor.close()
# conn.close()
#变量接收
# user="egon1"
# pwd="123"
# conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
# cursor=conn.cursor()
#单行插入----------------------------------------------------
# sql="insert into userinfo(username,password) values(%s,%s)"
# cursor.execute(sql,(user,pwd))
#多行插入----------------------------------------------------
# sql="insert into userinfo(username,password) values(%s,%s)"
# r=cursor.executemany(sql,[('egon2','sb'),('laoyao','SB')])
# print(r)
# conn.commit()  #通过连接提交
# cursor.close()
# conn.close()
#executemany和excute都有一个返回值,表示受影响的行数
#executemany只适用于增加
#增删改大致一样，可以归为一类，查自己属于一类



#查
# conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
# # cursor=conn.cursor() #元组类型
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) #字典类型
# sql="select * from userinfo"
# r=cursor.execute(sql)
# print(r)
# result=cursor.fetchone()
# print(result)
# result=cursor.fetchone()
# print(result)
# result=cursor.fetchone()
# print(result)
# # cursor.scroll(1,mode="relative") #相对于当前位置移动
# # cursor.scroll(2,mode="relative") #相对于绝对位置移动,就是相对于1定位
# # cursor.scroll(2,mode="relative")
# # cursor.scroll(3,mode="absolute")
# # result=cursor.fetchone()
# # print(result)
# result=cursor.fetchmany(5)
# print(result)
# result=cursor.fetchall()
# print(result)
# cursor.close()
# conn.close()
# #不管是fetchall还是fetchmany还是fetchone都跟conn.cursor()的位置有关
# #fetchall配合sel语句里面的limit用于分页

#新插入数据的自增ID
# conn=pymysql.connect(host="localhost",user="root",password="",database="db1")
# cursor=conn.cursor()
# sql="insert into article(title,hobby) VALUE ('武藤兰','wusir')"
# cursor.execute(sql)
# print(cursor.lastrowid)  #就是新插入的这条数据的id,差多条数据只显示最后一行的值
# sql="insert into media(path,article_id) VALUE ('D://agon','cursor.lastrowid')"
# cursor.execute(sql)
# cursor.close()
# conn.close()


'''
总结：
    连接、关闭（conn，cursor）
    execute(sql,()/[]/{})防止sql注入 返回值是受影响的行号
    增删改记得加conn.commit()
    查记得加fetchone fetchall fetchmany
    cursor.lastrowid 获取最后插入数据的自增ID
'''