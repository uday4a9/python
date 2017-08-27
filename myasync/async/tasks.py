class Task:
    """
        THis is the key component for processing the entire url fetcher.
    Implementation inpired from `concurrent.futures.Future`
    """
    __name__ = "Task"
    def __init__(self, coro):
        self.coro = coro
        self._status = "STARTED"
        self._id = hex(id(self))
        self.step()
    
    def __repr__(self):
        return '<{} at {} state={}>'.format(self.__name__, self._id, self._status)

    def step(self):
        try:
            f = self.coro.send(None)
        except StopIteration as exc:
            #print("COMPLEWEWEWEWE", exc.value)
            self.set_result(exc.value)
            self._status = "COMPLETED"
            return self.result() 
        except Exception:
            raise
        self._status = "RUNNING"
        f.callback = self.step
    
    def result(self):
        return self._result
    
    def set_result(self, result):
        self._result = result
