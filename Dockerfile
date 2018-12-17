    FROM python:3.6-alpine
WORKDIR /usr/src/app

RUN pip install Flask
RUN pip install flask-cors
RUN pip install flask-swagger-ui

COPY app .

EXPOSE 5000

CMD ["python", "./slackbotapp.py"]