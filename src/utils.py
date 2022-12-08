import os
import subprocess
import pymongo

from bson.objectid import ObjectId
from dotenv import load_dotenv

from constants import COMMAND_NOT_STARTED_STATUS, COMMAND_COMPLETED_STATUS


class MongoClient:
    """ Class to encapsulate the main actions to perform on mongodb cloud
    """
    def __init__(self):
        load_dotenv()
        self.client = pymongo.MongoClient(
            os.getenv('MONGODB_URL', '')
        )
        self.db = self.client.commands

    def insert_command(self, command: str, status: str):
        """ Inser the command to execute
        """
        return self.db.cmd_collection.insert_one({
            'command': command, 'status': COMMAND_NOT_STARTED_STATUS
        }).inserted_id.__str__()

    def update_command_status(self, id: str, status: str):
        """ Update command the status of the command executed
        """
        return self.db.cmd_collection.update_one({'_id': ObjectId(id)}, {'$set': {'status': status}})
    
    def insert_command_output(self, command_output: str):
        """ Insert the result of the commands
        """
        self.db.cmd_output_collection.insert_one({
            'output': command_output,
        })

    def get_command_output_by_id(self, id: str):
        return self.db.cmd_output_collection.find_one({'_id': ObjectId(id)})


def insert_command_result_and_update_command_status(command: str, mongod_db_id: str):
    """ Task to execute async. Save the command execution result and update the status of the executed command
    """
    command_output = subprocess.run(command.split(), capture_output=True)

    mongo_client = MongoClient()
    mongo_client.insert_command_output(command_output.stdout.decode())

    mongo_client.update_command_status(mongod_db_id, COMMAND_COMPLETED_STATUS)
