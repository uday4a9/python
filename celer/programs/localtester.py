from celery import Celery
import time

app = Celery("tasks",
             broker="amqp://localhost//")

@app.task
def reverse(string):
    time.sleep(2)
    return string[::-1]

