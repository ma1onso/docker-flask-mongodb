FROM mongo:5.0.14
WORKDIR /app
COPY . /app
RUN apt update -y
RUN apt install python3.8 python3-pip -y
RUN pip install -r requirements.txt

CMD ["flask", "--app", "src/app", "--debug", "run", "--host=0.0.0.0"]
EXPOSE 5000
