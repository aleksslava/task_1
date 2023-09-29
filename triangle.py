from validator import *


class Triangle:
    def __init__(self, *args):
        val = Validator()
        val.is_valid_type(*args)
        val.is_positive_val(*args)
        val.is_triangle_valid(*args)

        self.args = args

    @classmethod
    def is_valid(cls, *args):
        if len(args) == 3:
            return True
        return False

    def is_rectangle(*args):
        """Проверка, что треугольник прямоугольный"""
        a, b, c = args
        sides = [a, b, c]
        side_max = max((a, b, c))
        sides.remove(side_max)
        return side_max ** 2 == sides[0] ** 2 + sides[1] ** 2

    def get_square(self):
        """Функция для вычисления площади треугольника"""
        a, b, c = self.args
        p = (a + b + c) / 2
        s = (((p-a) * (p-b) * (p-c)) * p) ** 0.5
        return s
