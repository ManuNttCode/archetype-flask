FROM python:3.12.0a7-bullseye

WORKDIR /code

RUN apt-get update && \
    apt-get install -y gcc libc6-dev linux-libc-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=/code/src/app.py FLASK_RUN_HOST=0.0.0.0

COPY . .

CMD ["python", "-m", "flask", "run", "--port=6060"]