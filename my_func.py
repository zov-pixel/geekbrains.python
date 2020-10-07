'''
Task # 3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


numb_1 = int(input('Введите, пожалуйста, число № 1:'))
numb_2 = int(input('Введите, пожалуйста, число № 2:'))
numb_3 = int(input('Введите, пожалуйста, число № 3:'))

def big_sum_numb(numb_1, numb_2, numb_3):
     if numb_1 + numb_3 <= numb_1 + numb_2 >= numb_2 + numb_3:
         return numb_1 + numb_2
     elif numb_1 + numb_2 <= numb_1 + numb_3 >= numb_2 + numb_3:
         return numb_1 + numb_3
     else:
         return numb_2 + numb_3
print(f'Сумма наибольших двух введенных чисел: {big_sum_numb(numb_1, numb_2, numb_3)}')