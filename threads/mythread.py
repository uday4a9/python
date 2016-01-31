#! /usr/bin/env /usr/bin/python

import threading
import time

class MyThread(threading.Thread):
    """
    Creating my thread method to cancel my thread whenever it
    needed.
    """
    def __init__(self, target, *args, **kwargs):
        print "My thread instance created"
        threading.Thread.__init__(self, *args, **kwargs)
        self.status = True

    def run(self):
        while self.status:
            runner()
            time.sleep(1)
        print "Done with the thread funcationality"

    def cancel(self):
        self.status = False
        print "Just invoked the cancel method"

def runner():
    print "Runner Invoked"

if __name__ == '__main__':
    thread = MyThread(target=runner)
    print "Before"
    thread.start()
    time.sleep(5)
    print "After"
    thread.cancel()
