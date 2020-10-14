'''
Task # 1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка
1_task.txt
'''
data = input('Введите, пожалуйста, данные:')
new_list = []

while len(data) > 1:
    if len(data) > 1:
        new_list.append(data)
        data = input('Введите, пожалуйста, данные:')

with open("1_task.txt", 'a', encoding='utf-8') as f_obj:
    f_obj.writelines('\n'.join(new_list))
    f_obj.writelines('\n')
'''
Task # 2
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
1_task.txt
'''
with open("1_task.txt", 'r', encoding='utf-8') as f_obj:
    lines = 0
    words = 0
    for line in f_obj:
        lines += 1
        words_2 = words + len(line.split())
        print(lines, words_2)
'''
Task # 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
3_task.txt
'''
pays = []
with open('3_task.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        surname, pay = line.split()
        pay = float(pay)
        if pay < 20000.00:
            print(f'{surname} {pay}')
            pays.append(pay)
print(f'Средняя оплата: {(sum(pays)) / len(pays):.2f}')
'''
Task # 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительныедолжны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
4_task.txt, файл выложен уже измененный.
'''

data = []
with open("4_task.txt", 'r+', encoding='utf-8') as f_obj:
    for line in f_obj:
       if 'One' in line:
        numb2 = line.replace('One', 'Один')
        data.append(numb2)
       elif 'Two' in line:
           numb3 = line.replace('Two', 'Два')
           data.append(numb3)
       elif 'Three' in line:
           numb4 = line.replace('Three', 'Три')
           data.append(numb4)
       elif 'Four' in line:
           numb5 = line.replace('Four', 'Четыре')
           data.append(numb5)

with open("4_task.txt", 'w', encoding='utf-8') as f_obj:
    f_obj.writelines(data)
'''
Task # 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"5_task.txt"
'''
numbers = input('Введите, пожалуйста, числа через пробел:')
with open('5_task.txt', 'a', encoding='utf-8') as f_obj:
    f_obj.writelines(' ')
    f_obj.writelines(numbers)
with open('5_task.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        numb = sum(map(int, line.split(' ')))
        print(numb)
'''
Task # 6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий.
6_task.txt
'''
subject = []
lessons = []
with open('6_task.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        term, numb1, numb2, numb3 = line.split()
        if ':' in term:
            term1 = term.replace(':', '')
        subject.append(term1)
        if '(л)' in numb1:
            line1 = numb1.replace('(л)', '')
        elif '—' in numb1:
            line1 = numb1.replace('—', '0')
        if '—' in numb2:
            line2 = numb2.replace('—', '0')
        elif '(пр)' in numb2:
            line2 = numb2.replace('(пр)', '')
        if '(лаб)' in numb3:
            line3 = numb3.replace('(лаб)', '')
            if '(лаб).' in numb3:
                line3 = numb3.replace('(лаб).', '')
        elif '—' in numb3:
            line3 = numb3.replace('—', '0')
        line4 = int(line1) + int(line2) + int(line3)
        lessons.append(line4)
new_dict = {subject[0]: lessons[0], subject[1]: lessons[1], subject[2]: lessons[2]}
print(new_dict)
'''
Task # 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.
7_task.txt, my_file.json
'''
import json
data = []
data1 = []
company = []
profits = []
with open('7_task.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, ownership, revenue, lost = line.split()
        company.append(name)
        revenue = int(revenue)
        lost = int(lost)
        profit = revenue - lost
        profits.append(profit)
        print(name, ownership, profit)
        if revenue > lost:
            data.append(revenue - lost)
        else:
            data1.append(revenue - lost)
    print(f'Средняя прибыль, без учета компаний с убытками: {sum(data) / len(data)}')
new_dict = {company[0]: profits[0], company[2]: profits[2]}
new_dict_2 = {company[1]: profits[1], company[3]: profits[3]}
new_list = [new_dict, {'average_profit': sum(data) / len(data)}, new_dict_2, {'average_lost': sum(data1) / len(data1)}]
print(new_list)

with open('my_file.json', 'w') as write_f:
    json.dump(new_list, write_f)

