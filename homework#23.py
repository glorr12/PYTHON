from typing import Any

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]


def joining(data: Any) -> str:
    """
    Функцию, которая принимает список любых данных (строки, числа, списки, словари)
    и возвращает их строковое представление, объединённое через " | ".
    :param data - Список любых данных
    :return: Строковое представление, объединённое через " | "
    """

    return " | ".join([str(el) for el in data])


print(joining(data))

# ----------------------------------------

data = [

    {"name": "Alice", "scores": [10, 20, 30]},

    {"name": "Bob", "scores": [5, 15, 25]},

    {"name": "Charlie", "scores": [7, 17, 27]}

]


def sum_grade(objects: list[dict]) -> int:
    """
    Функция, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов
    :param objects: Принимает список словарей и суммирует баллы
    :return: Возвращает сумму всех чисел
    """
    result = map(lambda x: sum(x["scores"]), objects)
    return sum(result)


print(f"Сумма всех баллов:", sum_grade(data))
