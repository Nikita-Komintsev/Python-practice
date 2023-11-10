import math
from abc import ABC, abstractmethod


class Shape(ABC):
    name = "Shape"

    def __init__(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Rectangle(Shape):
    name = "Rectangle"

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    name = "Triangle"

    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height


class Circle(Shape):
    name = "Circle"

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


rectangle = Rectangle(4, 5)
triangle = Triangle(3, 6)
circle = Circle(2)
shape = Shape()

print(f"{rectangle.name} - {rectangle.square()}")
print(f"{triangle.name} - {triangle.square()}")
print(f"{circle.name} - {circle.square()}")
