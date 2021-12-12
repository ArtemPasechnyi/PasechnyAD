# -- coding: utf-8 --
y = float(input('введите число:'))
x = float(input('введите число:'))
k = 0
if (y or x) >=0:
    while x <= y:
        if x==y:
            break
        x+=x/10
        k+=1
    print('на',k ,'день')
else:
    print('введено не коректное число')