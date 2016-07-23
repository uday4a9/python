#! /usr/bin/env /usr/bin/python

from Queue import Queue
import pyos

class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = pyos.Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid
    
    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)

    def exit(self, task):
        print "Task {0} terminated".format(task.tid)
        del self.taskmap[task.tid]

def foo():
    for i in range(5):
        print "I'm foo"
        yield
#    while True:
#        print "I'm foo"
#        yield
#

def bar():
    for i in range(7):
        print "I'm bar"
        yield
#    while True:
#        print "I'm bar"
#        yield
#
if __name__ == '__main__':
    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()
