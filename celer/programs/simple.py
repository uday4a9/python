from flask import Flask, make_response, jsonify
from celery import Celery
import json
import time
import pdb
import sys 

app = Flask(__name__)

celery_config = json.loads(open("celery_config.json").read())
backend_url = celery_config["backend_url"]
app.config['CELERY_BROKER_URL'] = back_end_url
app.config['CELERY_RESULT_BACKEND'] = back_end_url

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

def run_bg_cal():
    time.sleep(1.5)
    return "Hello world"


def create_response(data, status=200):
    return make_response(jsonify(data), status)

@app.errorhandler(404)
def page_not_found(exc):
    print("exception", exc)
    return create_response({"reason": "URL NOT FOUND"}, 404)

@app.route("/")
def index():
    return "hello world"

#app.run(threaded=True)
