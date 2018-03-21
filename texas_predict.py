# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:36:03 2018

@author: hsf
"""
import texasfunction as tf
import copy
def predict_all(player_list, cards, repeat_num = 2000):
    """
    当全部玩家的手牌为明牌时，预测每名玩家的获胜概率
    """    
    player_num = len(player_list) #记录玩家数量
    player_drop = [player_list[x].drop for x in range(player_num)]
    result_count = [0] * player_num # 记录每位玩家获胜次数
    
    card_pr = tf.card_predict() # 生成预测牌桌
    card_pr.change_nums(player_num) # 设定玩家个数
    card_pr.remove_cards(cards) # 从牌桌移除底牌
    for i in range(len(player_list)):  #从牌桌移除玩家手牌
        card_pr.remove_cards(player_list[i].handcard)
        
    for i in range(repeat_num):
        card_pr.shuffle()   # 洗牌
        cards_tmp = cards + card_pr.deal(len(cards)) # 记录5张底牌
        # 生成每位玩家手牌
        for n in range(player_num):
            player_list[n].cardtype(cards_tmp)
        result = tf.player_rank(player_list[:]) #记录获胜玩家
        for m in range(player_num): #将弃牌玩家的排序置为100
            if player_drop[m] == 1:
                result[m] = 100
        for j in range(player_num): #更新每位玩家获胜次数
            if result[j] == min(result):
                result_count[j] += 1
    
    output = []
    for i in range(player_num):
        if player_drop[i] == 0:
            output.append(format(result_count[i]/repeat_num,'.2%'))
        else :
            output.append('Quit')
    return output

def predict_self(player, cards, player_num, drop_num = 0, repeat_num = 2000):
    """
    当只知道player玩家的手牌时，预测该玩家的获胜概率
    """
    if player.drop == 1:
        return 'Quit'    
    if player_num - drop_num== 1:
        return format(1, '.2%')
        
    card_pr = tf.card_predict() # 生成预测牌桌
    card_pr.remove_cards(player.handcard + cards)  # 从牌桌移除玩家的牌和底牌
    card_pr.change_nums(player_num-1) # 设定玩家个数
    player_tmp = tf.usr("test") #生成虚拟玩家test，用于与player比较
    n = 0   # 记录player获胜次数
    for i in range(repeat_num):
        flag = 0    #记录player是否获胜，0为获胜，1为失败
        card_pr.shuffle()   # 洗牌
        card_pr.generate_usr_cardlist(0)   # 生成虚拟玩家手牌
        cards_tmp = cards + card_pr.deal(len(cards)) # 记录5张底牌
        player.cardtype(cards_tmp)  #生成player牌型
        for j in range(player_num-1-drop_num):     # 根据牌桌上玩家个数分发玩家手牌
            player_tmp.handcards(card_pr.usr_cardlist[j]) # 分发虚拟玩家手牌
            player_tmp.cardtype(cards_tmp[:])   #生成虚拟玩家牌型
            if tf.card_compare(player.handcard_type,player_tmp.handcard_type) == -1:
                #比较player与虚拟玩家的大小
                flag = 1
                break
        else:
            if flag == 0:
                n += 1
    return format(n/repeat_num,'.2%')

def predict_result(player_list, cards):
    """
    格式化输出预测结果
    """
    player_num = len(player_list)
    symbol_num = player_num * 10 + 18
    
    self_prob = []
    drop_num = sum([player_list[i].drop for i in range(player_num)])
    print(drop_num)
    for i in range(player_num):
        self_prob.append(predict_self(copy.deepcopy(player_list[i]),\
                                    cards[:],player_num,drop_num))
    all_prob = predict_all(copy.deepcopy(player_list),cards[:])
    
    rounds = ['第〇轮','','','第一轮','第二轮','最终轮']
    print('%s' % '*' * symbol_num)
    print('%30s' % rounds[len(cards)] + '玩家获胜概率')
    print('%s' % '=' * symbol_num)
    print('%s' % ' ' * 18, end = '')
    for i in range(player_num):
        print('%10s' % player_list[i].name, end = '')
    print('\n%18s' % 'Self Probability:', end = '')
    for i in range(player_num):
        print('%10s' % self_prob[i], end = '') 
    print('\n%18s' % 'All Probability:', end = '')
    for i in range(player_num):
        print('%10s' % all_prob[i], end = '') 
    print('\n%s\n' % ('*' * symbol_num))


    
    