# -- coding: utf-8 --
def delete():
    S = str(input('Введите строку: '))
    symbol = str(input('Введите символ для удаления: '))
    print(S.replace(symbol, ''))
delete()