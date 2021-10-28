# -- coding: utf-8 --
def sf():
    S = str(input('Введите строку: '))
    count_f = S.count('f')
    if count_f >= 2:
        arrange = S.find('f') + 1
        second_f = S.find('f', arrange)
        print(second_f)
    else:
        if count_f == 1:
            print(-1)
        else:
            print(-2)
sf()