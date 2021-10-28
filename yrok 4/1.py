# -- coding: utf-8 --
def string():
    S = str(input('Введите строку: '))
    print(S[2])
    print(S[-2])
    print(S[:5])
    print(S[:-2])
    print(S[0::2])
    print(S[1::2])
    print(S[::-1])
    print(S[-1::-2])
    print(len(S))
string()