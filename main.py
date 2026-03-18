n = int(input())


def simp_numb(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if simp_numb(n):
    print(f"Число {n} является простым")
else:
    print(f"Число {n} не является простым")


def filter_numbers(type, *numbers):
    result = []
    if type == "even":
        for n in numbers:
            if n % 2 == 0:
                result.append(n)
        return result

    elif type == "odd":
        for n in numbers:
            if n % 2 != 0:
                result.append(n)
        return result

    else:
        return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))


def merge_dicts(group_dicts):
    result = {}
    for d in group_dicts:
        result = result | d
    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

all_dicts = [dict1, dict2, dict3]
print(merge_dicts([dict1, dict2, dict3]))
