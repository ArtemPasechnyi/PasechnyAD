# -- coding: utf-8 --
def fc():
    S = str(input('Введите строку: '))
    count_l = S.count('f')
    if count_l >= 2:
        print(S.find('f'), S.rfind('f'))
    if count_l == 1:
        print(S.find('f'))
    else:
        None
fc()