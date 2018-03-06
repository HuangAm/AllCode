#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

import pickle
from os import path,getcwd,listdir
from sys import path as sys_path
from core.my_pickle import MyPickle
from conf.settings import *
class Teacher:
    '''
    讲师类：管理班级，选择班级，查看学员，修改学员成绩
    '''
    menu = [
        ('选择班级', 'choose_class'), ('查看学生', 'show_student_list'),
        ('查看班级', 'show_classes'),('学生打分','student_grade'),
        ('修改成绩','revise_grades'),('退出', 'drop_out')
          ]  # 讲师的功能列表
    def __init__(self,name,school,*args):
        self.name = name
        self.shool = school
        self.classes = ['go1']   # 进行组合，讲师任课班级
    def show(self,pickle_file):
        '''
        读取文件并展示
        :return:
        '''
        pk_file = getattr(self,pickle_file)
        load_file = pk_file.load()
        for obj in load_file:
            for i in obj.__dict__:
                print(i,obj.__dict__[i])
            print('\n')

    def show_classes(self):
        '''
        查看管理员给老师绑定的班级
        :return:
        '''
        return {'已绑定班级：',self.classes}

    def choose_class(self):
        '''
        选择班级上课
        :return:
        '''
        for index,i in enumerate(self.classes):
            print(index,i)
            try:
                chance = input('输入选择的班级序号：').strip()
                if chance.isdigit():
                    chance = int(chance)
                    if chance >= 0 and chance<=len(self.classes):
                        clas = self.classes[chance]
                        print('你选择的班级是%s'%clas)
                        return clas
            except Exception as e:
                print('输入有误',e)

    def show_student_list(self):
        '''
        显示学生列表
        :return:
        '''
        chance = self.choose_class()
        print(chance)
        student_path = path.join(student_info)
        print(student_path)
        for file in listdir(student_path):
            print(file)
            if path.basename(file) == chance:
                print('hhh')
                # with open(file,'r',encoding='utf-8') as f:
                #     data = pickle.load(f)
                #     for stu in data:
                #         print(stu)

    def student_grades(self):
        '''
        给学员评分
        :return:
        '''
        pass
    def revise_grades(self):
        '''
        修改学员分数
        :return:
        '''
        pass
    def drop_out(self):
        exit('Bye')




# class Course:
#     '''
#     课程类
#     '''
#     def __init__(self,course_name,period,price,schoolinfo):
#         self.course_name = course_name  # 课程名
#         self.period = period  # 课程周期
#         self.price = price   # 课程价格
#         self.schoolinfo = schoolinfo # 课程所属学校
# c = Course('go','6-mons',12000,'北京')
# t = Teacher('cc','北京')
# t.course = c   # 组合（一个对象传给另一个对象的属性）
# print(t.course.period) # 调用一个对象的属性的属性，检验是否使用了组合