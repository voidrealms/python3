#Intro to Multiprocessing
#Multiple processes running the same script!
#This is VERY different than threading
#Each process has its own memory space, and its own threads!

#Imports
import logging
import multiprocessing
from multiprocessing import process
import time

#Process starting function
def run(num):
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')
    time.sleep(num * 2)
    logging.info(f'Finished {name}')


#Basic process usage

def main():
    #logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
    name = process.current_process().name
    logging.info(f'Running {name} as {__name__}')

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run,args=[x],daemon=True)
        processes.append(p)
        p.start()

    #wait for the processes
    for p in processes:
        p.join()

    logging.info(f'Finished {name}')

logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
if __name__ == "__main__":
    main()