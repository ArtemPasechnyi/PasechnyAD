# -- coding: utf-8 --
n = int(input())
f = 1
s = 0
for i in range(1, n + 1):
    f *= i
    s = s + f
print(s)