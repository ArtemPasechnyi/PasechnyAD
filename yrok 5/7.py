# -- coding: utf-8 --
first = int(input('введите число:'))
k = 0
while first != 0:
    second = int(input('введите число:'))
    if second != 0 and first < second:
        k = k + 1
    first = second
print('столько элементов этой последовательности больше предыдущего элемента - ',k)