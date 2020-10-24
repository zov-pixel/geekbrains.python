'''
Task loto. Частично(создание карточек).
loto.txt, loto1.txt - файлы карточек(игрока и компьютера соответственно).
'''

import random
def elem_card():
    num = []
    st1 = []
    st2 = []
    st3 = []
    key = ['', ' ', '  ', ' ', '']
    random.shuffle(key)
    while len(num) < 15:
        elem = random.randint(1, 90)
        if elem not in num:
            num.append(elem)
    st1.append(sorted(num[:5]))
    st2.append(sorted(num[5:10]))
    st3.append(sorted(num[10:]))
    data = ' '.join(list(map(str, sum((list(map(list, zip(sum(st1, []), key)))), []))))
    data1 = ' '.join(list(map(str, sum((list(map(list, zip(sum(st2, []), key)))), []))))
    data2 = ' '.join(list(map(str, sum((list(map(list, zip(sum(st3, []), key)))), []))))
    return f'{"-"*23}\n{data}\n{data1}\n{data2}\n{"-"*23}'

with open("loto.txt", 'a', encoding='utf-8') as f_obj:
    f_obj.writelines('Карточка игрока:')
    f_obj.writelines('\n')
    f_obj.writelines(elem_card())
with open("loto1.txt", 'a', encoding='utf-8') as f_obj:
    f_obj.writelines('Карточка компьютера:')
    f_obj.writelines('\n')
    f_obj.writelines(elem_card())
with open("loto.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line, end='')
print()
with open("loto1.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        print(line, end='')
