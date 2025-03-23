from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"  # Change this if using MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["fiver"]  # Change this to your actual DB name
