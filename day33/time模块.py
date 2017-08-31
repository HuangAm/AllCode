#Python中只有函数，类，模块能够建立自己的名称空间
#for循环和条件语句还有其他的都没有自己的作用域
import time
# print(time.time())#时间戳，给电脑用的
# print(time.localtime())#元组，给程序调用的
# print(time.strftime("%Y-%m-%d %X"))#格式化输出字符串，给人看的
# print(time.strftime("%x %X"))#格式化输出字符串，给人看的
#时间戳-->结构化时间-->字符串时间
#字符串时间-->结构化时间-->时间戳
#时间戳不能直接转换成字符串时间，字符串时间也不能直接转换成时间戳，他们必须经过中间人结构化时间

#时间戳==>结构化时间 localtime/gmtime(seconds=None)
# print(time.localtime(3600*24))#默认传当前时间，东八区时间
# print(time.gmtime(3600*24))#默认传当前时间，标准时区时间

#结构化时间的使用实例time.struct_time就是一个元组
# t=time.localtime()#这一步就是类实例化出一个对象，是struct_time的对象
# help(t)#可以通过help查询struct_time对象的属性
# print(t.tm_hour)#只是其中一个属性，这个是.不出来的pycharm不支持

#结构化时间==>时间戳 mktime(p_tuple)
# print(time.mktime(time.localtime()))#默认传当前时间

#结构化时间==>字符串时间 strftime(format, p_tuple=None) -> string
# print(time.strftime("%Y-%m-%d %X",time.localtime()))#time.localtime()结果就是一个元组

# 字符串时间==>结构化时间 strptime(string, format) -> struct_time
# print(time.strptime("2017-04-26 16:26:04","%Y-%m-%d %X"))#两个参数必须一一对应


#结构化时间==>字符串时间 asctime([tuple]) -> string
# print(time.asctime(time.localtime(3123425546)))#Sun Dec 23 02:12:26 2068，固定格式
#时间戳==>字符串时间  ctime(seconds) -> string
# print(time.ctime(3123425546))#Sun Dec 23 02:12:26 2068，固定格式

#---------其他方法---------
#time.sleep(seconds)
#线程推迟指定的时间运行，单位为秒









