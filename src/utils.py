import pymongo

from constants import COMMAND_NOT_STARTED_STATUS


class MongoClient:
    def __init__(self):
        self.client = pymongo.MongoClient(
            # TODO: Set a env variable for this password
            "mongodb+srv://malonso:PASSWORD@cluster0.aba4cnn.mongodb.net/?retryWrites=true&w=majority"
        )
        self.db = self.client.commands

    def insert_command(self, command, status):
        return self.db.cmd_collection.insert_one({
            'command': 'ps', 'status': COMMAND_NOT_STARTED_STATUS
        }).inserted_id.__str__()

    def find_not_execute_commands(self):
        # TODO: Set a lightweight alternative to Celery to read the MongoDB and run the commands
        return self.db.cmd_collection.find({'status': COMMAND_NOT_STARTED_STATUS})
