import select
import threading
from .tasks import Task
from .futures import Future

EVENT_READ = 0
EVENT_WRITE = 1

class GetEventLoop:
    """
        This will create an EventLoop, to process the event on the sockets
    """
    registry = {EVENT_READ: set(), EVENT_WRITE: set()}
    shadow_rev_lookup = {}

    def __init__(self):
        self.is_expired = False

    def run_until_complete(self, tasks):
        trd = threading.Thread(target=self._run_until_complete, 
                               args=(tasks,), 
                               daemon=True)
        trd.start()

    def get_read_event_list(self):
        return list(self.registry[EVENT_READ])

    def get_write_event_list(self):
        return list(self.registry[EVENT_WRITE])

    def _run_until_complete(self, tasks): 
        if self.is_expired:
            raise Exception("Loop Expired. Create one more loop and submit the tasks")

        while True:
            for task in tasks:
                if task._status != "COMPLETED":
                    break
            else:
                #print("Processed all tasks, So terminating the loop")
                self.close()
                return

            rlist = self.get_read_event_list()
            wlist = self.get_write_event_list()

            readable, writable, _ = select.select(rlist, wlist, [], 1.0)

            for sock in readable:
                future = sock.callb
                future.resolve()
                #self.unregister(sock)
            for sock in writable:
                future = sock.callb
                future.resolve()
                #self.unregister(sock)

    @classmethod
    def register(cls, sock, event, callback):
        setattr(sock, 'callb', callback)
        cls.registry[event].add(sock)
        cls.shadow_rev_lookup[sock] = event

    @classmethod
    def unregister(cls, sock):
        event = cls.shadow_rev_lookup[sock]
        cls.registry[event].remove(sock)

    def close(self):
        self.registry = {EVENT_READ: set(), EVENT_WRITE: set()}
        self.shadow_rev_lookup = {}
        self.is_expired = True
        
def register(sock, event, callback):
    GetEventLoop.register(sock, event, callback)

def unregister(sock):
    GetEventLoop.unregister(sock)

def as_completed(tasks):
    ltasks = set([task for task in tasks])
    #print("POLL STARTED for", tasks)
    while ltasks:
        for ind, task in enumerate(tasks):
            #print(89, len(tasks), len(ltasks), "in tasks")
            #print(tasks, ltasks)
            if task._status == "COMPLETED" and task in ltasks: 
                #print(len(tasks), len(ltasks), "in tasks")
                ltasks.remove(task)
                yield task

