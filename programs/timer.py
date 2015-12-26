#! /usr/bin/env /usr/bin/python


import threading
import time


class MyTimer(threading.Thread):
    """
     Creating a timer to handle the exactly user given time
    """
    def __init__(self, duration, status=True):
        threading.Thread.__init__(self)
	self.duration = duration
	self.done = threading.Event()
	self.status = status

    def __nonzero__(self):
        """
	 When checking for the boolean status from program, It polls
	and gives the result
	"""
	return bool(self.status)

    def cancel(self):
        """
	 when ever use wants to stop it from program
	"""
        self.done.set()

    def run(self):
        self.done.wait(self.duration)
	if not self.done.is_set():
	    self.status = not self.status
        self.done.set()


def main():
    runner = MyTimer(2.0)
    runner.start()

    print "Before Time :", time.time()
    for i in range(20000):
        if not runner:
	    print "time elaspsed @", i
	    break

        if i == 30:
	   runner.cancel()
	   print "After sending the cancel to runner"
	   break

        time.sleep(0.5)
    print "After Time :", time.time()
        
if __name__ == '__main__':
    main()
