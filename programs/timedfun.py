"""
    This program trying to execute a function with in given time.
Means target method needs to execute it in mentioned timeout time.
    
To achieve this we followed Process Based model an thread based model.
1) Process based model.
    a) computation wise bit heavy.
    b) Process pool has the cappability to stop/kill the execution of 
       the process, if any process causes for timeout.
       Whole process pool is managed by underlying manager, fine grained control on
       the process is controled by manager.
2) thread based model.
    a) thread joining with timeout will work, How the process works(Above model).
    b) Even after the timeout, still the python program in wait state due to its GIL.
       More over there is no manager implemented to manage threads in python.

======  WINNER IS PROCESSBASED APPROACH =======
  As tradeoff only process based thing works, Better than the thread based model
"""

from multiprocessing import Pool
import time
import os
import multiprocessing
import threading


def fun():
    #print("PID", os.getpid())
    #os.system("ps aux | grep {0}".format(os.getpid()))
    time.sleep(4)
    return 123

def execute_process_based():
    print("Before:", time.time())
    pool = Pool(processes=1)
    res = pool.apply_async(fun,)
#    import pdb; pdb.set_trace()
    print(res)

    try:
        # Chnage the below timeoyt parameter, more than time.sleep in target method
        res.get(timeout=5)
    except multiprocessing.context.TimeoutError:
        print("EXCEPTION")

    print("After", time.time())
    print("Done with execute")

def execute_thread_based():
    trd = threading.Thread(target=fun)
    print("THREAD:", "Before:", time.time())
    trd.start()
    trd.join(2.0)
    print("THREAD:", "After:", time.time())


if __name__ == '__main__':
#    execute_thread_based()
    execute_process_based()
    print("End", time.time())
