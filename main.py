# Задание 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width * self.height == other.width * other.height

    def __add__(self, other):
        return self.width + self.height + other.width + other.height

    def __mul__(self, num):
        return (self.width * self.height) * num

rect_1 = Rectangle(10, 20)
rect_2 = Rectangle(10, 20)

print("Задание 1\n")

print(rect_1.__eq__(rect_2))
print(rect_1.__add__(rect_2))
print(rect_1.__mul__(2))
print(rect_2.__mul__(3), '\n')

# Задание 2
class TrueFraction:
    def __init__(self, num):
        self.num = num

    def __eq__(self, other):
        return self.num == other.num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - self.num

    def __mul__(self, other):
        return self.num * other.num

numerator = TrueFraction(10)
denomerator = TrueFraction(5)

print("Задание 2\n")

print(numerator.__eq__(denomerator))
print(numerator.__add__(denomerator))
print(numerator.__sub__(denomerator))
print(numerator.__mul__(denomerator))