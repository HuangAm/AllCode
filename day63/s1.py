from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine

Base=declarative_base() #陈述基类,拿到Base基类

#创建表单,类就是表单,但是在数据库中的表明是__tablename__
class UserType(Base):
    __tablename__='usertype'  #真正的表名
    id=Column(Integer,primary_key=True,autoincrement=True) #主键 这两行在执行的时候会被放到__init__中
    title=Column(String(32),nullable=True,index=True) #普通索引

class Users(Base):
    __tablename__='users' #真正的表名
    id=Column(Integer,primary_key=True,autoincrement=True) #主键
    name=Column(String(32),nullable=True,index=True)
    email=Column(String(16),unique=True) #一个unique就能代表唯一索引么,不需要加index么
    user_type_id=Column(Integer,ForeignKey('usertype.id')) #外键

    #建立联合索引
    __table_args__=(
        UniqueConstraint('id','name',name='uix_id_name'),
        Index('ix_name_email','name','email')
    )

    #为连表而生的relationship
    user_type=relationship("UserType",backref='xxoo')

engine=create_engine("mysql+pymysql://root:@127.0.0.1:3306/db4?charset=utf8",max_overflow=5)
#引擎中的db4必须是已经建好的,连接池的功能
Base.metadata.create_all(engine) #检测文件中所有继承了Base类的类,在mysqld中建立所有的表,类就是表
Session=sessionmaker(bind=engine) #根据对话制造者,绑定引擎,创建出对话类,bind=engine就是socket里面的bind
session=Session() #对话类实例化出对话对象

#类-->表
#对象-->行
#增加-----------------------------------------------
# obj1=UserType(title='普通用户')
# session.add(obj1)
# objs=[
#     UserType(title='超级用户'),
#     UserType(title='白金用户'),
#     UserType(title='黑金用户'),
# ]
# session.add_all(objs)
# session.commit()
# session.close()

#查-------------------------------------------------
# print(session.query(UserType)) #打印结果是查询的sql语句 select usertype.id as usertype_id, usertype.title as usertype_title from usertype
# user_type_list=session.query(UserType).all() #不加all的话是迭代器,加all的话是可迭代对象列表
# print(user_type_list)
# user_type_list=session.query(UserType.id,UserType.title).all()
# 加all后直接就出来值了,不加all就是sql语句,原因在你写的是 UserType 还是 UserType.id,UserType.title 前者实是类,后面两个是对象
# print(user_type_list)
# print(type(UserType.id))
# for row in user_type_list:
#     print(row.id,row.title)

# user_type_list=session.query(UserType.id,UserType.title).filter(UserType.id>2)
##相当于select * from UserType where  session.query=selelct filter=where
# for row in user_type_list:
    # print(row.id,row.title)
    # print(row[0],row[1]) #两种查看方式

#删除--------------------------------------------------
# session.query(UserType.id,UserType.title).filter(UserType.id>2).delete()
# session.commit() #增删改一定要记得加commit
#修改--------------------------------------------------
# session.query(UserType.id,UserType.title).filter(UserType.id>0).update({"title":"黑金"})#全部修改
# session.query(UserType).filter(UserType.id > 0).update({UserType.title: UserType.title + "x"},synchronize_session=False) #在原来的基础上修改
# session.query(UserType).filter(UserType.id>0).update({"num":Users.num+1},synchronize_session="evaluate")#如果是数字列的话,会增加1
# session.commit()
# result=session.query(Users).join(UserType)
# print(result)
# result=session.query(Users).join(UserType,isouter=True) #加isouter=True就是建立左连接,有链接换一下位置
# print(result)
# result=session.query(UserType).all()
# print(result)
# for i in result:
#     print(i.id,i.title)
# 子查询---------------------------
# q1=session.query(UserType).filter(UserType.id>2).subquery()
# result=session.query(q1).all()
# print(result)
# result=session.query(UserType.id,session.query(Users).subquery()).all()#笛卡尔机了
# for i in result:
#     print(i)
# result=session.query(UserType.id,session.query(Users).filter(Users.id==1).subquery()).all()
# for i in result:
#     print(i)
# 1.select * from b where id in (select id from tb2)
# ret = session.query(Users).filter(Users.id.in_(session.query(UserType.id).filter(UserType.id>2))).all()
# print(ret)#每次返回的到底是对象还是真实值，傻傻分不清
# for i in ret:
#     print(i[1],i[2])
# 2.select * from (select * from tb)as B
# q1=session.query(UserType).filter(UserType.id>2).subquery()
# result=session.query(q1).all()
# print(result)
#动态传值
#select
#   id,
#   (select * from users where users.user_type_id=usertype.id),
#   ()
result=session.query(UserType.id,session.query(Users).filter(Users.user_type==UserType.id).as_scalar())
print(result)


#为连表而生的relationship
#正向操作
# user_list=session.query(Users)
# for row in user_list:
#     print(row.name,row.id,row.user_type.title)
#反向操作
# user_type_list=session.query(UserType)
# for row in user_type_list:
#     print(row.id,row.title,row.xxoo.name)
