#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

import sys
import os
import logging

userinfo = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\userinfo'
teacher_obj = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\teacher_obj'
student_obj = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\student_obj'
schoolinfo = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\schoolinfo'
courses_obj = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\courses_obj'
classes_obj = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\classes_obj'
student_info = r'D:\pycharm\Test1\Thrid_module\面向对象编程\select_course\db\student_info'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 默认管理员账户
ADMIN_USENAME = 'admin1'
ADMIN_PWD = 111

# 允许尝试登录次数
LOGIN_TRY = 3

