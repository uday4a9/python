#! /usr/bin/env /usr/bin/python

import socket
import threading
import select


class Socket(socket.socket):
    def __init__(self, ip, port):
        print("socket object created")

def writer(conn):
    while True:
        msg = raw_input("Me : ")
        conn.send(msg)

def messenger(conn):
    threading.Thread(target=writer, args=(conn,)).start()
    while 1:
        ip, op, excp = select.select([conn], [conn], [])
        if ip:
            #conn.send(msg)
            print("Sent")
        if op:
            data = conn.recv(1024)
            data = data.strip()
            if data == "bye":
                break
            print("Cient : {0}".format(data.strip()))
    conn.close()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('10.252.156.97',8080))
    sock.listen(5)
    print ("Server at {0}".format(sock.getsockname()))

    conn, addr = sock.accept()
    print("Connected by address : {0}".format(conn))
    messenger(conn)

if __name__ == '__main__':
    main()
