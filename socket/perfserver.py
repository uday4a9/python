#! /usr/bin/env /usr/bin/python

"""
    This simply run a server program to send "hello world" for whole 1 sec.
This program helps to debug performanceIO.py program. 
"""

from socket import *
import time
import threading

def connectionserve(conn):
    i = 0
    while i < 50:
        conn.send("Hello world! ")
        time.sleep(0.02)
        i += 1
    conn.send("\n")
    conn.close()

def server():
    sock = socket(AF_INET, SOCK_STREAM, 0)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('localhost', 25000))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        print("Connected by address : {0}".format(addr))
        trd = threading.Thread(target=connectionserve, args=(conn,))
        trd.start()

if __name__ == '__main__':
    server()
