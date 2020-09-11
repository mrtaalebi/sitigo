FROM python:3.7

RUN mkdir /app/
WORKDIR /app/

RUN apt-get update && apt-get install -yq vim curl gettext

COPY . /app/
RUN pip3 install -r /app/requirements.txt

