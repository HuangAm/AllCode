# D:\\agon
import os
def next_free(func):
    '初始化装饰器'
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@next_free
def searcher(target):
    while True:     #为什么while要放到yield的上面，因为如果在下面send一次后就找不到yield了，就会报错并结束运行
        fail_path = yield
        for i in os.walk(fail_path):
            for j in i[-1]:
                fail_path=("%s\\%s" %(i[0],j))
                target.send(fail_path)

@next_free
def opener(target):
    while True:
        fail_path=yield
        with open(fail_path) as f:
            target.send((fail_path,f))


@next_free
def greper(word,target):
    while True:
        fail_path,f = yield
        for line in f:
            if word in line:
                target.send((fail_path))

@next_free
def printer():
    while True:
        fail_path=yield
        print(fail_path)
g=searcher(opener(greper("python",printer())))
g.send("D://agon")



























