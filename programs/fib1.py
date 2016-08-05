#! /usr/bin/env /usr/bin/python3

import sys
import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed

def fib(n):
    return 1 if n <= 2 else (fib(n-1) + fib(n-2))

assert len(sys.argv) == 2, "Pass only two arguments..."

number_of_runs = int(sys.argv[1]) 

# sequential function call
start = time.time()
for _ in range(number_of_runs):
    fib(34)
end = time.time()
print("sequential execution Took :", end - start, "sec")

# Thread execution call Always takes more time, due to GIL
# Then what is the use of threads in python
start = time.time()
tasks = []
for _ in range(number_of_runs):
    tasks.append(threading.Thread(target=fib, args=(34,)))

for task in tasks:
    task.start()

for task in tasks:
    task.join()
end = time.time()
print("multi threading execution Took :", end - start, "sec")

# multiprocessing execution call Delayed response, due to GIL
start = time.time()
tasks = []
for _ in range(number_of_runs):
    task = multiprocessing.Process(target=fib, args=(34,))

for task in tasks:
    task.start()

for task in tasks:
    task.join()
end = time.time()
print("multiprocessing execution Took :", end - start, "sec")

# Threadpoolexecutor how it works
pool = ThreadPoolExecutor(number_of_runs)

start = time.time()
futures = []
for _ in range(number_of_runs):
    futures.append(pool.submit(fib, 34))

for future in as_completed(futures):
    pass
    #print(future)

end = time.time()
print("Threadpool executor execution Took :", end - start, "sec")

# Threadpoolexecutor how it works
pool = ProcessPoolExecutor(number_of_runs)

start = time.time()
futures = []
for _ in range(number_of_runs):
    futures.append(pool.submit(fib, 34))

for future in as_completed(futures):
    pass
    #print(future)

end = time.time()
print("Processpool executor execution Took :", end - start, "sec")
