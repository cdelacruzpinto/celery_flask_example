from celery import Celery

from dotenv import load_dotenv
load_dotenv()

app = Celery('tasks', broker='pyamqp://guest@rabbitmq/')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y


@app.task
def get_dict():
    return {"result":"RENDERED_OK"}
