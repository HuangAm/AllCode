#coding:utf8
#两种配置方式：config  logger
# config，默认root用户，只能让文件流向一个地方要么是屏幕要么是文件，输出接口是logging
# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",
#                     datefmt="%a %d %b %Y %H:%M:%S",
#                     filename="loger",
#                     filemode="a",#不用w也会自己创建文件
#                     )
# 如果没有上面的函数，下面的默认输出到屏幕
# logging.debug("debug message你好")
# logging.info("info message")
# logging.warning("waining message")
# logging.error("error message")
# logging.critical("critical message")

# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s [%(lineno)s] %(message)s",
#                     datefmt="%Y-%m-%d %H:%M:%S", #时分秒全部大写
#                     filename="loger1",
#                     filemode="a", #追加写，不用w也会自动创建文件，
#                     )
# logging.debug("debug message哈喽")
# logging.info("info message")
# logging.warning("warning message")
# logging.error("error message")
# logging.critical("critical message")

#logger 推荐使用，可以同时打印到屏幕和文件，吸心大法，输出接口是logger
#先产生logger对象，再产生格式对象，然后产生两个流对象并把格式对象作为参数传入，在把两个流对象作为参数传入logger对象，通过对象之间的交互完成输出
#反正就是4个对象最牛逼的是logger然后是文件流和屏幕流，最怂的是格式对象，4个对象搞来搞去
import logging
def get_logger():  #每次用都写这么多太麻烦，直接定义一个函数，要改需求在函数里面改就好了
    logger = logging.getLogger() #实例化产生一个对象
    fm=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s") #创建一个格式对象
    fh=logging.FileHandler("log") #创建一个文件流handler(处理程序)，用于写入日志
    sh=logging.StreamHandler() #创建一个屏幕流，用于输出到控制台

    fh.setFormatter(fm) #文件流吸入格式对象，对象之间的交互
    sh.setFormatter(fm) #屏幕流吸入格式对象，对象之间的交互

    logger.addHandler(fh) #添加文件流，默认就是追加写
    logger.addHandler(sh) #添加屏幕流

    logger.setLevel(logging.DEBUG) #设计等级只能对logger对象进行设置，fh和sh设计了不管用
    return logger
logger=get_logger()
logger.debug("logger debug messgage")
logger.info("logger info message")
logger.warning("logger warning message")
logger.error("logger error message")
logger.critical("logger critical message")

# import logging
#
# logger = logging.getLogger()
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
# logger.addHandler(ch)

# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
# logger1 = logging.getLogger('mylogger')
# logger1.setLevel(logging.DEBUG)

# logger2 = logging.getLogger('mylogger')
# logger2.setLevel(logging.INFO)

# logger1.addHandler(fh)
# logger1.addHandler(ch)
#
# logger2.addHandler(fh)
# logger2.addHandler(ch)

# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')

# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')






# import sys,time
# for i in range(10):
#     sys.stdout.write('#')
#     time.sleep(1)
#     sys.stdout.flush()