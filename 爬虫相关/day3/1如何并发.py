url_list = [
    'http://www.cnblogs.com/wuyongqiang',
    'http://www.baidu.com',
    'http://www.xiaohuar.com',
]
import requests
#串行
# for url in url_list:
#     response = requests.get(url)
#     print(response.content)

#线程、进程，创建的不是越多越好
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def test(url):
    response = requests.get(url)
    print(response.content)

pool = ThreadPoolExecutor(10)
for url in url_list:
    pool.submit(test,url) #去线程池中获取一个线程,执行task函数
pool.shutdown(wait=True) #等待所有线程都执行完

#异步：回调,任务完成后通过回调函数通知一下你
#非阻塞：不等待，obj_socket.setblocking=False比如给socket设置非阻塞,建立connect后就直接进行下一步直接收消息然后报错
#异步和非阻塞分开的话意义不大，一般都合在一起用






