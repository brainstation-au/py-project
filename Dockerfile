FROM python:buster as prod

WORKDIR /opt/code

RUN pip install -U pip

COPY src/ src/
COPY requirements.txt setup.py README.md ./
RUN  pip install .

FROM python:buster as test

RUN apt update -y && apt install git -y

COPY ./requirements.txt ./requirements_dev.txt /tmp/

RUN pip install -r /tmp/requirements_dev.txt
