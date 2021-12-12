# -- coding: utf-8 --
sum = 0
length = 0
n = int(input('введите число:'))
while n != 0:
    sum =sum + n
    length = length + 1
    n = int(input('введите число:'))
print('среднее значение равно:',sum / length)