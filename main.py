from area import Area
from triangle import Triangle


class SquareCalc:
    """Для добавления новой формы для расчета площади, добавьте новый класс фигуры в аттрибут класса 'Forms'
    В классе должны быть прописаны методы: 1) "get_square"(расчет площади фигуры),
     2) "is_valid"(проверка подходит ли фигура под аргументы)."""
    FORMS = [Area, Triangle]

    def __init__(self, *args: (int, float)):
        self.forms = [obj(*args) for obj in self.FORMS if obj.is_valid(*args)]

    def get_square(self):
        return round(self.forms[0].get_square(), 1)

    def add_form(self, obj):
        """Добавление новой фигуры для просчета площади"""
        self.FORMS.append(obj)







def test():
    form = SquareCalc(4)

    assert round(form.get_square()) == 50

    form = SquareCalc(1)
    assert round(form.get_square()) == 3

    try:
        form = SquareCalc('h')
    except ValueError:
        assert True
    else:
        assert False, "Не сгенерировалось исключение, не верный тип данных"

    try:
        form = SquareCalc(-2)
    except ValueError:
        assert True
    else:
        assert False, "Не сгенерировалось исключение, значение должно быть положительным числом"

    try:
        form = SquareCalc(0)
    except ValueError:
        assert True
    else:
        assert False, "Не сгенерировалось исключение, значение должно быть положительным числом"

    try:
        form = SquareCalc('1', 2, 5)
    except ValueError:
        assert True
    else:
        assert False, "Не сгенерировалось исключение, значения должны быть числами"

    form = SquareCalc(5, 4, 4)
    assert round(form.get_square()) == 8

    try:
        form = SquareCalc(20, 4, 4)
    except ValueError:
        assert True
    else:
        assert False, "Не сгенерировалось исключение, нельзя создать треугольник с такими сторонами"

    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    test()