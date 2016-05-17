#! /usr/bin/env /usr/bin/python

import socket
import threading


class Socket(socket.socket):
    def __init__(self, ip, port):
        print("socket object created")


def messenger(conn):
    while 1:
        data = conn.recv(1024)
        data = data.strip()
        if data == "bye":
            break
        print("Cient : {1} : {1}".format(data.strip()))
        msg = raw_input("Me : ")
        conn.send(msg)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('10.252.156.97',8080))
    sock.listen(5)
    print ("Server at {0}".format(sock.getsockname()))

    while True:
        conn, addr = sock.accept()
        print("Connected by address : {0}".format(conn))
        threading.Thread(target=messenger, args=(conn, )).start()

if __name__ == '__main__':
    main()
