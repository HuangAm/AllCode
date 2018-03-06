#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong
from os import path,getcwd
from sys import path as sys_path
from conf.settings import *
from core.Teacher import *
from core.Student import Student
from core.my_pickle import MyPickle
from core.school import *
class Admin:
    '''
    管理员类：创建讲师，创建班级，创建课程
    '''
    menu = [
        ('查看学校', 'show_school'),('创建学校','creat_school'),
        ('创建讲师','creat_teacher'),('查看讲师','show_teacher'),
        ('创建班级', 'creat_class'),('查看班级','show_classes'),
        ('创建课程', 'creat_course'),('查看课程','show_courses'),
        ('创建学生','creat_student'),('绑定班级','bound_class'),
        ('退出','drop_out')
    ]  # 管理员的功能列表
    def __init__(self,name,*args):
        '''
        管理员独有的属性
        :param name:
        '''
        self.name = name
        self.teacher_pk_obj = MyPickle(teacher_obj)
        self.class_pk_obj = MyPickle(classes_obj)
        self.course_pk_obj = MyPickle(courses_obj)
        self.school_pk_obj = MyPickle(schoolinfo)

    @staticmethod
    def userinfo_handle(insert):
        '''
        处理管理员添加的讲师等信息
        :return:
        '''
        with open(userinfo,'a',encoding='utf-8') as f:
            f.write('\n %s'%insert)

    def show(self,pickle_file):
        pk_obj = getattr(self,pickle_file)
        load_obj = pk_obj.load()
        for obj in load_obj:
            for k in obj.__dict__:
                print(k,obj.__dict__[k])
            print('\n')


    def show_school(self):
        '''
        展示学校列表
        :return:
        '''
        self.show('school_pk_obj')

    def creat_school(self):
        '''
        创建学校
        :return:
        '''
        school_name = input('学校名称：').strip()
        school_site = input('学校地址：').strip()
        #school_path = path.join(schoolinfo)
        school_obj = self.school_pk_obj.load()
        school = School(school_name, school_site)
        self.school_pk_obj.dump(school)
        print('学校创建成功')

    def show_teacher(self):
        '''
        展示讲师列表
        :return:
        '''
        self.show('teacher_pk_obj')

    def creat_teacher(self):
        '''
        输入学校，用户名，密码
        实例化讲师对象，存到讲师文件
        :return:
        '''
        teacher_name = input('讲师姓名：').strip()
        teacher_pwd = input('讲师密码：').strip()
        school = input('学校：')
        teacher_obj = self.teacher_pk_obj.load()
        insert = '%s-%s-Teacher'%(teacher_name,teacher_pwd)
        Admin.userinfo_handle(insert)
        teacher = Teacher(teacher_name,school)
        self.teacher_pk_obj.dump(teacher)
        print('讲师创建成功！')

    def creat_course(self):
        '''
        输入课程名，价格，周期
        创建课程对象，存到文件
        :return:
        '''
        self.show_school()
        school = input('学校名称：').strip()
        course_name = input('课程名：').strip()
        course_price = int(input('价格：').strip())
        course_period = input('课程周期：').strip()
        courses_obj = self.class_pk_obj.load()
        course = Course(course_name,course_period,course_price,school)
        self.course_pk_obj.dump(course)
        print('课程创建成功')

    def show_courses(self):
        '''
        打开文件，读出来展示
        :return:
        '''
        self.show('course_pk_obj')

    def creat_class(self):
        '''
        输入班级名称，学校-->属性
        绑定学科对象，先调用获取学科对象，用户选择后，将对象绑定到班级
        创建一个班级文件存储学生信息，文件路径存到班级对象中
        创建一个班级对象（名称 学校 学科对象 讲师空列表 学生信息所在文件路径）dump进class文件
        :return:
        '''
        class_name = input('班级名称：').strip()
        self.show_school()
        school = input('学校：').strip()
        self.show_courses()
        course = input('输入学科名称：').strip()
        student_path = path.join(student_info,class_name)
        open(student_path,'w',encoding='utf-8').close()
        class_obj = Classes(school,class_name,course,student_path)
        self.class_pk_obj.dump(class_obj)

    def show_classes(self):
        '''
        打开文件，将文件对象读出来展示（班级名称，人数）
        :return:
        '''
        self.show('class_pk_obj')

    def creat_student(self):
        '''
        输入学校，用户名，密码
        存到学生文件student_info
        创建一个学生对象（姓名 讲师空列表）
        :return:
        '''
        student_name = input('学员姓名：').strip()
        student_pwd = input('学员密码：').strip()
        self.show_school()
        school = input('学校：').strip()
        self.show_classes()
        student_class = input('学员班级：').strip()
        class_f = self.class_pk_obj.load()
        for clas in class_f:
            if clas.name == student_class:
                insert = '%s-%s-Student'%(student_name,student_pwd)
                Admin.userinfo_handle(insert)
                student_obj = Student(student_name,school,student_class)
                MyPickle(clas.path).dump(student_obj)
                print('学员%s创建成功'%student_name)
                break
        else:
            print('输入有误')


    def bound_class(self):
        '''
        管理员选择为老师或学生指定班级
       
        :return:
        '''
        self.show_classes()
        class_name = input('输入班级：').strip()
        self.show_teacher()
        teacher_name = input('输入讲师：')
        teacher_p = self.teacher_pk_obj.load()
        for teacher_obj in teacher_p:
            if teacher_obj.name == teacher_name:
                teacher_obj.classes.append(class_name)
                self.teacher_pk_obj.edit(teacher_obj)
                print('创建成功')


    def drop_out(self):
        exit('Bye')