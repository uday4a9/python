from flask import Flask
from flask import jsonify
from time import sleep
import random
import functools
import threading
from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

app = Flask(__name__)

class MyReqCache:
    def __init__(self, func):
        self.func = func 
        self.cache = {}

    def __call__(self, app):
        self.args = app
        return self.ret_or_create_future() 

    def ret_or_create_future(self):
        with lock:
            if self.args not in self.cache:
                self.cache[self.args] = self.func(self.args)
        return self.cache[self.args]

def gen_rand(appid):
    #print("Generating randm value for app", appid)
    return int(random.random() * 100)

#@functools.lru_cache()
@MyReqCache
def generate_random(appid):
    print("Entering for appid", appid)
    sleep(3)
    return gen_rand(appid)

@app.route('/')
def index():
    sleep(3)
    return jsonify("Hello world")

@app.route("/fetch/<appid>")
def fetch_data(appid):
    val = generate_random(appid)
    return jsonify(str(val))
    
app.run(threaded=True)
