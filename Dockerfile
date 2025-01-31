
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=forum_app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
