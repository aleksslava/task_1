from math import pi
from validator import Validator


class Area:
    def __init__(self, radius):
        val = Validator()
        val.is_valid_type(radius)
        val.is_positive_val(radius)
        self.radius = radius

    @classmethod
    def is_valid(cls, *args):
        if len(args) == 1:
            return True
        return False

    def get_square(self):
        """Функция для вычисления площади круга"""
        s = pi * (self.radius ** 2)
        return s
