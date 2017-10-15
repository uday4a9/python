from flask import Flask, jsonify, make_response
import multiprocessing
import os
import time

from procpool import funpool 
from targets import funtarget

app = Flask(__name__)

def create_response(data, status_code=200):
    return make_response(jsonify(data), status_code)

@app.route("/fun/<int:timeout>")
def fun(timeout):
    """
    if timeout < 5, This method responds with status as True 
    else, returns status as False.
    """
    pool = funpool()
    print("Got the pool", pool, os.getpid())

    async_resp = pool.apply_async(funtarget, (timeout,))

    try:
        res=async_resp.get(timeout=5)
    except multiprocessing.context.TimeoutError:
        print("EXCEPTION")
        return create_response({"status": False}, 404)

    print("After", time.time())
    print("Done with execute")

    return create_response(res)

if __name__ == '__main__':
    app.run(threaded=True)

