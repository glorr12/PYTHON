orders = [

    {"product": "Laptop", "price": 1200},

    {"product": "Mouse", "price": 50},

    {"product": "Keyboard", "price": 100},

    {"product": "Monitor", "price": 300},

    {"product": "Chair", "price": 800},

    {"product": "Desk", "price": 400}

]

result = sorted(map(lambda x: x["product"], filter(lambda x: x["price"] > 500, orders)))
print(result)

# --------------------------------------------------------------
sales = [

    ("Laptop", 5, 1200),

    ("Mouse", 50, 20),

    ("Keyboard", 30, 50),

    ("Monitor", 10, 300),

    ("Chair", 20, 800)

]
new_dict = {name: count * price for name, count, price in sales}
sorted_dict = dict(sorted(new_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_dict)