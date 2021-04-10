import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://abuzer33:Asude1608.@cluster0.wqgsj.mongodb.net")


print(client.list_database_names())
# print(db.insert_one({"_id": "1", "name": "Abuzer Alaca", "no": "13"}).inserted_id)

# db.my_collection.insert_one({"_id": 1, "name": "Abuzer Alaca", "no": 13})

# print(db.name)
#  db.my_collection.find_one()
