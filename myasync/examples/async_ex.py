import time
import sys
from os import getcwd
from os.path import dirname
sys.path.append(dirname(getcwd()))

from async.selectors import GetEventLoop, EVENT_WRITE, EVENT_READ, as_completed
from async.tasks import Task
from async.fetcher import AsyncRequests


tasks = [Task(AsyncRequests('127.0.0.1', 5000).execute("/")) for i in range(10)]
loop = GetEventLoop()
loop.run_until_complete(tasks)

start = time.time()
for task in as_completed(tasks):
    resp = task.result()
    #print(task, "Completed, With", resp)
loop.close()
print('took %.2f seconds' % (time.time() - start))
