# -- coding: utf-8 --
n = int(input('минуты - '))
hour = n % (60 * 24) // 60
min = n % 60
print(hour, min)
