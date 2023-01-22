import doctest

class Table:
    """ Класс для описания стола
    """

    def __init__(self, length: int, width: int, height: int):
        """ Конструктор

        :param length: Длина стола
        :param width: Ширина стола
        :param height: Высота стола
        :raises ValueError: Если любой из аргументов меньше или равен нулю
        """
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError('Недопустимое значение аргумента')
        if not isinstance(length, int) and not isinstance(width, int) and not isinstance(height, int):
            raise TypeError('Аргументы должны иметь тип int')

        self.length = length
        self.width = width
        self.height = height

    def get_square(self) -> int:
        """ Вычисляет площадь стола

        :return: Площадь стола
        :rtype: int
        """
        return self.length * self.width

    def get_volume(self) -> int:
        """ Вычисляет объем стола

        :return: Объем стола
        :rtype: int
        """
        return self.length * self.width * self.height

    def set_height(self, height: int) -> None:
        """ Устанавливает высоту стола

        :param height: Значение высоты стола
        :type height: int
        :raises ValueError: Если аргумент меньше или равен нулю
        """
        if height <= 0:
            raise ValueError('Недопустимое значение аргумента')
        self.height = height


class Tree:
    """ Класс для описания дерева
    """

    def __init__(self, height: int, width: int, age: int):
        """ Конструктор

        :param height: Высота дерева
        :param width: Ширина дерева
        :param age: Возраст дерева
        :raises ValueError: Если любой из аргументов меньше или равен нулю
        """
        if not isinstance(height, int) or not isinstance(width, int) or not isinstance(age, int):
            raise ValueError('Недопустимое значение аргумента')
        elif height <= 0 or width <= 0 or age <= 0:
            raise ValueError('Недопустимое значение аргумента')

        self.height = height
        self.width = width
        self.age = age

    def get_square(self) -> int:
        """ Вычисляет площадь дерева

        :return: Площадь дерева
        :rtype: int
        """
        return self.height * self.width

    def get_age(self) -> int:
        """ Возвращает возраст дерева

        :return: Возраст дерева
        :rtype: int
        """
        return self.age

    def set_height(self, height: int) -> None:
        """ Устанавливает высоту дерева

        :param height: Значение высоты дерева
        :type height: int
        :raises ValueError: Если аргумент меньше или равен нулю
        """
        if height <= 0:
            raise ValueError('Недопустимое значение аргумента')
        self.height = height



class Stack:
    """ Класс для описания стека
    """

    def __init__(self, max_size: int):
        """ Конструктор

        :param max_size: Максимальный размер стека
        :raises ValueError: Если аргумент меньше или равен нулю
        """
        if not isinstance(max_size, int):
            raise TypeError('Недопустимый тип аргумента')
        if max_size <= 0:
            raise ValueError('Недопустимое значение аргумента')

        self.max_size = max_size
        self.stack = []

    def push(self, data: any) -> any:
        """ Добавляет элемент в стек

        :param data: Элемент для добавления
        :type data: any
        :raises ValueError: Если размер стека превышает максимально допустимый
        """
        if len(self.stack) == self.max_size:
            raise ValueError('Размер стека превышает максимально допустимый')

        self.stack.append(data)

    def pop(self) -> any:
        """ Возвращает и удаляет последний элемент из стека

        :return: Последний элемент стека
        :rtype: any
        """
        return self.stack.pop()

    def peek(self) -> any:
        """ Возвращает последний элемент из стека без его удаления

        :return: Последний элемент стека
        :rtype: any
        """
        return self.stack[-1]


if __name__ == '__main__':
    doctest.testmod()