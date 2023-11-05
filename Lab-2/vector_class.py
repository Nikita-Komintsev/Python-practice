import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __mul__(self, scalar):
        if (type(scalar) is int) or (type(scalar) is float):
            return Vector(self.x * scalar, self.y * scalar)
        elif type(scalar) is Vector:
            return self.x * scalar.x + self.y * scalar.y
        else:
            raise Exception("Unknown argument")

    def __rmul__(self, scalar):
        return self * scalar

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"<{self.x}; {self.y}>"


v1 = Vector(1, 2)
v2 = Vector(3.1, 4)

print(f'V1 = {v1}')
print(f'V2 = {v2}')

print(f'Сложение: {v1 + v2}')
print(f'Вычитание: {v1 - v2}')
print(f'Сравнение: {v1 == v2}  {v1 != v2}')
print(f'Умножение на число: {v1 * 5}')
print(f'Умножение числа на вектор: {7 * v1}')
print(f'Скалярное произведение: {v1*v2}')
print(f'Длина v2: {abs(v2)}')
