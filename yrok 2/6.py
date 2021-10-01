# -- coding: utf-8 --
def dos():

    print("Введите 4 числа для клеток от 1 до 8:")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if a in range(1, 9) and b in range(1, 9) and c in range(1, 9) and d in range(1, 9):
        if (a+b+c+d) % 2 == 0:
            return 'Клетки одинаковых цветов'
        else:
            return 'Клетки разных цветов'
    else:
        return 'Введённое число должно быть от 1 до 8'
print (dos())