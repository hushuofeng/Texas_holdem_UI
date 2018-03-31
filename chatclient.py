# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:01:40 2018

@author: hsf
"""

from asyncore import dispatcher
from errno import *
import sys
import socket, asyncore

class  ChatClient(dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
    
    def connect(self, address):
        self.connected = False
        self.connecting = True
        print('timeouterror')
        self.socket.settimeout(1)
        err = self.socket.connect_ex(address)
        self.socket.settimeout(None)
        if err == 10035:
            raise OSError(err)
        
        if err in (EINPROGRESS, EALREADY, EWOULDBLOCK) \
        or err == EINVAL and os.name == 'nt':
            self.addr = address
            return
        if err in (0, EISCONN):
            self.addr = address
            self.handle_connect_event()
        else:
            raise OSError(err, errorcode[err])
        
    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192).decode())
        
    def writable(self):
        if(sys.stdin):
            self.messages = sys.stdin.readline().strip('\n')
        return (len(self.messages) > 0)

    def handle_write(self):
        if len(self.messages) > 0: 
            sent = self.send((self.messages + '\r\n').encode())
            print("sender write",sent)
#            self.messages = self.messages[sent:]

if __name__ == '__main__':
    if(len(sys.argv) < 3) :
        print('Usage : python chat_client.py hostname port')
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    s = ChatClient(host, port)
    try: asyncore.loop()
    except KeyboardInterrupt: print()
