'''
Task # 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
'''
from itertools import cycle
from time import sleep
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    def running(self):
        for color in cycle(TrafficLight.__color):
           if color == 'красный':
               print('красный')
               sleep(7)
           elif color == 'желтый':
               print('желтый')
               sleep(2)
           elif color == 'зеленый':
               print('зеленый')
               sleep(6)
t = TrafficLight()
t.running()
'''
Task # 2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
'''

length = int(input('Введите, длину дороги, в метрах:'))
width = int(input('Введите, ширину дороги, в метрах:'))
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def asphalt(self):
        return f'Масса асфальта, в тоннах: {(self._length * self._width * 25 * 1 * 5) /1000:.2f}'
r = Road(length, width)
print(r.asphalt())
'''
Task # 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
'''
salary = {'123': {'wage': 30000, 'bonus': 10000}, '124': {'wage': 40000, 'bonus': 5000, }}
personal_data = {'123': {'surname': 'Сидоров', 'name': 'Сидор', 'position': 'менеджер'}, '124': {'surname': 'Орешкин', 'name': 'Орех', 'position': 'главный менеджер'}}

class Worker:
    def __init__(self, name, surname, position):
       self.name = name
       self.surname = surname
       self.position = position
class Position(Worker):
    __income = salary
    def get_full_name(self):
        for key, value in personal_data.items():
            if personal_data[key]['name'] == self.name:
                if personal_data[key]['surname'] == self.surname:
                    if personal_data[key]['position'] == self.position:
                        self.key = key
                        return f'{self.name} {self.surname}'
                        return f'{self.key}'
    def get_total_income(self):
        for key in self.__income.keys():
            if key == self.key:
                return self.__income[key]['wage'] + self.__income[key]['bonus']

p = Position('Сидор', 'Сидоров', 'менеджер')
print(p.get_full_name())
print(p.get_total_income())
'''
Task # 4
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
'''
class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction
    def show_speed(self):
        if self.is_police is True:
            print('Состоит на учете в полиции')
        elif self.is_police is False:
            print('Не состоит на учете в полиции')
        print(self.name, self.color)
        print(self.speed)
    def go(self):
        if self.speed > 0:
            print('Автомобиль начал движение')
    def stop(self):
        if self.speed <= 0:
            print('Автомобиль остановился')
    def turn(self):
        if self.direction == 'left':
            print('Повернул налево')
        elif self.direction == 'right':
            print('Повернул направо')
        elif self.direction == 'back':
            print('Движение назад')
        elif self.speed == 0:
            pass
        else:
            print('Движение прямо')
class TownCar(Car):
    def towncar(self):
        if self.speed > 60:
            print('Скорость превышена')
class SportCar(Car):
    def sportcar(self):
        if self.speed > 80:
            print('Скорость превышена')
class WorkCar(Car):
    def workcar(self):
        if self.speed > 40:
            print('Скорость превышена')
class PoliceCar(Car):
    def policecar(self):
        if self.speed > 100:
            print('Скорость превышена')
tw = TownCar(70, 'синий', 'corola', False, 'stop')
tw.show_speed()
tw.towncar()
tw.turn()
tw.go()
tw.stop()
'''
Task # 5
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
'''
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Выбрана ручка')
class Pencil(Stationery):
    def draw(self):
        print('Выбран карандаш')
class Handle(Stationery):
    def draw(self):
        print('Выбран маркер')
s = Stationery('title')
s.draw()
p = Pen(s)
p.draw()
pn = Pencil(s)
pn.draw()
h = Handle(s)
h.draw()