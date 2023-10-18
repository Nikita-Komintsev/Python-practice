import math


class Shape:
    def __init__(self, name):
        self.name = name

    def square(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def square(self):
        return math.pi * self.radius**2

# if main -_main
rectangle = Rectangle("Rectangle", 4, 5)
triangle = Triangle("Triangle", 3, 6)
circle = Circle("Circle", 2)

print(f"{rectangle.name} S = {rectangle.square()}")
print(f"{triangle.name} S = {triangle.square()}")
print(f"{circle.name} S = {circle.square()}")
