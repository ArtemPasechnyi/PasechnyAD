# -- coding: utf-8 --
def inv():
    s = str(input('Введите строчку: '))
    h_1 = s.find('h')
    h_2 = s.rfind('h')
    s = s[h_1 + 1:h_2]
    print(s[::-1])
inv()
