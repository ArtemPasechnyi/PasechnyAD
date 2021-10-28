# -- coding: utf-8 --
def delete():
    S = str(input('Введите строку: '))
    first_h = S.find('h')
    second_h = S.rfind('h')
    delete = S[first_h:second_h + 1]
    print(S.replace(delete, '', 1))
delete()