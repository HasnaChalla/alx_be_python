import math


class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, raduis):
        super().__init__()
        self.raduis = raduis

    def area(self):
        return math.pi * self.raduis ** 2
