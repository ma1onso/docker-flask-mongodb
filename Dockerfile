FROM python:3.11.0-bullseye
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["flask", "--app", "src/app", "--debug", "run", "--host=0.0.0.0"]
EXPOSE 5000
