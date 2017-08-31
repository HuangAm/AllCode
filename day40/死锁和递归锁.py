# import threading
# import time
#
# mutexA=threading.Lock() #同步锁
# mutexB=threading.Lock()
#
# class MyThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#     def run(self):
#         self.fun1()
#         self.fun2()
#     def fun1(self):
#         mutexA.acquire() #如果锁被占用，则阻塞在这里，等待锁的释放
#         print("I am %s,get res:%s---%s" %(self.name,"ResA",time.time()))
#         mutexB.acquire()
#         print("I am %s,get res: %s---%s" %(self.name,"ResB",time.time()))
#         mutexB.release()
#         mutexA.release()
#     def fun2(self):
#         mutexB.acquire()
#         print("I am %s,get res: %s---%s" %(self.name,"ResB",time.time()))
#         time.sleep(0.2)
#         mutexA.acquire()
#         print("I am %s,get res: %s---%s" %(self.name,"ResA",time.time()))
#         mutexA.release()
#         mutexB.release()
# if __name__ == '__main__':
#     print("start------------%s"%time.time())
#     for i in range(10):
#         my_thread=MyThread()
#         my_thread.start()
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()