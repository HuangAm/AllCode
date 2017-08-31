# import time
# import threading
# def subNum():
#     global num
#     print("ok")
#     lock.acquire() #acquire获取
#     temp=num
#     time.sleep(0.1)
#     num=temp-1
#     lock.release() #release释放
#
# num=100
# thread_list=[]
# lock=threading.Lock()
# for i in range(100):
#     t=threading.Thread(target=subNum)
#     t.start()
#     thread_list.append(t)
# for t in thread_list:
#     t.join() #只是让所有进程都走完在打印下面的print
# print("result:",num)

import time
import threading
def addNum():
    global num
    # num -= 1

    temp=num        #这种情况的结果是99，因为从第一个线程开始保存到内存当中的都是100
    time.sleep(0.1) #就这样一直到最后一个线程都是100，然后没有线程的时候num就
    num = temp-1    #只能等着收100-1的值也就是99
num=100 #设定一个共享变量
threads=[]
for i in range(100):
    t=threading.Thread(target=addNum)
    t.start()
    threads.append(t)
for t in threads: #等待所有线程执行完毕
    t.join()
print("Result: ",num)















