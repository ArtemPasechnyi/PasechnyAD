# -- coding: utf-8 --
n = int(input('Введите первое число - '))
m = int(input('Введите второе число - '))
k = int(input('Введите количество долек - '))
if (n * m > k and (k % m ==0 or k % n == 0)):
    print('Да')
else:
    print('Нет')