'''
Task # 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
'''

matrix_list = [[31, 22, 29],[37, 43, 47],[51, 86, 90]]
matrix_list2 = [[10, 12, 15],[27, 35, 38], [49, 91, 100]]

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list
        self.i = 0
    def __str__(self):
        return f'Матрица: ({self.matrix_list})'
    def __add__(self, other):
        mx3 = [[j + k for j, k in zip(h, i)]for h, i in zip(self.matrix_list, other.matrix_list)]
        return mx3
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= len(self.matrix_list):
            raise StopIteration
        value = self.matrix_list[self.i]
        self.i += 1
        return value


mx1 = Matrix(matrix_list)
mx2 = Matrix(matrix_list2)

for i in mx1:
    print(' '.join(map(str, i)))
print()
for i in mx2:
    print(' '.join(map(str, i)))
print()
for i in (mx1 + mx2):
    print(' '.join(map(str, i)))
'''
Task # 2
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
'''
from abc import ABC, abstractmethod
class Garment(ABC):
    def __init__(self, volume, height):
        self.V = volume
        self.H = height
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def suit(self):
        pass

class Clothes(Garment):
    @property
    def coat(self):
        self.outlay = self.V / 6.5 + 0.5
        return round(self.outlay, 2)
    @property
    def suit(self):
        self.outlay = 2 * self.H + 0.3
        return round(self.outlay, 2)
    def __add__(self, other):
        return Clothes(self.outlay + other.outlay, self.outlay + other.outlay)

c = Clothes(50, 175)
print(c.coat)
print(c.suit)
print(c.coat + c.suit)
'''
Task # 3
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
'''
class Cell:
    def __init__(self, mesh):
        self.mesh = mesh
    def __str__(self):
        self.mesh *= "*"
        return f'ячейки: {self.mesh}, кол-во ячеек: {len(self.mesh)}'
    def __add__(self, other):
        return f'Сложение: {Cell(self.mesh + other.mesh)}'
    def __sub__(self, other):
        sub = self.mesh - other.mesh
        if sub > 0:
            return f'Вычитание: {Cell(sub)}'
        else:
            return f'Вычитание: отрицательный результат!'
    def __mul__(self, other):
        return f'Умножение: {Cell(int(self.mesh * other.mesh))}'

    def __truediv__(self, other):
        return f'Деление: {Cell(round(self.mesh // other.mesh))}'
    def make_order(self, cells):
        for i in range(1, int(cells) + 1):
            row = (int(cells) // 5) - 1
            row2 = int(cells) - ((int(cells) // 5) * 5)
            if cells % 5 == 0:
                i = row * (f'\\n{"*" * 5}')
                row3 = f'{"*" * 5}{i}{"*" * row2}'
                return row3
            else:
                i = (int(cells) // 5) * (f'{"*" * 5}\\n')
                row3 = f'{i}{"*" * row2}'
                return row3

c = Cell(9)
с2 = Cell(3)
print(c + с2)
print(c - с2)
print(c / с2)
print(c * с2)
print(c.make_order(15))
print(c.make_order(12))
