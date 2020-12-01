#Thread Pools
#Reusing existing threads, because creating threads are expensive

#Imports
import logging
import threading
from concurrent.futures import ThreadPoolExecutor #Python 3.2
import time
import random

#Test function
def test(item):
    s = random.randrange(1,10)
    logging.info(f'Thread {item}: id = {threading.get_ident()}')
    logging.info(f'Thread {item}: name = {threading.current_thread().name}')
    logging.info(f'Thread {item}: sleeping for {s}')
    time.sleep(s)
    logging.info(f'Thread {item}: finished')

#Main function
def main():
    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)
    logging.info('App Start')

    workers = 5
    items = 15

    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(test,range(items))

    logging.info('App Finished')


if __name__ == "__main__":
    main()

