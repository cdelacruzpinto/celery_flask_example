from flask import Flask
from celery import Celery
from tasks.tasks import add, get_dict

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@rabbitmq:5672'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://mongo:27017'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route("/")
def hello():
    add.delay(4, 4)
    get_dict.delay()
    return "Hello, World!"

