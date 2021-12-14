# -- coding: utf-8 --
def last():
    a = 1
    b = 0
    k = 0
    while True:
        i = int(input("Введите число:"))
        if i == 0:
            break
        if (k != 0):
            if (i == p):
                a = a + 1
            else:
                if (b < a):
                    b = a
                a = 1
        p = i
        k = k + 1
    print(max(b, a))
last()
