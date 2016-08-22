#! /usr/bin/env /usr/bin/python3

from concurrent.futures import ThreadPoolExecutor
import time

def func(x, y):
    time.sleep(3)
    return x + y

pool = ThreadPoolExecutor(max_workers = 8)
fut = pool.submit(func, 2, 4)
# runs above funciton in seperate thread 

# Below it waits for result
r = fut.result()
print("GOT:", r)
