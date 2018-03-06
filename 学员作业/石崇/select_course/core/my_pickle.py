#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong
import pickle
import os
# 封装常用的类，便于使用
class MyPickle:
    def __init__(self,filename):
        self.filename = filename

    def dump(self,obj):
        with open(self.filename,'ab') as f:
            pickle.dump(obj,f)

    def load(self):
        with open(self.filename,'rb') as f:
            while True:
                try:
                    obj = pickle.load(f)
                    yield obj
                except:
                    break

    def edit(self,obj):  # 修改已保存的文件
        f2 = MyPickle(self.filename+'.new')
        for i in self.load():
            if i.name == obj.name:
                f2.dump(obj)
            else:
                f2.dump(i)
        os.replace(self.filename+'.new',self.filename)



