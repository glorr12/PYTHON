from pymongo import MongoClient
client = MongoClient(

)

db = client["ich_edit"]
products = db["products_121225_IgorF"]

client.admin.command("ping")
print("Connection successful!")



