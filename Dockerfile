FROM python:slim as prod

WORKDIR /opt/code


FROM python:buster as test

RUN apt update -y && apt install git -y

COPY ./requirements.txt ./requirements_dev.txt /tmp/

RUN pip install -r /tmp/requirements_dev.txt
