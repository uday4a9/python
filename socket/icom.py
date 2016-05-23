#! /usr/bin/env /usr/bin/python

import socket
import threading
import select
import pickle
import sys


class Socket(socket.socket):
    def __init__(self, ip, port):
        print("socket object created")

def writer(conn):
    conn = socket.create_connection((sys.argv[1], sys.argv[2]))
    # obtain the results to be sent
    msg = pickle.dumps("Hello world")
    #send the results to the client
    conn.send(msg)
    # Send the bye statement
    msg = pickle.dumps("bye")
    conn.send(msg)

def messenger(conn):
    trd = threading.Thread(target=writer, args=(conn,))
    trd.daemon = True
    trd.start()
    while 1:
        ip, op, excp = select.select([conn], [conn], [])
        data = ""
        if op:
            data = conn.recv(1024)
            data = pickle.loads(data).strip()
            if data == "bye":
                conn.close()
                break
            print("\b" * 3 + "Cient : {0}".format(data.strip()))
    conn.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('10.252.156.97',8080))
    sock.listen(5)
    print ("Server at {0}".format(sock.getsockname()))

    conn, addr = sock.accept()
    print("Connected by address : {0}".format(addr))
    messenger(conn)
    sock.close()

if __name__ == '__main__':
    main()
