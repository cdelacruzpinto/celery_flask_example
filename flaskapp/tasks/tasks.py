import sys
import logging

from celery import Celery
from dotenv import load_dotenv

sys.path.append('../common')
from common.jsonifier import jsonifier

load_dotenv()

app = Celery('tasks', broker='pyamqp://guest@rabbitmq/')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    j = jsonifier.Jsonifier()
    logging.error("WTF WTF WTF")
    return x + y


@app.task
def get_dict():
    j = jsonifier.Jsonifier()
    logging.error("WTF WTF WTF")
    return {"result":"RENDERED_OK"}
