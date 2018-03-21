# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:46:03 2018

@author: hsf
"""
#import texasfunction as tf
#import texas_predict as tp
#
#player_tmp1 = tf.usr("robot1")  
#player_tmp1.handcards([39,40])
#player_tmp2 = tf.usr("robot2")  
#player_tmp2.handcards([39,46])
#player_tmp3 = tf.usr("robot3")  
#player_tmp3.handcards([39,42])
#player_tmp3.drop = 1
#player_tmp2.drop = 1
#
#
#cards=[14,15,16]
#print(tp.predict_self(player_tmp1, cards, 3, 2, 10))
#print(tp.predict_all([player_tmp1,player_tmp2,player_tmp3], cards,  10))

#ss = input("input:")
#if ss.isdigit():
#    print('%s%s' % (ss,ss))
    
import sys
from PyQt5 import QtWidgets
from desk import *

if __name__ == '__main__':
    '''
    主函数
    '''
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_()) 