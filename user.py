from config.db import db
 
user_collection = db['users']

def add_user(user_data):
    # Convert ImmutableMultiDict to a regular dictionary
    user_data = dict(user_data)

    # Insert into MongoDB
    user_id = user_collection.insert_one(user_data).inserted_id
    return {"message": "User added successfully", "id": str(user_id)}

def login(user_data):
    # Convert ImmutableMultiDict to a regular dictionary
    user_data = dict(user_data)

    # Find the user by email
    user = db['users'].find_one({"email": user_data["email"]},{"password": 0, "_id": 0})

    if user:
        return {"message": "Login successful", "user": user}
    else:
        return {"error": "Invalid email or password"}


def getUser(email):
    return db["users"].find_one({"email": email},{"password": 0, "_id": 0})