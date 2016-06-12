FROM python:slim
MAINTAINER Tharyrok <dev@tharyrok.eu>

COPY ./app /app
RUN pip install -r /app/requirements.txt
WORKDIR /app
CMD python bot.py

