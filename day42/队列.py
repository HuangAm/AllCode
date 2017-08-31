# import queue
# q=queue.Queue(3) #first in first out （FIFO）
# Queue类的__init__()中有一个参数maxsize,设置最大put量
#这里设置为3
# q.put(111)
# q.put("hello")
# q.put(2220)
# q.put(222,False) #raise Full
# q.put(222) #这是第四次put但是maxsize为3,这次不成功底下都不运行,1个也取不出来

# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get(False))  #raise Empty
#---------------------------------------------------------------------------
# import queue
# q=queue.Queue()
# q.put(111)
# q.put(222)
# q.task_done()
# q.task_done() #如果只有put没有get，put几次就需要几个task_done
# q.join() #阻塞进程知道所有任务完成,配合task_done操作
# print("ending")
# import queue
# q=queue.Queue()

# q.put(111)
# q.put(222)

#  #如果只有put没有get，put几次就需要几个task_done
# print(q.get())
# # print(q.get()) #如果get和put都出现，task_done
# q.task_done()
# q.task_done()
# # q.get()
# q.join() #阻塞进程知道所有任务完成,配合task_done操作
# print("ending")
#----------------------------------------------------------------------------
#先进后出
# import queue
# q=queue.LifoQueue(5) #last in first out (LIFO)
# q.put(111)
# q.put(222)
# q.put(333)
# print(q.get())
#-------------------------------------------------------------------------
#按优先级来
# import queue
# q=queue.PriorityQueue() #priority 优先权
# q.put([1,"hello"]) #列表形式，第一个元素是定优先级的，第二个元素是你插入的数据
# q.put([0,"hello"])
# q.put([-1,"hello"])
# print(q.get())
# print(q.get())
# print(q.get())
#-------------------------------------------------------------------------
#生产者消费者而模型,和线程进程、队列是没有关系的，这是一种设计模式
#我们可以配合队列来模拟这种模型
#这个模型是通过一个容器来解决生产者和消费者的强耦合问题的
#在线程的世界里，生产者就是生产数据的线程，消费者就是消费数据的线程
#A-->B-->C  C-->B-->A  B就相当于一个缓冲区,平衡生成者和消费者的处理能力
# import queue
# import time,threading,random
# q=queue.Queue()
# def producer(name):  #生产数据的函数
#     count=0
#     while count<10:
#         print("making....")
#         time.sleep(2)
#         # time.sleep(random.randrange(3))
#         q.put(count)
#         print("producer %s has produced %s baozi..." %(name,count))
#         count +=1
#         q.task_done()
#         q.join()
#         print("ok.....")
#
# def consumer(name):
#     count=0
#     while count<10:
#         time.sleep(1)
#         if not q.empty(): #如果队列里面不为空
#             data=q.get()
#             # q.task_done()
#             # q.join()
#             print(data)
#             print("\033[32;1mConsumer %s has eat %s baozi...\33[0m" %(name,data))
#         else:
#             print("-------no baozi anymore-------")
#         count += 1
# p1=threading.Thread(target=producer,args=("Atai",))#args的参数后面是元组形式,而且一定要加,号哦
# c1=threading.Thread(target=consumer,args=("egon",))
# # c2=threading.Thread(target=consumer,args=("alex",))
# # c3=threading.Thread(target=consumer,args=("yuan",))
# p1.start()
# c1.start()