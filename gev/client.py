import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import gevent
import gevent.monkey
from gevent.pool import Pool

gevent.monkey.patch_socket()


def caller():
    url = r"http://127.0.0.1:5000/"
    return requests.get(url)

def execute_threads():
    pool = ThreadPoolExecutor(max_workers=4)
    futures = [pool.submit(caller) for _ in range(4)]

    for i in range(4):
        futures[i].name = "THREAD0" + str(i)
        futures[i].start = time.time()

    for fut in as_completed(futures):
        print(fut.name, " started @", fut.start, 
                "completed after ", time.time() - fut.start, "secs")

def execute_gevent():
    pool = Pool(4)
    futures = [pool.spawn(caller) for _ in range(4)]

    for i in range(4):
        futures[i].name = "GEV0" + str(i)
        futures[i].start = time.time()

    for fut in gevent.joinall(futures):
        print(fut.name, " started @", fut.start, 
                "completed after ", time.time() - fut.start, "secs")


execute_threads()
execute_gevent()

