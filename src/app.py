from flask import Flask
from flask import request

from utils import MongoClient
from constants import COMMAND_NOT_STARTED_STATUS

app = Flask(__name__)

@app.route('/new_task', methods=['POST'])
def new_task():
    command = request.form.get('command')

    mongo_client = MongoClient()
    id = mongo_client.insert_command(command=command, status=COMMAND_NOT_STARTED_STATUS)

    return {'id': id}
