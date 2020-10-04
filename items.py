add_goods = input("Вы хотели бы добавить товар? Введите, пожалуйста, да или нет: ")
goods = []
if add_goods == 'да':
    while add_goods == 'да':
        number = int(input("Введите, пожалуйста, номер товара: "))
        traits = {}
        product = input("Введите, пожалуйста, название товара: ")
        traits_key1 = 'название'
        traits_value1 = product
        cost = input("Введите, пожалуйста, стоимость товара: ")
        traits_key2 = 'стоимость'
        traits_value2 = cost
        volume = input("Введите, пожалуйста, количество товара: ")
        traits_key3 = 'кол-во'
        traits_value3 = volume
        measure = input("Введите, пожалуйста, единицу измерения: ")
        traits_key4 = 'ед.измерения'
        traits_value4 = measure
        traits.update({traits_key1: traits_value1, traits_key2: traits_value2, traits_key3: traits_value3, traits_key4: traits_value4})
        add_goods = input("Вы хотели бы добавить товар? Введите, пожалуйста, да или нет: ")
        goods.append(tuple([number, traits]))
print(goods)

data = {}
for i in goods:
    for traits_key, traits_value in i[1].items():
        if traits_key in data:
            data[traits_key].append(traits_value)
        else:
         data[traits_key] = [traits_value]
print(data)