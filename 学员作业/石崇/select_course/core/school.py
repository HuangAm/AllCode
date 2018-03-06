#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong
from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))   # os.getcwd()获取当前目录，os.path.dirname()获取上一级目录

class Classes:
    '''
    班级类
    '''
    def __init__(self,school,name,subject,student_path):
        self.school = school  # 学校
        self.name = name # 班级名,如python10期
        self.subject = subject # 学科名，如Python、go
        self.path = student_path
        self.student = []

class Course:
    '''
    课程类
    '''
    def __init__(self,name,period,price,school):
        self.name = name  # 课程名
        self.period = period  # 课程周期
        self.price = price   # 课程价格
        self.school = school

class School:
    def __init__(self,name,site):
        self.name = name
        self.site = site
'''
if __name__ == '__main__':
    from conf.settings import schoolinfo
    from core.my_pickle import MyPickle
    school_pk = MyPickle(schoolinfo)
    python = Course('Python','6-mons',9999,'北京校区')
    go = Course('Go','5-mons',8888,'北京校区')
    linux = Course('Linux','5-mons',9988,'上海校区')
    Beijing = School('北京校区',[python,linux])
    Shanghai = School('上海校区',[go])
    school_pk.dump(Beijing)
    school_pk.dump(Shanghai)

    from conf.settings import courses_obj
    course_pk = MyPickle(courses_obj)
    python = Course('Python','6-mons',9999,'北京校区')
    go = Course('Go','5-mons',8888,'北京校区')
    linux = Course('Linux','5-mons',9988,'上海校区')
    course_pk.dump(python)
    course_pk.dump(go)
    course_pk.dump(linux)

'''