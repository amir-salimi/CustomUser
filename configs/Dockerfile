FROM python:alpine3.17

# set work directory
WORKDIR /app                                                                                                                    

# copy project
COPY ./.. /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]