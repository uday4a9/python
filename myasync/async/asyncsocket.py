"""
 To perform the sync socket functionality, defined a new module here. 
"""

import socket

class Socket:
    """
        As part of this asynsocket, need to attach callback attribute in
    otherplaces to this socket. So, created a new socket class here.
    """
    def __init__(self):
        self._sock = socket.socket()

    def __getattr__(self, name):
        return getattr(self._sock, name)
