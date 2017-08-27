from .asyncsocket import Socket
from . import selectors
from async.selectors import EVENT_READ, EVENT_WRITE
from .futures import Future
from .httpadapters import HttpResponse


class AsyncRequests:
    def __init__(self, host, port=80, **kwargs):
        self.host = host 
        self.port = port

    def execute(self, path="", method="GET"):
        s = Socket()
        s.setblocking(False)
        try:
            s.connect((self.host, self.port))
        except BlockingIOError:
            pass

        f = Future()
        selectors.register(s, EVENT_WRITE, f)
        yield f

        selectors.unregister(s)
        s.send(('GET %s HTTP/1.0\r\n\r\n' % path).encode())
        buf = []

        while True:
            f = Future()
            selectors.register(s, EVENT_READ, f)
            yield f

            selectors.unregister(s)
            chunk = s.recv(1000)
            if chunk:
                buf.append(chunk)
            else:
                break
        final = (b''.join(buf))#.decode("utf-8")

        return HttpResponse(final)
