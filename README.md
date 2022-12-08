# docker-flask-mongodb

## Preparation
- Create a .env file into src folder, and put your own mongodb cluster information (from https://cloud.mongodb.com), using the name: MONGODB_URL.
Example:
MONGODB_URL="mongodb+srv://USER:PASSWORD@cluster0.aba4cnn.mongodb.net/?retryWrites=true&w=majority"

## Build the project

docker build -t doflamon .

## Run the project

docker run -p 5000:5000 doflamon

## Authorize IP address from MongoDB
If you have problems to connect to mongodb cloud, check if you need to approved you IP address on the mongodb webpage.
