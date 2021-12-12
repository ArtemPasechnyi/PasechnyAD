# -- coding: utf-8 --
def cut():
    s = str(input('Введите строчку: '))
    l = len(s) // 2
    s_1 = (s[-l:])
    S_2 = (s[:(len(s) - l)])
    print(s_1 + s_2)
cut()
