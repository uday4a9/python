#! /usr/bin/env /usr/bin/python

import socket

def client():
    print("Client trying to establish new connection")
    conn = socket.create_connection(('10.252.156.97', 8080))
    conn.send("Hello buddy")
    while True:
        data =  conn.recv(1024).strip()
        if data == "bye":
            break
        print(data)


if __name__ == '__main__':
   client ()
