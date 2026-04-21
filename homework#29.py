def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#----------------------------------------------
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]
def unique2(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

for i in unique2(data):
    print(i)