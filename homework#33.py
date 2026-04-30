import time

def measure_time(func):
    def wrapper():
        total_time = 0
        for _ in range(5):
            start_time = time.perf_counter()
            func()
            end_time = time.perf_counter()
            total_time += end_time - start_time
        return f"Среднее время выполнения для 5 вызовов: {round(total_time / 5, 2)}\nРезультат:{func()}"

    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total


print(compute())

# ----------------------------------------------------------------


def measure_time(repeats):
    def decorator(func):
       def wrapper():
            total_time = 0
            for _ in range(repeats):
                start_time = time.perf_counter()
                result = func()
                end_time = time.perf_counter()
                total_time += end_time - start_time
            return f"Среднее время выполнения для {repeats} вызовов: {round(total_time / repeats , 2)}\nРезультат:{result}"
       return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print(compute())