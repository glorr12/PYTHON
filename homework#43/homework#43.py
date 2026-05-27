from connectDB import client,db,products


class Mongo:
    def __init__(self,clients,dbs,productss):
        self.client = clients
        self.db = dbs
        self.products = productss


    def delete_all(self):
        self.products.delete_many({})


    def insert_many(self,data):
        data_len = len(data)
        self.products.insert_many(data)
        print(f"добавлено {data_len} строк") # для себя
        return data_len

    def increase_price(self):
        result = self.products.update_many({},{"$mul": {"price":1.2}})
        return result.matched_count


    def find_all(self):
        return self.products.find({"price":{"$exists": True}})


if __name__ == "homework#43":
    client = Mongo(client,db,products)
client.admin.command("ping")
database = Mongo(client,db,products)
database.delete_all()
prod = ([
    {"name": "Pen", "price": 1.5, "stock": 1},
    {"name": "Notebook", "price": 3.99, "stock": 2},
    {"name": "Backpack", "price": 25.00, "stock": 3},

])

database.insert_many(prod)

print(f"prices updated for {database.increase_price()} products")

for r in database.find_all():
    print(f"{r['name']}: ${r['price']:.2f}")




