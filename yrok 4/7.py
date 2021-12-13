# -- coding: utf-8 --
def del_1(): 
    s = input('Введите строчку:') 
    s = s[:s.find('h')] + s[s.rfind('h') + 1] 
    print(s) 
del_1()
