import pymongo
from bson.utils import 

client = pymongo.MongoClient(
    "mongodb+srv://abuzer33:Asude1608.@cluster0.wqgsj.mongodb.net/")

db = client.class4

client.sta

print(db.my_collection.insert_one(
    {"_id": "2", "name": "Abuzer Alaca", "no": "13"}).inserted_id)

for user in db.users.find():
    print(user)

# db.my_collection.insert_one({"_id": 1, "name": "Abuzer Alaca", "no": 13})

# print(db.name)
#  db.my_collection.find_one()
