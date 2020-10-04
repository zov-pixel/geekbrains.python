my_list = [7, 5, 3, 3, 2]
next_number = int(input('Введите, пожалуйста, число:'))

for i in my_list:
    if my_list.count(next_number) > 0:
        next_number3 = my_list.index(next_number) + my_list.count(next_number)
        my_list.insert(next_number3, next_number)
        break
    else:
        if next_number > i:
            my_list.insert(my_list.index(i), next_number)
            break
        elif next_number < my_list[len(my_list) - 1]:
            my_list.append(next_number)
            break
print(my_list)