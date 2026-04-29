def make_rounder(func):
    def round_function(num):
        return round(num,func)
    return round_function

round2 = make_rounder(2)
round0 = make_rounder(0)
print(round2(3.141591231))

print(round2(2.71828))

print(round0(9.999))


# ---------------------------------------------------
from datetime import datetime

def logger():
    data = []
    def log(data_text=None):
        if data_text:
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data.append(f"{data_text}:{time}")
        return data
    return log

log = logger()

log("Загрузка данных")

log("Обработка завершена")

log("Сохранение файла")

for event in log():

    print(event)

# ---------------------------------------------------


def frame(func):
    def wrapper():
        print("-" * 50)
        func()
        print("-" * 50)
    return wrapper

@frame
def say_hello():
    print("Привет, игрок!")

say_hello()

