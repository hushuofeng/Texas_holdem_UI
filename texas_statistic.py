# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:35:42 2018

@author: hsf
"""

#from matplotlib import pyplot
#matplotlib.use('qt4agg')  
import matplotlib
#matplotlib.use('qt4agg')
import matplotlib.pyplot as ply

#指定默认字体  
matplotlib.rcParams['font.sans-serif'] = ['SimHei']   
matplotlib.rcParams['font.family']='sans-serif'  
#解决负号'-'显示为方块的问题  
matplotlib.rcParams['axes.unicode_minus'] = False  
matplotlib.rcParams["figure.dpi"] = 100 


#绘制柱状图
def bar_card_type(card_type_list, card_types):
    xticks = card_types
    cardGroup = {}
    #对每一类成绩进行频数统计
    for i in card_type_list:
        cardGroup[i] = cardGroup.get(i, 0) + 1
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    rects = ply.bar(range(len(card_types)), [cardGroup.get(xtick, 0) for xtick in xticks], align='center')

    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    ply.xticks(range(len(card_types)), xticks)
    #设置横坐标的文字说明
    ply.xlabel('Card Type')
    #设置纵坐标的文字说明
    ply.ylabel('Frequency')
    #设置标题
    ply.title(u'Card Type Statistic')
    #绘图
    total = len(card_type_list)
    print(total)
    for rect in rects:
        height = rect.get_height()
        ply.text(rect.get_x() + rect.get_width() / 2, height, \
                 round(height/total*100,3), ha='center', va='bottom')
    ply.show()
#    print(cardGroup)
    
def bar_player(player_list, players):
    xticks = players
    playerGroup = {}
    #对每一类成绩进行频数统计
    for i in player_list:
        playerGroup[i] = playerGroup.get(i, 0) + 1
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    rects = ply.bar(range(len(players)), [playerGroup.get(xtick, 0) for xtick in xticks], align='center')

    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    ply.xticks(range(len(playerGroup)), xticks)
    #设置横坐标的文字说明
    ply.xlabel('Card Type')
    #设置纵坐标的文字说明
    ply.ylabel('Frequency')
    #设置标题
    ply.title(u'Card Type Statistic')
    #绘图
    total = len(player_list)
    print(total)
    for rect in rects:
        height = rect.get_height()
        ply.text(rect.get_x() + rect.get_width() / 2, height, \
                 round(height/total*100,3), ha='center', va='bottom')
    ply.show()
#    print(playerGroup)

