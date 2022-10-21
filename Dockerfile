FROM python:alpine3.16

WORKDIR /src .

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./src .
