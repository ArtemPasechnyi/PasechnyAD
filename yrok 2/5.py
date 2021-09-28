# -- coding: utf-8 --
def m():
    a = int(input('Введите первое число - '))
    b = int(input('Введите второе число - '))
    c = int(input('Введите третье число - '))
    return min(a,b,c)
print('Минимальное число - ', m())
