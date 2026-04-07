
import logging

logging.basicConfig(
 filename="errors.log",
 format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s -%(message)s",encoding="utf-8",filemode="a",
 level=logging.ERROR
)
logging.error("Error")
logging.critical("Critical error")
num1 = int(input("Введите делимое: "))
num2 = int(input("Введите делитель: "))
def div(num1, num2):
    try:
        if int(num1) == 0 or int(num2) == 0:
            raise ZeroDivisionError("с нулём не работаем :)")
        res = int(num1) / int(num2)
        return res
    except ZeroDivisionError as d:
        logging.critical("Ахнутг , гений делит на 0")
        return f"Нет нет нет, {d}"
    except ValueError:
        logging.error("Алерт,алерт!Обнаружена строка в поле для интеджера")
        return "Ошибка.Введите корректные данные"



print(div(num1, num2))