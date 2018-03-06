

from core import main
from conf import setting,display


if __name__ == "__main__":
    while True:
        print(display.index_default_menu.format(setting.DATE, setting.WEEK))
        option = input('>>>>:').strip()
        if option == '1':
            main.run('person')
        elif option == '2':
            main.run('manager')
        elif option == '3':
            print('The ATM program end')
            break
