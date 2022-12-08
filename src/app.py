import logging
from threading import Thread

from flask import Flask
from flask import request

from utils import MongoClient, insert_command_result_and_update_command_status
from .constants import COMMAND_NOT_STARTED_STATUS

app = Flask(__name__)

@app.route('/new_task', methods=['POST'])
def new_task():
    command = request.form.get('command')

    mongo_client = MongoClient()
    id = mongo_client.insert_command(command=command, status=COMMAND_NOT_STARTED_STATUS)

    thread = Thread(target=insert_command_result_and_update_command_status, args=(command, id))
    thread.start()

    return {'id': id}


# TODO: complete this endpoint
# @app.route('/get_ouput/:id', methods=['GET'])
# def get_output(id):
#     mongo_client = MongoClient()

#     return {'output': mongo_client.get_command_output(id)}
