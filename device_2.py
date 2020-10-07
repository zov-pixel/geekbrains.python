'''
Task # 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

number = int(input('Введите, пожалуйста, делимое:'))
number_2 = int(input('Введите, пожалуйста, делитель:'))
def device(number, number_2):
    try:
        return f'{number / number_2:.2f}'
    except ZeroDivisionError:
        return 'На ноль делить нельзя.'
print(device(number, number_2))