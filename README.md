# docker-flask-mongodb

## Preparation

- Create a .env file in the src folder, and put your own mongodb cluster information (from https://cloud.mongodb.com).

Like this -> `MONGODB_URL="mongodb+srv://USER:PASSWORD@cluster0.aba4cnn.mongodb.net/?retryWrites=true&w=majority"`

- Create two collections (on https://cloud.mongodb.com:) named: **cmd_collection** and **cmd_output_collection**.

## Authorize IP address from MongoDB
If you have problems to connect to mongodb cloud, check if you need to approved you IP address on the mongodb webpage.

## Build the project

docker build -t doflamon .

## Run the project

docker run -p 5000:5000 doflamon

## Endpoints:

- `POST /new_task`: Create a new record in **cmd_collection** and save the output in **cmd_output_collection**.

- `GET /get_output/<id>`: Received a id from **cmd_output_collection** and return the output from a command.
