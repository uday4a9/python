#! /usr/bin/env /usr/bin/python3

from socket import *
import sys
import time

from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

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

    callback = lambda: connected(conn)
    selector.register(conn.fileno(), EVENT_WRITE, callback)


def connected(conn):
    print("Invoked conn")
    i, times = 0, 1
    buf = ""
    while True:
        try:
            buf = conn.recv(40)
        except BlockingIOError:
            continue 
        if not buf:
            break
        #sys.stdout.write(buf.decode())


if __name__ == '__main__':
    start = time.time()
    for _ in range(20):
        helper()

    events = selector.select()
    for key, mask in events:
        callback_fn = key.data
        callback_fn()

    print("Took {0}secs".format(time.time() - start))
