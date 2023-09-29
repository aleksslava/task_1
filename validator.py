class Validator:
    @staticmethod
    def is_triangle_valid(*args):
        """Проверка, что с такими сторонами можно создать треугольник"""
        a, b, c = args
        res = (a + b > c), (a + c > b), (c + b > a)
        if not all(res):
            raise ValueError("У треугольника не может быть сторон такого размера")

    @staticmethod
    def is_valid_type(*args):
        """Проверка что тип входных данных - целые или вещественные числа"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise ValueError("Неверный тип данных, допустимы только целые и вещественные числа")

    @staticmethod
    def is_positive_val(*args):
        """Проверка на положительные числа"""
        for val in args:
            if val <= 0:
                raise ValueError("Число должно быть больше нуля")

