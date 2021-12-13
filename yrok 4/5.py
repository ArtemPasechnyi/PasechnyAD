# -- coding: utf-8 --
def cf():
    s = input('Введите строчку: ')
    if (s.count('f') == 1):
        print(s.find('f'))
    if (s.count('f') >= 2):
        print('первый индекc: ', s.find('f'))
        print('последний индекс: ', s.rfind('f'))
cf()
