# -- coding: utf-8 --
n = int(input('введите число:'))
d = 1
s = 0
while d <= n:
    d = d * 2
    s = s + 1
    if d<=n:
        print(d,s)