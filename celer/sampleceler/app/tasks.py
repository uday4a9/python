from celery.decorators import task
import time

@task(name="start")
def validatep():
    time.sleep(10)
    return "hello"
