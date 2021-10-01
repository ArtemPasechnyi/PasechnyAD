# -- coding: utf-8 --
def schet():
    print("Введите 3 целых числа")
    a = int(input())
    b = int(input())
    c = int(input())
    k = 0
    if a == b and b == c:
        return '3 числа'
    elif a == b or b == c:
        return '2 числа'
    else:
        return '0 чисел'
print (schet())