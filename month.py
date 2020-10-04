month_number = int(input('Введите, пожалуйста, номер месяца в году:'))
year1 = ['зима', 'весна', 'лето', 'осень']
year2 = {'key_1': 'зима', 'key_2': 'весна', 'key_3': 'лето', 'key_4': 'осень'}


if 0 < month_number <= 2:
    print(f'Это {year2.get("key_1")}, снежная {year1[0]}, лепим снеговиков.')
elif 2 < month_number <= 5:
    print(f'Это {year2.get("key_2")}, теплая {year1[1]}, убираем пуховики.')
elif 5 < month_number <= 8:
    print(f'Это {year2.get("key_3")}, солнечное {year1[2]}, идем загорать.')
elif 8 < month_number <= 11:
    print(f'Это {year2.get("key_4")}, золотая {year1[3]},  собираем гербарий.')
elif month_number == 12:
    print(f'Это {year2.get("key_1")}, снежная {year1[0]}, лепим снеговиков.')
else:
    print(f'К сожалению, {month_number} месяца в календаре найти не удалось.')
