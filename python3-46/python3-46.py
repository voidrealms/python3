#Thread Locking
#Avoiding the dreaded race conditions and deadlocks
#Race condition: same resource modified by multiple threads
#Deadlock: multiple threads waiting on the same resource

"""
https://wiki.python.org/moin/GlobalInterpreterLock
https://hackernoon.com/has-the-python-gil-been-slain-9440d28fa93d

Python threads can’t run in parallel on multiple CPU cores because of the global interpreter lock (GIL).
Use Python threads to make multiple system calls in parallel. This allows us to do blocking I/O at the same time as computation.

CPython supports multiple threads within a single interpreter, but threads must request access to the 
GIL in order to execute Opcodes (low-level operations). This, in turn, means that Python developers 
can utilize async code, multi-threaded code and never have to worry about acquiring locks on any 
variables or having processes crash from deadlocks.

The GIL makes multithreaded programming in Python simple.
BUT
Also python takes a lot of flack as its not TRUE threading

If you want truly concurrent code in CPython, you have to use multiple processes.
This example shows how the GIL keeps us from crashing an app

If you want speed an power use multi-process not multi-threads
We will cover multi-processing later
"""

#Imports and globals
import logging
import threading
from concurrent.futures import ThreadPoolExecutor #Python 3.2
import time
import random

counter = 0

#Test function
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')

    for x in range(count):
        logging.info(f'Count: {threadname} += {count}')

        #The global interpreter lock (GIL) in action
        #counter += 1

        #Locking
        #lock = threading.Lock()
        #lock.acquire()
        #lock.acquire() #deadlock - waiting on resources
        #try:
        #    counter += 1
        #finally:
        #    lock.release()

        #Locking Simplified
        lock = threading.Lock()
        with lock:
            logging.info(f'Locked: {threadname}')
            counter += 1
            time.sleep(2)  


    logging.info(f'Completed: {threadname}')

#Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')

    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test,v)

    print(f'Counter: {counter}')
    logging.info('App Finished')


if __name__ == "__main__":
    main()