from AsyncNoBlocking import AsyncNoBlocking

def done1(response):
    """回调函数,对响应内容进行处理"""
    print("from done1")

def done2(response):
    """回调函数,对响应内容进行处理"""
    print("from done2")

def done3(response):
    """回调函数,对响应内容进行处理"""
    print("from done3")

url_list = [
    {'host':'www.baidu.com','port':80,'path':'/','callback':done1},
    {'host':'www.cnblogs.com','port':80,'path':'/','callback':done2},
    {'host':'www.bing.com','port':80,'path':'/','callback':done3},
]

anb = AsyncNoBlocking()
for item in url_list:
    anb.add_request(item) #创建请求
anb.run()