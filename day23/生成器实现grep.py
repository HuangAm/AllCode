#/usr/bin/env python
#定义阶段：定义两个生成器函数
import time
def tail(file_path):
    with open(file_path,encoding="utf8") as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if not line:
                time.sleep(0.5)
                continue
            else:
                yield line
def grep(pattern,target):
    for line in target:
        if pattern in line:
            yield line
#调用阶段：得到两个生成器对象
g1=tail("/tmp/a.txt")
g2=grep("error",g1)
#next触发执行改g2生成器函数 ,用for循环或者while循环来
for i in g2:
    print(i)