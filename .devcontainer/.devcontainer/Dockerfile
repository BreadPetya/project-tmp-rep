FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && apt-get install -y git curl

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt