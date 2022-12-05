import pymongo

from constants import COMMAND_NOT_STARTED_STATUS


def insert_to_mongodb(command, status):
    client = pymongo.MongoClient(
        "mongodb+srv://malonso:PASSWORD@cluster0.aba4cnn.mongodb.net/?retryWrites=true&w=majority"
    )
    
    db = client.commands
    
    return db.cmd_collection.insert_one({
        'command': 'ps', 'status': COMMAND_NOT_STARTED_STATUS
    }).inserted_id.__str__()
