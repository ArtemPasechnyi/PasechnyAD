# -- coding: utf-8 --
seconds = int(input("Введите количество секунд: "))
sec = seconds % 60
min = seconds // 60 % 60
hour = seconds // 60 // 60 % 24
day = seconds // 86400
print (day,'',hour,'',min,'',sec,)