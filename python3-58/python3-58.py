#UDP Sockets
#UDP does not have concepts like connections, clients, servers
#Think of UDP as anyone can shout out at any time

"""
UDP (User Datagram Protocol) is a communications protocol 
that is primarily used for establishing low-latency and 
loss-tolerating connections between applications on the internet. 
It speeds up transmissions by enabling the transfer of data before an 
agreement is provided by the receiving party.
"""

#Imports
import logging
import multiprocessing
import threading
import socket
import sys
import time

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#Socket
def make_socket(ip='localhost',port=2045,sender=False):
    proc = multiprocessing.current_process().name
    logging.info(f'{proc}: starting')

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    if sender:
        logging.info(f'{proc}: starting to send')
    else:
         logging.info(f'{proc}: binding to port')
         address = (ip,port)
         s.bind(address)

    with s:
        while True:
            if sender:
                logging.info(f'{proc}: sending...')
                s.sendto(b'Hello UDP', (ip,port))
                time.sleep(1)
            else:
                data, addr = s.recvfrom(1024)
                logging.info(f'{proc}: from {addr} = {data}')

#See it in action
def main():
    broadcaster = multiprocessing.Process(target=make_socket,kwargs={'sender':True},daemon=True,name='Broadcaster')
    listener = multiprocessing.Process(target=make_socket,kwargs={'sender':False},daemon=True,name='Listener')

    broadcaster.start()
    listener.start()

    timer = threading.Timer(5,sys.exit,[0])
    timer.start()

if __name__ == "__main__":
    main()