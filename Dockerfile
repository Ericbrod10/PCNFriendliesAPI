FROM python:3.11.2
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# **Copy your Django application code into the container**
COPY . /app
