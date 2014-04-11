import socket  # Import socket module
import sys
from struct import *
from collections import namedtuple
import os

DATA_TYPE = 0b0101010101010101
DATA_SIZE = 64   #need to be modified

data_pkt = namedtuple('data_pkt', 'seq_num checksum data_type data')
ack_pkt = namedtuple('ack_pkt', 'seq_num zero_field data_type')

def calculate_checksum(message):
    checksum = 0
    return checksum

def pack_data(message, seq_num):
    pkt = data_pkt(seq_num, calculate_checksum(message), DATA_TYPE, message)
    packed_pkt = pack('ihh' + str(DATA_SIZE) + 's', pkt.seq_num, pkt.checksum, pkt.data_type, bytes(pkt.data,'utf-8'))
    return packed_pkt


def prepare_pkts(file_content):
    pkts_to_send = []
    seq_num = 0
    pkts_to_send.append(pack_data(file_content, seq_num))
    return pkts_to_send
    #your code here

def send_file(file_content, sock, hport):
    num_pkts_sent = 0
    pkts = prepare_pkts(file_content)
    print(file_content)

    while num_pkts_sent < len(pkts):
        sock.sendto(pkts[num_pkts_sent], hport)
        num_pkts_sent += 1
    #your code here



def main():
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12345  # Reserve a port for your service.

    s.connect((host, port))


    try:
        test_file = open('test_file.txt', 'r')
        file_content = test_file.read()
        test_file.close()
    except:
        sys.exit("Failed to open file!")


    send_file(file_content,s, (host, port))
    s.close()  # Close the socket when done


if __name__ == "__main__":
    main()


