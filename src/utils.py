import subprocess
import pymongo

from bson.objectid import ObjectId

from .constants import COMMAND_NOT_STARTED_STATUS, COMMAND_COMPLETED_STATUS


class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient(
            # TODO: Set a env variable for this password
            "mongodb+srv://malonso:PASSWORD@cluster0.aba4cnn.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client.commands

    def insert_command(self, command: str, status: str):
        return self.db.cmd_collection.insert_one({
            'command': command, 'status': COMMAND_NOT_STARTED_STATUS
        }).inserted_id.__str__()

    def insert_command_output(self, command_output: str):
        self.db.cmd_output_collection.insert_one({
            'output': command_output,
        })

    def find_by_id(self, id: str):
        return self.db.cmd_collection.find_one({"_id": id})

    def update_by_id(self, id: str, status: str):
        id = ObjectId(id)
        return self.db.cmd_collection.update_one({'command': 'ps'}, {'$set': {'status': status}})


def insert_command_result_and_update_command_status(command: str, mongod_db_id: str):
    command_output = subprocess.run(command.split(), capture_output=True)

    mongo_client = MongoClient()
    mongo_client.insert_command_output(command_output.stdout.decode())

    mongo_client.update_by_id(id, COMMAND_COMPLETED_STATUS)
