#grep -rl 'python' D:\\agon
#定义阶段
import os,time
def next_free(func):
    '协助初始化'
    def wrapper(*args,**kwargs):
        res=func(*args,**kwargs)
        next(res)
        return res
    return wrapper
@next_free
def sercher(target):
    '找到绝对路径路径'
    while True:
        dir_name=yield
        print('search：文件绝对路径')
        time.sleep(2)
        g=os.walk(dir_name)
        for i in g:
            for j in i[-1]:
                file_path = '%s\\%s' % (i[0],j)
                target.send(file_path)

@next_free
def opener(target):
    '打开文件'
    while True:
        file_path = yield
        print('opener：文件句柄')
        time.sleep(2)
        with open(file_path) as f:
            target.send((file_path,f))



@next_free
def cat(target):
    '读取文件'
    while True:
        file_path,f = yield
        print('cat：文件内容')
        time.sleep(2)
        for line in f:
            target.send((file_path,line))

@next_free
def grep(pattern,target):
    '过滤出一行内容中有无Python'
    while True:
        file_path,line = yield
        print('grep：包含python这一行内容的文件路径')
        time.sleep(2)
        if pattern in line:
            target.send(file_path)

@next_free
def printer():
    '打印文件路径'
    while True:
        file_path=yield
        print('print：文件绝对路径')
        time.sleep(2)
        print(file_path)

#调用阶段
g=sercher(opener(cat(grep("python",printer()))))
g.send('D:\\agon')
