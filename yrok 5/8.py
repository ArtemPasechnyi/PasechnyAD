# -- coding: utf-8 --
def last():
    a = 1
    b = 0
    k = 0
    while True:
        x = int(input("Введите число:"))
        if x == 0:
            break
        if (k != 0):
            if (x == p):
                a = a + 1
            else:
                if (b < a):
                    b = a
                a = 1
        p = x
        k = k + 1
    print(max(b, a))
last()
