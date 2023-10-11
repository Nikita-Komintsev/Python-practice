import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Перегрузка оператора сложения
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Перегрузка оператора вычитания
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    # Перегрузка оператора сравнения (равенство)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Перегрузка оператора неравенства
    def __ne__(self, other):
        return not self == other

    # Перегрузка оператора умножения на число
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    # Перегрузка оператора скалярного произведения
    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    # Получение длины вектора
    def __length__(self):
        return math.sqrt(self.x2 + self.y2)

    # Перегрузка оператора str для вывода вектора
    def __str__(self):
        return f"<{self.x}; {self.y}>"

    # Перегрузка оператора repr для отображения в интерпретаторе
    def __repr__(self):
        return f"<{self.x}; {self.y}>"

# Пример использования класса
v1 = Vector2D(2, 3)
v2 = Vector2D(1, 1)

# Сложение и вычитание векторов
result_add = v1 + v2
result_sub = v1 - v2

# Сравнение векторов
are_equal = v1 == v2

# Умножение вектора на число
scaled_vector = v1 * 2

# Скалярное произведение векторов
dot_product = v1 @ v2

# Получение длины вектора
length_v1 = v1.length()

# Вывод векторов
print("v1 + v2 =", result_add)
print("v1 - v2 =", result_sub)
print("v1 == v2?", are_equal)
print("2 * v1 =", scaled_vector)
print("v1 @ v2 =", dot_product)
print("|v1| =", length_v1)