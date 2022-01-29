# celery_flask_example
Example of using Celery with flask using MongoDB as result backend and RabbitMQ as broker

usage:

- Create virtualenv and install dependencies in requirements.txt
- docker-compose up -d to start all dependencies
- celery -A tasks worker --loglevel=INFO
- (in other terminal) flask run
- (in other terminal, optional) celery flower

