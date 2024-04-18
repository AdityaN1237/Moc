from pymongo import MongoClient

host = "localhost"
port = 27017
try:
    client = MongoClient(host,port)
except:
    print("connection failed")
    
db = client["school"]
collection = db["class"]


""" insert operation """
# doc = {"name": "student0", "class": 12, "roll-no": 1, "division": "A", "attendance": 75}
# insert = collection.insert_one(doc)
# print("inserted", insert.inserted_id)


""" read operation """
# find = {"name": "student0"}
# read = collection.find_one(find)
# print(read)


""" update operation """
# query = {"name": "student0"}
# values = {"$set": {"division": "C"}}
# update = collection.update_one(query,values)
# print("updated", update.acknowledged)


""" delete opetation """
# query = {"name": "student0"}
# delete = collection.delete_one(query)
# print("deleted", delete.deleted_count)