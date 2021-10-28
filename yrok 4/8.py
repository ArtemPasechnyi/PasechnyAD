# -- coding: utf-8 --
def inv():
    S = str(input('Введите строку: '))
    first_h = S.find('h')
    second_h = S.rfind('h')
    S = S[first_h + 1:second_h]
    print(S[::-1])
inv()
