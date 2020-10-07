words = input('Введите, пожалуйста, слова через пробел:')
new_list = words.split()
new_list2 = new_list[:10]
for i in range(len(new_list2)):
    print(str(i + 1), new_list2[i][:10])
