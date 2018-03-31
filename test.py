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
    
import socket
from errno import *
socket.setdefaulttimeout(0.01)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try:
#    sock.connect(("192.168.1.211", 5005))
#except socket.timeout as e:
#    print("timeout")
#    pass


err = sock.connect_ex(("192.168.1.211", 5005))
print(err)
if err == EWOULDBLOCK:
    print('1')