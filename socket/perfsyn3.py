#! /usr/bin/env /usr/bin/python3

from socket import *
import sys
import time

from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

msg = "Fetching info from server."

def helper():
    #conn = create_connection(('localhost', 25000))
    conn = socket(AF_INET, SOCK_STREAM, 0)
    # Asyncio can apply only on non-blocking sockets
    conn.setblocking(False)

    # By making socket as non-blocking, it'll fail at below point
    # with below blocking exception
    try:
        conn.connect(('localhost', 25000))
    except BlockingIOError:
        pass
    # In above case, If an exception occurs then
    # that leads to fail at following send (or) recv methods.
    # So, We need to choose them carefully with select call

    selector.register(s.fileno(), EVENT_WRITE, callback)



    i, times = 0, 1
    while True:
        buf = conn.recv(40)
        if not buf:
            break
        #sys.stdout.write(buf.decode())


if __name__ == '__main__':
    start = time.time()
    helper()
    helper()
    print("Took {0}secs".format(time.time() - start))
