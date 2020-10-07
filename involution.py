'''
Task # 4
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y
'''
numb = int(input('Введите число для возведения в степень:'))
extent = int(input('Введите отрицательное значение степени:'))


def my_func(numb, extent):
    res = 1
    for i in range(abs(extent)):
        res *= numb
    if extent >= 0:
        return f'Решение № 1: {res}. Решение № 2(**): {numb**extent}.'
    else:
        return f'Решение № 1: {1 / res}. Решение № 2(**): {numb**extent}.'

print(my_func(numb, extent))
