FROM python:3.7

RUN mkdir /sitigo/
WORKDIR /sitigo/

RUN apt-get update && apt-get install -yq vim curl gettext

COPY . /sitigo/
RUN pip3 install -r /sitigo/requirements.txt

