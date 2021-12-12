# -- coding: utf-8 --
def d():
    s = str(input('Введите строчку: '))
    h_1 = s.find('h')
    h_2 = s.rfind('h')
    delete = s[h_1:h_2 + 1]
    print(s.replace(delete, '', 1))
d()
