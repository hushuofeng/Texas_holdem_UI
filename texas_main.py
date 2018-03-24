# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:08:54 2018

@author: hsf
"""
import sys,Texas_UI,asyncore
from PyQt5.QtWidgets import QApplication
from chatclient import *


if __name__ == '__main__':
    '''
    主函数
    '''

    host = sys.argv[1]
    port = int(sys.argv[2])
    s = ChatClient(host, port)
    try: asyncore.loop()
    except KeyboardInterrupt: print()
    app = QApplication(sys.argv)
    if(login()):
        mainWindow = Desk_Window()
        mainWindow.show()
        sys.exit(app.exec_())