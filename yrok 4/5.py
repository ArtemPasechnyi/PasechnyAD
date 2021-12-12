# -- coding: utf-8 --
def fc():
    s = str(input('Введите строку: '))
    c = s.count('f')
    if c >= 2:
        print(s.find('f'), s.rfind('f'))
    if c == 1:
        print(s.find('f'))
    else:
        None
fc()
