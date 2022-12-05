# docker-flask-mongodb

## Preparation
- Create a .env file into src folder, and put the mongodb password

## Build project

docker build -t doflamon .

## Run project

docker run -p 5000:5000 doflamon
