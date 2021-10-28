# -- coding: utf-8 --
def cut_string():
    S = str(input('Введите строку: '))
    l = len(S) // 2
    S_first = (S[-l:])
    S_second = (S[:(len(S) - l)])
    print(S_first + S_second)
cut_string()