class InvalidSizeError(ValueError):
    pass

class Shape :
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        if radius <= 0:
            raise InvalidSizeError(f"Радиус должен быть положительным")
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,width,height):
        if width <= 0 or height <= 0:
            raise InvalidSizeError(f"Размеры должны быть положительными")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(3), Rectangle(3, 5)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")

try:
    zero_circle = Circle(0)
except InvalidSizeError as e:
    print(e)

try:
    zero_rect = Rectangle(0,0)
except InvalidSizeError as e:
    print(e)