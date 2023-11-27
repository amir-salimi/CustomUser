FROM python:alpine3.17

# set work directory
WORKDIR /usr/src/app                                                                                                                    

# copy project
COPY ../. .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


