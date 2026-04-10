import logging

logging.basicConfig(
    filename="errors.log",
    format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s -%(message)s", encoding="utf-8", filemode="a",
    level=logging.ERROR
)
logging.error("Error")
logging.critical("Critical error")


def div(n1, n2) -> float:
    """
    Функция выполняет деление двух чисел с плавающей точкой.
    :param n1: Это делимое. Переменная принимает как число так и строку.
    :param n2: Это делитель. Переменная принимает как число так и строку.
    :return: Результат деления.Выводится в виде числа с плавающей точкой.
    """
    n1 = float(n1)
    n2 = float(n2)
    if n1 == 0 or n2 == 0:
        raise ZeroDivisionError("с нулём не работаем :)")

    return n1 / n2


num1 = input("Введите делимое: ")
num2 = input("Введите делитель: ")

try:
    res = div(num1, num2)
    print(f"Результат : {res}")

except ZeroDivisionError as d:
    logging.critical("Ахнутг , гений делит на 0")
    print(f"Нет нет нет, {d}")
except ValueError:
    logging.error("Алерт,алерт!Обнаружена строка в поле для интеджера")
    print("Ошибка.Введите корректные данные")