from typing import Generator

def fibonacci() -> Generator[int, None, None]:
    """
    Генератор чисел Фибоначчи
    :yield: возвращает следующее число последовательности
    """
    a, b = 0, 1
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Аргументы должны быть целыми числами.')
    if a < 0 or b < 0:
        raise ValueError('Аргументы должны быть неотрицательными числами.')
    if b < a:
        raise ValueError('Второе число должно быть больше первого.')
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#----------------------------------------------
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
def unique2(items: list[int]) -> Generator [int, None, None]:
    """
    Фильтрует входящую последовательность и оставляет только уникальные элементы
    :param items: Итерируемый объект, содержащий элементы для фильтрации
    :yield: Элементы в порядке первого значения входящей последовательности
    """
    if not isinstance(items, list):
        raise TypeError('Аргумент должен быть списком.')

    if not items:
        raise ValueError("Список не может быть пустым.")

    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

try:
    for i in unique2(data):
        print(i)
except(TypeError, ValueError) as e:
    print(f"Ошибка: {e}")