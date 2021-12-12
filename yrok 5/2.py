# -- coding: utf-8 --
n = int(input('введите число:'))
k = 2
while n % k != 0:
    k += 1
print(k)