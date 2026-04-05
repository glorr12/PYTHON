


num = 43197
def sum_num(n):
    if n == 0:
        return 0
    return n % 10 + sum_num(n // 10)
print(sum_num(num))

#-------------------------------------

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def sum_nest(data):
    total = 0
    for d in data:
        if isinstance(d, list):
            total += sum_nest(d)
        else:
            total += d
    return total
print(sum_nest(nested_numbers))

#--------------------------------------

def sum_num1(n):
    return sum([sum_num1(i) if isinstance(i,list) else i for i in n])
print(sum_num1(nested_numbers))