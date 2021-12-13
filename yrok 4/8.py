# -- coding: utf-8 --
def inv():
    s = str(input('Введите строчку: '))
    h_1 = s.find('h')
    h_2 = s.rfind('h')
    print(s[:h_1 + 1] + s[h_1 + 1:h_2][::-1] + s[h_2:])
    
inv()
