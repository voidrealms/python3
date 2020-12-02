#Daemon threads
#Quitting when we quit the app

#Imports
import logging
import threading
from threading import Thread, Timer
import time

#Test functions
def test():
    threadname = threading.current_thread().name
    logging.info(f'Starting: {threadname}')
    for x in range(60):
        logging.info(f'Working: {threadname}')
        time.sleep(1)
    logging.info(f'Finished: {threadname}')


def stop():
    logging.info('Exiting the application')
    exit(0)

#Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('Main thread Started')

    #Stop in 3 seconds
    timer = Timer(3,stop)
    timer.start()

    #Run a thread
    #t = Thread(target=test,daemon=False)
    t = Thread(target=test,daemon=True)
    t.start()

    logging.info('Main thread Finished')

if __name__ == "__main__":
    main()