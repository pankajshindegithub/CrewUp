from config.db import db
 
clientRequest = db['Hire']

def add_client_Request(client):
    # Convert ImmutableMultiDict to a regular dictionary
    data = dict(client)

    # Insert into MongoDB
    request_id = clientRequest.insert_one(data).inserted_id
    return {"message": "successfully sent", "id": str(request_id)}


def getHire():
    return db['Hire'].find()