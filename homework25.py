
import logging

logging.basicConfig(
 filename="errors.log",
 format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s -%(message)s",
 level=logging.ERROR
)
logging.error("Error")
logging.critical("Critical error")
def div():
    try:
        num = int(input("Введите делимое: "))
        num1 = int(input("Введите делитель: "))
        if int(num) == 0 or int(num1) == 0:
            raise ZeroDivisionError("с нулём не работаем :)")
        res = int(num) / int(num1)
        return res
    except ZeroDivisionError as d:
        logging.critical("Ахнутг , гений делит на 0")
        return f"Нет нет нет, {d}"
    except ValueError:
        logging.error("Алерт,алерт!Обнаружена строка в поле для интеджера")
        return "Ошибка.Введите корректные данные"
print(div())