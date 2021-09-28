# -- coding: utf-8 --
a = int(input())
if ((a % 4 == 0) and (a % 100 != 0)) or (a % 400):
    print('да')
else:
    print('нет')
