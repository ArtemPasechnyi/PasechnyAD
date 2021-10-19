# -- coding: utf-8 --
def sum_fib():
    n = int(input('количество = '))
    first = 0
    second = 1
    sum = 1
    number = 0

    for i in range(2, n+1):
        sum += number
        number = first + second
        first, second = second, number
    print(sum)
sum_fib()