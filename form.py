'''
Task # 2
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
name = input('Введите, пожалуйста, имя:')
surname = input('Введите, пожалуйста, фамилию:')
birth_year = input('Введите, пожалуйста, год рождения:')
city = input('Введите, пожалуйста, город проживания:')
email = input('Введите, пожалуйста, адрес электронной почты:')
phone = input('Введите, пожалуйста, номер телефона:')

def form(name='name', surname='surname', birth_year='birth_year', city='city', email='email', phone='phone'):
    print(name, surname, birth_year, city, email, phone)

form(name, surname, birth_year, city, email, phone)
