#Queues and Futures

#Getting values from a thread
#This is a problem for future me

"""
Queues is like leaving a message
A Future is used for synchronizing program execution 
in some concurrent programming languages. They describe an 
object that acts as a proxy for a result that is initially unknown, 
usually because the computation of its value is not yet complete.
"""

#Imports
import logging
import threading
from threading import Thread
import time
import random
from concurrent.futures import ThreadPoolExecutor #Python 3.2
from queue import Queue

#Queues
#Use Queue to pass messages back and forths

def test_que(name, que):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finished: {threadname}')
    ret = 'Hello ' + name + ' your random number is: ' + str(random.randrange(1,100))
    que.put(ret)

def queued():
    que = Queue()
    t = Thread(target=test_que,args=['Bryan', que])
    t.start()
    logging.info('Do something on the main thread')
    t.join()
    ret = que.get()
    logging.info(f'Returned: {ret}')


#Futures
#Use futures, easier and cleaner
def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    time.sleep(random.randrange(1,5))
    logging.info(f'Finished: {threadname}')
    ret = 'Hello ' + name + ' your random number is: ' + str(random.randrange(1,100))
    return ret

def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(test_future,'Bryan' + str(x)) 
            ret.append(future)
    logging.info('Do something on the main thread')
    for r in ret:
        logging.info(f'Returned: {r.result()}')


#Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')
    #queued()
    pooled()

if __name__ == "__main__":
    main()