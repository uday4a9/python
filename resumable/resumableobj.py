#! /usr/bin/env /usr/bin/python

import ftplib
import threading
import time

class Main(object):
    def __init__(self, val):
        print("Main object Created")
        self.val = val
        self._observers = []

    def register(self, pos, obj):
        print obj, " : REGISTERED"
        self._observers.append(obj)

    def unregister(self, obj):
        print obj, " : UNREGISTERED"
        ind = self._observers.index(obj)
        self._observers[ind] = None

    def monres(self):
        pass

#        for child in self._observers:
#            if child:
#                print "TIME : ",time.time()
#                time.sleep(2)
#                child.resume()
#                print "TIME : ",time.time()
#                time.sleep(1)
#                child.pause()
#                time.sleep(2)
#                child.resume()
#                time.sleep(2)
#                child.pause()
#                time.sleep(2)
#                print "STATUS : ", child.status
#                child.resume()
#

class ResumableFTP(ftplib.FTP):
    """
    Create a resumable ftp from here.
    As using generator concept from here
    """

    def __init__(self, parent, myid, instances=[], *argsn, **kwargsn):
        print("New Resumable FTP object created")


        print argsn
        print kwargsn

        self.filename = kwargsn['fname']
        self.transfer = kwargsn['transfer']

        for key in ('fname', 'transfer'):
            del kwargsn[key]

        print kwargsn

        try:
            ftplib.FTP.__init__(self, *argsn, **kwargsn)
        except Exception as emsg:
            print(threading.currentThread().getName() + " : Failure reason : " + str(emsg))
            #instances[myid] = None
            return None
        else:
            print(threading.currentThread().getName() + " : Succesfully logged in")
            instances[myid] = self

        self.totalbytes = 0

        self.PR_EVENT = threading.Event() 
        self.PR_EVENT.set()
        self.conn = None
        self.fp = None # for uploading the file data 
        self.transferprocess = None
        if self.transfer == "UL":
            self.fp = open(self.filename, "r")
        self.status = None

        self.parent = parent
        parent.register(myid, self)

    def progress(self):
        if self.transfer == "DL":
            print("Do the download related things")
            self.cwd("download")
            self.prior_download()
            self.transferprocess = self.download
        elif self.transfer == "UL":
            print("Do the upload related things")
            self.fp = open(self.filename, "r")
            self.cwd("upload")
            self.prior_upload()
            self.transferprocess = self.upload

    def do(self):
        while True:
            self.PR_EVENT.wait()
            if self.totalbytes == 0:
                print "Started the data transfer for : ", threading.currentThread().getName()
            try:
                self.transferprocess(blocksize=8000, callback=self.callb)
            except StopIteration:
                print threading.currentThread().getName(), ": file transfer completed",
                self.status = "completed"
                self.close()
                break

    def callb(self, data):
        self.totalbytes += len(data)
        #print("Data got as : {0}".format(len(data)))

    def download(self, blocksize=8192, callback=None):
        #print("downloading {0} bytes".format(blocksize))
        if self.conn:
            data = self.conn.recv(blocksize)
            if not data:
                print("File download completed succesful")
                raise StopIteration
            #print(len(data))
            if callback:
                callback(data)

    def upload(self, blocksize=8192, callback=None):
        #print("uploading {0} bytes".format(blocksize))
        if self.conn:
            data = self.fp.read(blocksize)
            if not data:
                print("File upload completed succesful")
                raise StopIteration
            self.conn.send(data)
            #print(len(data))
            if callback:
                callback(data)

    def prior_download(self):
        print("prior Downloading progress")
        self.voidcmd("TYPE I")
        cmd = "RETR {0}".format(self.filename) 
        self.conn = self.transfercmd(cmd)

    def prior_upload(self):
        print("uploading the file in progress")
        self.voidcmd("TYPE I")
        cmd = "STOR {0}".format(self.filename) 
        self.conn = self.transfercmd(cmd)

    def resume(self):
        self.PR_EVENT.set()
        print threading.currentThread().getName() , " : resumed @", time.time(),

    def pause(self):
        self.PR_EVENT.clear()
        print threading.currentThread().getName() , " : paused @", time.time(),

    def close(self):
        self.conn = None
        self.parent.unregister(self)
        print("FTP Close method invoked")

class MyGen():
    def __init__(self, limit=10):
        print("object created")
        self.limit = limit
        self.start = 0

#    def __iter__(self):
#        return self

    def next(self):
        if self.start > self.limit:
            raise StopIteration
        self.start += 1
        print self.start

#    def nextstep(self):
#        val = yield 
#        print val


def foo(inst):
    while True:
        print("Total bytes Transferred: {0}".format(inst.totalbytes))
        try:
            next(inst)
        except StopIteration:
            print("File Transfer completed")
            raise
    

if __name__ == '__main__':
    count = 5

    instances = [None for i in range(count)]
#    ftp = ResumableFTP(instances, host="202.46.23.164", user="qiplfield", passwd="field123",
#                       fname="15MB", transfer="up")

#    trd = threading.Thread(target=ResumableFTP, args=(instances,), kwargs={"host":"202.46.23.164", "user":"qiplfield", "passwd":"field123", "fname" :"15MB", "transfer":"up"})
#    trd.start()
#    trd.join()
#    print("Thread status : {0}".format(trd.isAlive()))

    one = Main(1)

    thrds = []
    for i in range(count):
        if i%2 == 0:
            thrds.append(threading.Thread(target=ResumableFTP, args=(one, i, instances, ), kwargs={"host":"202.46.23.164", "fname" :"600MB", "transfer":"UL", "user":"qiplfield", "passwd":"field123", "timeout":29}, name="loginthread_"+str(i)))
        else:
            thrds.append(threading.Thread(target=ResumableFTP, args=(one, i, instances, ), kwargs={"host":"202.46.23.164", "fname" :"600MB", "transfer":"UL", "user":"qiplfield", "passwd":"field123", "timeout":29}, name="loginthread_"+str(i)))
    
    for trd in thrds:
        trd.setDaemon(True)

    for trd in thrds:
        trd.start()

    for trd in thrds:
        trd.join(30)

    print "Login threads status : {}".format([trd.isAlive() for trd in thrds])

    print instances
    print one._observers

    # take only one instance and check for the existence of DIR and FILE
    instance = None
    for i in range(len(instances)):
        if instances[i] is not None:
            break
    instance = instances[i]

    dirstatus_failed = None
    try:
        instance.cwd("download")
    except ftplib.error_perm as emsg:
        print("Directory not found")
        dirstatus_failed = True

    # check the existence of the directory
    if dirstatus_failed:
        print("ALARM_DIR_NOT_FOUND, raise it")

    # check for the given file in directory
    lst = []
    instance.retrlines("LIST", lst.append)
    if instance.filename not in [l.split()[-1] for l in lst]:
        print("ALARM_FILE_NOT_FOUND, raise it")

    # To reach back the original / filesystem

    instance.cwd("/")
    #raw_input()
    print instances
    datathreads = []
    for instance in instances:
        if instance:
            instance.progress()
            datathreads.append(threading.Thread(target=instance.do, name="DATATHREAD_{0}".format(instances.index(instance))))

    print datathreads
    #raw_input()

    for data in datathreads:
        data.start()

    trd = threading.Thread(target=one.monres)

    for data in datathreads:
        data.join()

#


"""
    instances[0].progress()



    trd = threading.Thread(target=instances[0].do) 

    one.register(instances[0])
    trd.start()

    one.monres()

    trd.join()

    one.unregister(instances[0])

    print("Total bytes transferred : ", instances[0].totalbytes)


    #for i in range(100):
    #    next(instances[0])

#    trd = threading.Thread(target=foo, args=(instances[0],))
#    trd.start()
#    print "TIME : ",time.time()
#    time.sleep(.2)
#    print "TIME : ", time.time()
#    print("Total bytes MAIN : {0}".format(instances[0].totalbytes))
#    instances[0].notify(True)
#    time.sleep(.2)
#    print "TIME : ", time.time()
#    print("Total bytes MAIN : {0}".format(instances[0].totalbytes))
#
#    trd.join()
"""
