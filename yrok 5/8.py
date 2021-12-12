# -- coding: utf-8 --
n = int(input('Введите число: ')) 
i=0 
second=0 
while n != 0: 
    k=n 
    n = int(input('Введите число: ')) 
    if k==n: 
        i = i + 1 
    if second<=i: 
        second=i 
    else: 
     i=0 
if second==0: print('таких чисел нет') 
else: print('число подряд идущих элементов этой последовательности равных друг другу - :',second + 1)