# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:19:26 2018

@author: hsf
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from UI_desk import *
from UI_login import *

class Desk_Window(QMainWindow, Ui_desk):
    def __init__(self, parent = None):
        super(Desk_Window,self).__init__(parent)
        self.setupUi(self)

    

class Login_Dialog(QDialog,Ui_login):
    def __init__(self, parent = None):
        super(Login_Dialog,self).__init__(parent)
        self.setupUi(self)
        
    def accept(self):
#        playername = 
        if self.client_checkbox.isChecked():
            if not self.player_text:
                QMessageBox.critical(self, u'Error', u'Please input player name!')  
#            elif 
#                QDialog.accept(self)
            else:
                QDialog.accept(self)

        elif self.server_checkbox.isChecked():
            QDialog.accept(self)

def login():
    dialog =Login_Dialog()
    if dialog.exec_():  
        return True  
    else:
        return False

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    if(login()):
        mainWindow = Desk_Window()
        mainWindow.show()
        sys.exit(app.exec_())

