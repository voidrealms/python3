#TCP Client
#Intro to networking concepts

"""
TCP (Transmission Control Protocol) - is a standard that defines how to establish
and maintain a network conversation through which application programs can
exchange data. TCP works with the Internet Protocol (IP), which defines how 
computers send packets of data to each other. Uses a 3 way hand shake
c > syn
s < syn/ack
c > ack


Server - listens for incomming connections via TCP

Client - connects to the server via TCP

Network - A network consists of two or more computers that are linked

IP - The number that represents the machine on the network (IP4 vs IP6)

Port - A communication end point

Protocol - Defined means of application communictions
"""

#Includes
import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

#TCP Client
def download(server,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (server,port)
    logging.info(f'Connecting to: {server}:{port}')

    s.connect(address)
    logging.info('Connected')

    logging.info('Send')
    s.send(b'Hello\r\n')

    logging.info('Recv')
    data = s.recv(1024)

    logging.info('Closing')
    s.close()

    logging.info(f'Data: {data}')

#Main Function

def main():
    download("voidrealms.com",80)

if __name__ == "__main__":
    main()
