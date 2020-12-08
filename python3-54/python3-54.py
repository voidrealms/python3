#Communicating with processes
#Real time communications with processes
#Even on other machines

#Imports
import logging
import time
import multiprocessing
from multiprocessing import process
from multiprocessing.context import Process
from multiprocessing.connection import Listener, Client

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#Worker process
def proc(server='localhost',port=6000, password=b'password'):
    name = process.current_process().name
    logging.info(f'{name} stated')

    #Start listening for connections
    address = (server,port)
    listener = Listener(address,authkey=password)
    conn = listener.accept()
    logging.info(f'{name}: connection from {listener.last_accepted}')

    #Loop for input from the connected process
    while True:
        msg = conn.recv()
        logging.info(f'{name} data in: {msg}')
        if msg == 'quit':
            conn.close()
            break
    listener.close()

    logging.info(f'{name} finished')

#Main Function
def main():
    name = process.current_process().name
    logging.info(f'{name} started')

    #Setup the process
    address = 'localhost' #127.0.0.1
    port = 2823 # above 1024
    password = b'password'

    p = Process(target=proc,args=[address,port,password],daemon=True,name="Worker")
    p.start()

    logging.info(f'{name} waiting on the worker...')
    time.sleep(1)

    #Connect to the process
    dest = (address,port)
    conn = Client(dest,authkey=password)
   
    #Command loop
    while True:
        command = input('\r\nEnter a command or type quit:\r\n').strip()
        logging.info(f'{name} command: {command}')
        conn.send(command)
        if command == 'quit':
            break

    #Cleanup and shutdown
    if p.is_alive:
        logging.info(f'{name} terminating worker')
        conn.close()
        time.sleep(1)
        p.terminate()
    p.join()


    logging.info(f'{name} finished')

if __name__ == "__main__":
    main()

