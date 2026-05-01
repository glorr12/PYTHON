class Rectangle:
    def __init__(self, width: int | float, height: int | float) -> None:
        """Инициализация прямоугольника с проверкой типов"""
        self.width = width
        self.height = height
    def get_area(self) -> int | float:
        """
        Метод возвращает площадь прямоугольника
        :return: вычисление площая прямоугольника
        """
        return self.width * self.height

s = Rectangle(10, 2)
print(f"Площадь:{s.get_area()}")
s.width, s.height  = 7, 5
print(f"Новая площадь:{s.get_area()}")



# -------------------------------------------------------

class Counter:
    def __init__(self, value: int = 0):
        """Инициализирует счетчик с начальным значением - 0"""
        self.value = value
    def increase(self):
        """Увеличививает значение счетчика на 1 и выводит результат"""
        self.value += 1
        return f"Значение увеличено, текущее: {self.value}"
    def decrease(self):
        """Уменьшает значение счетчика на 1 и выводит резульат"""
        self.value -= 1
        return f"Значение уменьшено, текущее: {self.value}"
    def current_counter(self):
        """Выводит текущее значение счетчика"""
        return f"Текущее значение: {self.value}"

s = Counter()
print(s.increase())
print(s.increase())
print(s.increase())
print(s.decrease())
print(s.current_counter())