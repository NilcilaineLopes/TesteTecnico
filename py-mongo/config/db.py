from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:123@cluster0.j6hjk.mongodb.net/test")

db = client.user_db

collection_name = db["MongoClient"]
