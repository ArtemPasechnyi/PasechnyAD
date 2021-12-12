# -- coding: utf-8 --
def swap():
    s = str(input('Введите строчку из 2-х слов: '))
    i = s.find(' ') + 1
    str_2 = s[:i]
    str_1 = s[-(len(s) - i):]
    print(str_1 + ' ' + str_2)
swap()
