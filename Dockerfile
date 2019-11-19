FROM python:3.8-alpine

RUN mkdir /app

WORKDIR /app

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .

ENV FLASK_APP app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]