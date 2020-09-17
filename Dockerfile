FROM python:3.8-alpine 
LABEL maintainer="sasidhar7575@outlook.com"
RUN apk update 
COPY ./src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python  app.py


