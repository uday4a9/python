#! /usr/bin/env /usr/bin/python

import socket
import threading
import Queue
import time

# Need to update the client address details
client1_address = ('10.252.156.97', 8081)
client2_address = ('10.252.156.95', 8081)

# Create two element queue, to hold the details
# master and slave ip
q = Queue.Queue(2)
D = {'10.252.156.97' : {'target' : None,
                        'data' : None},
     '10.252.156.95' : {'target' : None,
                        'data' : None}
    }
cl1ip = '10.252.156.97'
cl2ip = '10.252.156.95'

def exchange_comm():
    client1 = q.get()
    client2 = q.get()
    print client1, client2
    print("In exchange comm : {0}".format(q.qsize()))
    client1['data'], client2['data'] = client2['data'], client1['data']
    print client1, client2
    print("After exchange sending the data ")
    client1['target'].send(client1['data'])
    client2['target'].send(client2['data'])
    time.sleep(.5)
    client1['target'].send("bye")
    client2['target'].send("bye")


def receiver(conn, addr):
    print("Connection : ", conn, addr[0])
    D[addr[0]]['target'] = conn
    data = conn.recv(1024)
    D[addr[0]]['data'] = data 
    q.put(D[addr[0]])
    print("Q size :", q.qsize())

    # invoke exchange comunication b/w clients
    if q.qsize() == 2:
        exchange_comm()


def server():
    while True:
        print("server waiting for response")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('10.252.156.97',8080))
        sock.listen(5)
        print ("Server at {0}".format(sock.getsockname()))

        while True:
            conn, addr = sock.accept()
            print("Connected by address : {0}".format(addr))
            threading.Thread(target=receiver, args=(conn, addr, )).start()
        sock.close()

if __name__ == '__main__':
    # Need to run this server as daemon
    trd = threading.Thread(target=server,)
    #trd.daemon = True
    trd.start()
