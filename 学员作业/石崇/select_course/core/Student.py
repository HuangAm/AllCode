#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

from os import path,getcwd
from sys import path as sys_path
from conf.settings import *
from core.my_pickle import MyPickle
from core.school import *
class Student:
    '''
    学生的功能类
    交学费，选择班级，查看分数
    '''
    menu = [
        ('查看学校','show_school'),('查看班级', 'show_classes'),
        ('充值','recharge'),('缴纳学费','pay_fees'),
        ('查看分数','show_grade'),('退出', 'drop_out')
    ]  # 学生的功能列表
    def __init__(self,name,school,clas):
        self.name = name
        self.school = school
        self.clas = clas
        self.money = 0
        self.grades = []

    def show_school(self):
        '''
        查看学校
        :return:
        '''
        return {'你所在的学校信息：',self.school}

    def show_class(self):
        '''
        查看班级
        :return:
        '''
        return {'你所在的班级信息：',self.clas}

    def recharge(self):
        '''
        充值
        :return:
        '''
        exit_flag = False
        while not exit_flag:
            amount = input('输入充值金额(b退出)：').strip()
            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                self.money += amount
                print('充值成功，你充值的金额为%s'%self.money)
                student_path = path.join(student_info,str(self.clas))
                student_p = MyPickle(student_path).load()
                for student_obj in student_p:
                    if student_obj.name == self.name:
                        student_obj.money = amount
                        self.clas.edit(student_obj)
                        print('修改成功')
            elif amount.lower() == 'b' :
                exit_flag = True
            else:
                print('输入错误！')
    def pay_fees(self):
        '''
        缴费
        :return:
        '''
        pass
    def show_grades(self):
        '''
        查看分数
        '''
        pass

    def drop_out(self):
        exit('Bye')



    # def show(self,pk_file):
    #     pick_obj = getattr(self,pk_file)
    #     load_f = pick_obj.load()
    #     for obj in load_f:
    #         for i in obj.__dict__:
    #             print(i,obj.__dict__[i])
    #         print('\n')
    # def show_school(self):
    #     '''
    #     展示学校列表
    #     :return:
    #     '''
    #     self.show('school_pk_obj')
    #
    # def show_classes(self):
    #     '''
    #     展示班级列表
    #     :return:
    #     '''
    #     self.show('class_pk_obj')
    #
    # def choose_school(self):
    #     '''
    #     选择报名的学校
    #     :return:
    #     '''
    #     print('可选择的学校如下：\n')
    #     self.show_school()
    #     chance_school = input('输入学校名：').strip()
    #     school_obj = self.school_pk_obj.load()
    #     student_path = path.join(student_info, self.clas)











