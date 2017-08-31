#存储过程需要提交数据库,因为它里面不只有查还会有增删改
#简单无参版
# import pymysql
# conn = pymysql.connect(host="localhost",user='root',password='',database='work',charset='utf8')
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# # cursor=pymysql.cursors.DictCursor
# cursor.callproc('p1')
# conn.commit()
# r=cursor.fetchall()
# cursor.close()
# conn.close()
# print(r)

#有in参
# import pymysql
# conn = pymysql.connect(host="localhost",user='root',password='',database='work',charset='utf8')
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# # cursor=pymysql.cursors.DictCursor
# cursor.callproc('p2',(2,3))
# conn.commit()
# r=cursor.fetchall()
# cursor.close()
# conn.close()
# print(r)

#in+out+结果集
# import pymysql
# conn = pymysql.connect(host="localhost",user='root',password='',database='work',charset='utf8')
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# # cursor=pymysql.cursors.DictCursor
# cursor.callproc('p3',(2,3))
# r=cursor.fetchall()
# cursor.execute('select @_p3_0,@_p3_1')
# r1=cursor.fetchall()
# conn.commit()
# cursor.close()
# conn.close()
# print(r1)
# print(r)