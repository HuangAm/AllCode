#！/usr/bin/env python3
#-*- coding:utf-8 -*-

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#print(BASE_DIR)

if __name__ == '__main__': #  #如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行。
    from core import main
    main.login_entry()

