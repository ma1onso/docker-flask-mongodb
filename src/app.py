from flask import Flask
from flask import request

from utils import insert_to_mongodb
from constants import COMMAND_NOT_STARTED_STATUS

app = Flask(__name__)

@app.route('/new_task', methods=['POST'])
def new_task():
    command = request.form.get('command')
    id = insert_to_mongodb(command=command, status=COMMAND_NOT_STARTED_STATUS)

    return {'id': id}

