#! /usr/bin/env /usr/bin/python

import threading
import time

exit = False

def main():
    print("In main program")
    for i in range(1, 6):
        if exit: break
        print("fun value : {0}".format(i))
        time.sleep(1)

def foo():
    global exit
    print("timer thread elapsed")
#    exit = True


if __name__ == '__main__':
    timer = threading.Timer(8, foo)
    timer.start()
    print("Hello world")
    #mt = threading.Thread(target=main, name="Main")
    #mt.start()
    print('timer state : {0}'.format(timer.is_alive))
    #timer.cancel()
    

