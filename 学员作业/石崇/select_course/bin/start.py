#！/usr/bin/env python3
#-*- coding:utf-8 -*-
# write by congcong

# 程序入口
'''
    修改sys.path,将当前项目路径添加到sys.path列表中，使之后的模块从当前项目执行相对导入
'''
import os,sys

# BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # print(BaseDir) # D:\pycharm\Test1\Thrid_module\面向对象编程\选课系统
# sys.path.append(BaseDir)

from os import getcwd,path
from sys import path as sys_path
sys_path.insert(0,path.dirname(getcwd()))   # os.getcwd()获取当前目录，os.path.dirname()获取上一级目录


from core import main
if __name__ == '__main__':
    main.main()
