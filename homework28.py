import itertools
import sys

weekly_schedule = ({
    "Monday": ["Gym", "Work", "Read book"],

    "Tuesday": ["Meeting", "Work", "Study Python"],

    "Wednesday": ["Shopping", "Work", "Watch movie"],

    "Thursday": ["Work", "Call parents", "Play guitar"],

    "Friday": ["Work", "Dinner with friends"],

    "Saturday": ["Hiking", "Rest"],

    "Sunday": ["Family time", "Rest"]
})

iterable = itertools.cycle(weekly_schedule.items())
while True:
    key, value = next(iterable)

    while True:
        n = input("Нажмите 'Enter' для получения плана или введите 'exit' для выхода:").strip().lower()
        if n == "":
            break
        elif n == "exit":
            sys.exit()
        else:
            print("Программа поддерживает только нажатие клавиши 'Enter' или ввода 'exit' ")
    result = ", ".join(value)
    print(f"{key}: {result}")

# --------------------------------------------------------------------

fruits = ["Apple", "Banana", "Orange"]

vegetables = ["Carrot", "Tomato", "Cucumber"]

dairy = ["Milk", "Cheese", "Yogurt"]


def merged(*lst):
    return  (item.lower() for item in itertools.chain(*lst))


for item in merged(fruits, vegetables, dairy):
    print(item)

# --------------------------------------------------------------------
clothes = ["T-shirt", "Jeans", "Jacket"]

colors = ["Red", "Blue", "Black"]

sizes = ["S", "M", "L"]

def generate_combinations(*lst):
    return (" - ".join(item) for item in itertools.product(*lst))

for item in generate_combinations(clothes, colors, sizes):
    print(item)
