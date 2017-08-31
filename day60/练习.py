'''
练习：
    权限管理
    基于角色权限管理系统
    权限一张表（用户管里，订单管理，商品管理）
    权限表：
        1   订单管理
        2   用户管理
        3   菜单管理
        4   权限分配
        5   Bug管理
    用户表：
        1   egon
        2   yuan
        3   alex
    用户权限关系表
        id      用户id    权限id
        1        1          1
        2        1          2
        3        2          3

    用Python实现：
        某个用户登录之后，查看自己拥有的所有权限
'''
import pymysql
# user=input("username:")
# pwd=input("password:")
# conn=pymysql.connect(host="localhost",user="root",password="",database="db1",charset='utf8')
# cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
# # sql="select id,name,qname from 用户权限关系表 left join 权限表 on 用户权限关系表.qx_id=权限表.qid left join 用户信息 on 用户信息.id=用户权限关系表.user_id where name=%s"
# sql="select id,name,password from userinfo"
# cursor.execute(sql)
# result=cursor.fetchall()
# cursor.close()
# conn.close()
# print(result)
# for i in result:
#     print(i)


conn = pymysql.connect(host='localhost', user="root", password="", db='db1', charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = "select id,name,password from userinfo"
cursor.execute(sql)
result = cursor.fetchall()
cursor.close()
conn.close()
print(result)





















