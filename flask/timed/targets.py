import os
import time

def funtarget(secs):
    print("fun_target :", os.getpid())
    time.sleep(secs)
    return {"status":True, "message": "success"}
