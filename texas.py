# -*- coding: utf-8 -*-
import texasfunction as tf
#import texas_statistic as ts
import texas_predict as tp
            
"""初始化牌桌"""
player_num_init = 4  # 玩家人数
poke = tf.cards()    # 生成牌桌
player_list = []    # 生成玩家列表
for i in range(player_num_init):
    player_list.append(tf.usr(str(i)))

"""统计数据"""
stat_card_types = []
stat_win_players = []

"""开始游戏"""
for r in range(1):
    player_num = len(player_list)
    poke.change_nums(player_num)
    flag_drop = 0
    poke.shuffle()  #洗牌
    cards = []
    poke.generate_usr_cardlist(r % player_num)   # 生成玩家手牌，根据序号生成
    for i in range(player_num):     #分发玩家手牌
        player_list[i].handcards(poke.usr_cardlist[i])

    """预测胜利的概率"""
    chips = tf.chips()
    chips.reset(player_num)
    # 第〇轮
    print("第〇轮加注开始：")
    card_deal = poke.deal()     # 发牌
    #加注
    flag_drop = tf.check_raise(player_list,chips,r % player_num, 1)
    if flag_drop:
        for i in range(player_num):
            if player_list[i].drop == 0:
                player_list[i].handchip += sum(chips.chip_num)
                print("玩家%s获胜！ 赢得%d筹码！" % \
                      (player_list[i].name,sum(chips.chip_num)))
        continue
#    tp.predict_result(player_list, cards)
    
    # 第一轮，发三张牌发第一轮三张牌
    print("第一轮加注开始：")
    cards = next(card_deal)
    #加注
    flag_drop = tf.check_raise(player_list,chips,r % player_num)
    if flag_drop:
        for i in range(player_num):
            if player_list[i].drop == 0:
                player_list[i].handchip += sum(chips.chip_num)
                print("玩家%s获胜！ 赢得%d筹码！" % \
                      (player_list[i].name,sum(chips.chip_num)))
        continue
#    tp.predict_result(player_list, cards)
    
    # 第二轮，发一张牌
    print("第二轮加注开始：")
    cards.append(next(card_deal))
    #加注
    flag_drop = tf.check_raise(player_list,chips,r % player_num)
    if flag_drop:
        for i in range(player_num):
            if player_list[i].drop == 0:
                player_list[i].handchip += sum(chips.chip_num)
                print("玩家%s获胜！ 赢得%d筹码！" % \
                      (player_list[i].name,sum(chips.chip_num)))
        continue
#    tp.predict_result(player_list, cards)
    
    # 第三轮，发一张牌
    print("第三轮加注开始：")
    cards.append(next(card_deal))
    #加注
    flag_drop = tf.check_raise(player_list,chips,r % player_num)
    if flag_drop:
        for i in range(player_num):
            if player_list[i].drop == 0:
                player_list[i].handchip += sum(chips.chip_num)
                print("玩家%s获胜！ 赢得%d筹码！" % \
                      (player_list[i].name,sum(chips.chip_num)))
        continue
#    tp.predict_result(player_list, cards)
    
    # 生成玩家手牌类型
    for i in range(player_num):
        player_list[i].cardtype(cards)
    # 输出测试
    tf.print_cards(player_list,cards)
    tf.chip_balance(player_list,chips)
    tf.print_chips(player_list)
    
    
                
                
                
                        
                    

            
            

#    for i in range(player_num):
#        stat_card_types.append(card_types[player_list[i].handcard_type[0]])
#        if result[i] == 0:
#            stat_win_players.append(player_list[i].name)
#
#ts.bar_card_type(stat_card_types,card_types)
#ts.bar_player(stat_win_players,[x.name for x in player_list])




