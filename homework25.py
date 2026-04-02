
import logging

logging.basicConfig(
 filename="errors.log",
 format="%(asctime)s - %(filename)s - %(lineno)d - %(levelname)s -%(message)s",
 level=logging.DEBUG
)
logging.debug("Debug message")
logging.info("Information message")
logging.warning("Warning message")
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
        return f"Нет нет нет, {d}"
    except ValueError:
        return "Ошибка.Введите корректные данные"
print(div())