# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:19:26 2018

@author: hsf
"""

import sys
from PyQt5.QtWidgets import *
from UI_desk import *
from UI_login import *
from chatclient import *
from chatserver import *
import re

global s
class Desk_Window(QMainWindow, Ui_desk):
    def __init__(self, parent = None):
        super(Desk_Window,self).__init__(parent)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.Menu_New)
        self.actionConnect.triggered.connect(self.Menu_Connect)
    
    def __judge_legal_ip(self,one_str):  
        ''''' 
        正则匹配方法 
        判断一个字符串是否是合法IP地址 
        '''
        compile_ip=re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')    
        if compile_ip.match(one_str):    
            return True    
        else:    
            return False 
        
    def Menu_New(self):
        self.client = ChatServer(5005, 'TestChat')
        name, ok = QInputDialog.getText(self, 'Player', '输入name：')
        pass
    
    def Menu_Connect(self):
        ip, ok = QInputDialog.getText(self, 'Server', '输入服务器IP：')
        if ok:
            if not self.__judge_legal_ip(ip):
                QMessageBox.critical(self, u'Error', u'IP is illegal!')
                self.Menu_Connect()
            else :
                try :
                    self.client = ChatClient(ip, 5005)
                except OSError as e:
                    QMessageBox.critical(self, u'Error', u'Server is not available!')
                    self.Menu_Connect()
            name, ok = QInputDialog.getText(self, 'Player', '输入name：')

                    
            

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = Desk_Window()
    mainWindow.show()
    sys.exit(app.exec_())

