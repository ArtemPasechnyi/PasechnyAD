# -- coding: utf-8 --
def sf():
    s = str(input('Введите строчку: '))
    c = s.count('f')
    if c >= 2:
        a = s.find('f') + 1
        f_2 = s.find('f', a)
        print(f_2)
    else:
        if c == 1:
            print(-1)
        else:
            print(-2)
sf()
