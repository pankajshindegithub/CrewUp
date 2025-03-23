from config.db import db
 
collab = db['collab']

def add_collab(client):
    # Convert ImmutableMultiDict to a regular dictionary
    data = dict(client)

    # Insert into MongoDB
    request_id = collab.insert_one(data).inserted_id
    return {"message": "successfully sent", "id": str(request_id)}


def getCollab():
    return db['collab'].find()