import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #ATM层目录
sys.path.append(BASE_DIR) #把ATM层目录加入start的sys.path里面

from core import main
if __name__ == '__main__':
    main.run()