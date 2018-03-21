# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:07:37 2018

@author: hsf
"""
import random
import numpy as np
class usr():
    def __init__(self,name):
        self.name = name
        self.drop = 0
        self.handcard_type = []
        self.handcard = []
        self.handchip = 200
        
    def handcards(self,handcard):
        self.handcard = handcard
    
    """接受底牌序列并将数字转化为花色+牌号"""
    def __prepare(self,cards):
        tmp = sorted(cards + self.handcard)
        self.num = [((x-1) % 13 + 1) for x in tmp]
        self.color = [((x-1) // 13) for x in tmp]
    
    """__complement: 序列补足"""    
    def __complement(self,cardking,cardcount):
        for i in range(len(cardcount)):
            if cardcount[i] == 1:
                cardking.append(i)   #在序列中补充频次唯一的牌号，按照由大到小的顺序
            if len(cardking) == 5:   #当序列长度为5时停止
                break        

    """__islong: 判断是否为顺子"""
    def __islong(self, cardlist):
        if 13 in cardlist:          #当序列中存在13（A）时，在序列前加入0，A2345
            cardlist.insert(0,0)
        long = [cardlist[0]]        #保存顺子序列
        cardlast = long[0]
        for i in range(len(cardlist)):
            if cardlist[i] - cardlast == 1:   #本次-前次=1，记录
                long.append(cardlist[i])
            elif cardlist[i] - cardlast == 0: #本次=前次，跳过
                next
            else:                        #本次-前次>1
                if len(long) >= 5:       #若此时连续序列个数大于等于5   
                    return long[-5::]
                else:                    #若此时连续序列个数小于5，重置
                    long = [cardlist[i]]
            cardlast = cardlist[i]       #记录本次牌号
        else:                            #循环结束
            if len(long) >= 5:
                    return long[-5::]
            else:
                return False
            
    """__isking: 判断是否为金刚、葫芦、三条、两对、单对、高牌"""        
    def __isking(self, cardlist):
        """为方便从大到小取牌，将牌号从大到小排列"""
        cardcount = [cardlist.count(x) for x in range(1,14)] #记录每张牌出现次数
        cardcount.reverse()  #反向
        cardking = []  #记录最大的牌组
        cardorder = 0  #记录最大牌组的等级序号
        
        """当存在两种重复牌号时，记录第一大（如三条）和第二大（一对）的牌号"""
        first_index = 0
        second_index = 0
        
        if max(cardcount) == 4:    #当重复牌号的频次最大为4
            first_index = cardcount.index(4)
            for i in range(len(cardcount)):
                if (i != first_index) and (cardcount[i] != 0):
                    cardking = [first_index] * 4 + [i]
                    break
            cardorder = 8
        elif max(cardcount) == 3:  #当重复牌号的频次最大为3
            first_index = cardcount.index(3)
            """为区别不同情况，对cardcount中的数字求平方和，记为cardsum
                3+3+1 = 19
                3+2+2 = 17
                3+2+1+1 = 15
                3+1+1+1+1 = 13
            """
            cardsum = sum([x ** 2 for x in cardcount])
            if cardsum == 19:    #3+3+1
                second_index = cardcount.index(3,first_index+1)
                cardking = [first_index] * 3 + [second_index] * 2
                cardorder = 7
            elif cardsum == 17:  #3+2+2
                cardking = [first_index] * 3 + [cardcount.index(2)] * 2
                cardorder = 7
            elif cardsum == 15:  #3+2+1+1
                cardking = [first_index] * 3 + [cardcount.index(2)] * 2
                cardorder = 7
            elif cardsum == 13:  #3+1+1+1+1
                cardking = [first_index] * 3
                self.__complement(cardking,cardcount[:])
                cardorder = 4
        elif max(cardcount) == 2:   #当重复牌号的频次最大为2
            first_index = cardcount.index(2)
            if (first_index != 12) and (max(cardcount[first_index+1:]) == 2):     #当牌组为双对时
                second_index = cardcount.index(2,first_index+1) #求第二大牌号
                cardorder = 3
                for i in range(len(cardcount)):
                    if (i == first_index) or (i == second_index):
                        next
                    else:
                        if cardcount[i] != 0:
                            cardking = [first_index] * 2 + [second_index] * 2 \
                            + [i]
                            break
            else:   #当牌组为单对时
                cardking = [first_index] * 2
                self.__complement(cardking,cardcount[:])
                cardorder = 2
        else:
            self.__complement(cardking,cardcount[:])
            cardorder = 1
        cardking_reverse = [13-x for x in cardking]
        cardking_reverse.reverse()
        return cardorder, cardking_reverse #将牌号顺序转为有小到大
    
    def cardtype(self, cards):
        self.__prepare(cards)
        cardcolor_list = []  
        """判断是否为同花顺和同花"""
        cardset = {}
        count_max = 0  #记录同花色最大卡牌数量
        cardcolor = '' #记录卡牌数量最大的花色
        for c in range(4):  #生成key为花色，item为牌号序列的字典
            cardset[str(c)] = [x for i, x in enumerate(self.num) if self.color[i] == c]
        for key in cardset.keys():     #统计最长牌号序列的长度和花色
            if len(cardset[key]) > count_max:
                count_max = len(cardset[key])
                cardcolor = key
        if count_max >= 5:      #如果序列长度大于等于5，此时为同花
            if self.__islong(cardset[cardcolor][:]):  #如果为顺子，则为同花顺
                self.handcard_type = [9, [int(cardcolor)]*5, \
                                          self.__islong(cardset[cardcolor])[:]]
                return
            else :  #否则为同花
                self.handcard_type = [6, [int(cardcolor)]*5, \
                                          cardset[cardcolor][-5::]]
                return
        
        """判断是否为顺子"""        
        if self.__islong(sorted(self.num)):
            for c in self.__islong(sorted(self.num)):
                if c == 0:  #如果包含0，对应A2345，需要转化为13
                    cardcolor_list.append(self.color[self.num.index(c+13)])
                else:
                    cardcolor_list.append(self.color[self.num.index(c)])
            self.handcard_type = [5, cardcolor_list, \
                                  self.__islong(sorted(self.num))[:]]
            return
        
        """判断是否为金刚、葫芦、三条、两对、单对、高牌"""
        cardorder, cardnum_list = self.__isking(sorted(self.num))
        start = 0
        c_last = 0
        #将返回的cardnum_list/牌号与牌组比较，得出对应花色
        for c in cardnum_list:
            if c == c_last: #若牌号c与上次相等，需要从上次的序号的下一个开始查询
                cardcolor_list.append(self.color[self.num.index(c,start)])
                start = self.num.index(c,start) + 1   #更新下次查询的开始序号 
            else:   #若牌号c与上次不等，
                cardcolor_list.append(self.color[self.num.index(c)])
                c_last = c
                start = self.num.index(c)+1
        self.handcard_type = [cardorder, cardcolor_list, cardnum_list[:]]
        return
        
class cards():
    cardlist = list(range(1,53))
    def __init__(self):
        self.usr_nums = 0
        self.usr_cardlist = []  
    def change_nums(self,player_num):
        self.usr_nums = player_num
    def shuffle(self):
        random.shuffle(self.cardlist)
    def generate_usr_cardlist(self,usr_order):
        order = 0
        self.usr_cardlist = [[0,0]] * self.usr_nums
        for n in range(self.usr_nums):
            order = (n + self.usr_nums - usr_order + 1) % self.usr_nums
            self.usr_cardlist[n] = [self.cardlist[order],\
                              self.cardlist[order + self.usr_nums]]
    def deal(self):
        while(True):
            yield self.cardlist[(2*self.usr_nums+1):(2*self.usr_nums+4):]
            yield self.cardlist[(2*self.usr_nums+5)]
            yield self.cardlist[(2*self.usr_nums+7)]

class card_predict(cards):
    #继承cards类，用于在texas_predict中生成手牌类
    def remove_cards(self,cardlist):
        #用于去掉已经存在的牌
#        self.cardlist = [x for x in range(1,53) if x not in cardlist]
        self.cardlist = [x for x in self.cardlist if x not in cardlist]
    def deal(self,card_num):
        #重写deal函数，根据此时底牌数量，返回应发的底牌
        if card_num == 0:
            return self.cardlist[(2*self.usr_nums+1):(2*self.usr_nums+4):] +\
                [self.cardlist[(2*self.usr_nums+5)]]+\
                [self.cardlist[(2*self.usr_nums+7)]]
        elif card_num == 3:
            return [self.cardlist[(2*self.usr_nums+1)]]
        elif card_num == 4:
            return [self.cardlist[(2*self.usr_nums+1)]]+\
                [self.cardlist[(2*self.usr_nums+3)]]
        elif card_num == 5:
            return []

class chips():
    def __init__(self):
        self.chip_num = []
        self.all_in = []
    def reset(self, player_num):
        self.chip_num = [0] * player_num
        self.all_in = [0] * player_num
    
def card_trans(card_num,card_color=[], card_type = 10):
    #将卡牌列表转化为poke牌
    #如果只输入card_num，则表示输入为原始牌号，1-52
    #如果同时输入三个变量，则表示输入为最终手牌
    
    color = ["红桃","方片","黑桃","草花"]
    num = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    card_poker = []
    if not card_color:  #如果没有花色列表，需要对card_num转化
        card_color = [((x-1) // 13 ) for x in card_num]
        card_num = [((x-1) % 13 + 1) for x in card_num]
        tmp = np.argsort(card_num)
        card_num = [card_num[x] for x in tmp]
        card_color = [card_color[x] for x in tmp]
    for i in range(len(card_num)):  #将花色与牌号结合输出
        card_poker.append(color[card_color[i]]+num[card_num[i]-1])
    if (card_type == 5) or (card_type == 9):
        #如果为同花顺或顺子，需判断是否要将A置于第一位
        if card_num[0] == 1:
            card_poker.insert(0,card_poker[-1])
            del card_poker[-1]
    return card_poker

def card_compare(cardtype1,cardtype2):
    # 比较两组牌型的大小
    if cardtype1[0] > cardtype2[0]:
        return 1
    elif cardtype1[0] < cardtype2[0]:
        return -1
    else:
        type1, type2 = cardtype1[2][:], cardtype2[2][:]
        type1.reverse()
        type2.reverse()
        if type1 > type2:
            return 1
        elif type1 < type2:
            return -1
        else:
            return 0

def player_rank(players):
    # 返回玩家最终牌型大小顺序，最大为0
    l = len(players)
    index = list(range(l))
    rank = [-1] * l
    n = 0   # 记录排名
    while(len(index)>=2):
        tmp = index[0]
        max_rank = [tmp]
        # 取出玩家中最大的一个或多个玩家的序号
        for i in index[1:]:
            if card_compare(players[i].handcard_type,players[tmp].handcard_type) == 1:
                tmp = i
                max_rank = [tmp]
            elif card_compare(players[i].handcard_type,players[tmp].handcard_type) == -1:
                continue
            elif card_compare(players[i].handcard_type,players[tmp].handcard_type) == 0:
                tmp = i
                max_rank.append(tmp)
        # 将玩家序号对应位置的rank排名置为当前n
        for j in max_rank:
            rank[j] = n
        # n加一，去掉列表中最大的玩家，进行下一轮筛选最大玩家
        n += 1
        index = [x for x in index if x not in max_rank]
    else:
        #当循环到列表只有一个玩家时
        if len(index) == 1:
            rank[index[0]] = n
    return rank

def print_cards(player_list,cards):
    # 打印底牌与手牌
    card_types = ["高牌","单对","双对","三条","顺子","同花","葫芦","金刚","同花顺"]
    print("此时底牌是:",card_trans(cards))
    print("玩家手牌分别是：")
    for i in range(len(player_list)):
    
        print("玩家" + player_list[i].name + "：", end=' ')
        print(card_types[player_list[i].handcard_type[0]-1], end=' ')
        print(card_trans(player_list[i].handcard_type[2],\
                         player_list[i].handcard_type[1],\
                         player_list[i].handcard_type[0]), end=' ')
        print("\t底牌：", end=' ')
        print(card_trans(player_list[i].handcard))

def check_raise(player_list, chips, usr_order, first_round = 0):
    player_num = len(player_list)
    chip_round = [0] * player_num #记录每人加注数量
    rounds = [0] * player_num #记录每人加注轮数
    allin = ['','(All In)']
    flag = True
    i = usr_order
    at_last = 0
    if first_round == 1:
        chip_round[i] = 5
        chips.chip_num[i] = 5
        chip_round[i+1] = 10
        chips.chip_num[i+1] = 10
        player_list[i].handchip -= 5
        player_list[i+1].handchip -= 10
        rounds[i] = 1
        rounds[i+1] = 2
        i += 2
        at_last += 2
    
    while(flag):
        at_last += 1
        i = i % player_num
        if player_list[i].drop == 1:
            rounds[i] = max(rounds)
            if (rounds == [max(rounds)] * player_num) and (at_last >= player_num):
                flag = False
            i += 1
            continue
        if chips.all_in[i] == 1:
            rounds[i] = max(rounds)
            if (rounds == [max(rounds)] * player_num) and (at_last >= player_num):
                flag = False
            i += 1
            continue
        print('玩家%s：(筹码%s)' % (player_list[i].name, player_list[i].handchip))
        while(True):
            chip_last_tmp = 0 #玩家加注，若筹码不足时需要重新加注
            chip_min = max(chip_round) - chip_round[i]
            chip_max = sum(chips.chip_num)
            chip = input("是否加注？(%s ~ %s)\n(加注输入额外的筹码/弃牌输入q/梭哈出入a/跟注输入f/一倍底池输入d）" %\
                         (chip_min,chip_max))
            if chip.lower() == 'q':
                player_list[i].drop = 1
                chip_last_tmp = 0
                print('玩家%s弃牌！' % player_list[i].name)
            elif chip.lower() == 'a':              
                chip_last_tmp = player_list[i].handchip
                              
            elif chip.lower() == 'f':
                chip_last_tmp = max(chip_round) - chip_round[i]
                pass

            elif chip.lower() == 'd':
                chip_last_tmp += sum(chips.chip_num)
                
            elif chip.isdigit():
                chip_last_tmp = int(chip) + max(chip_round) - chip_round[i]

            else:
                print("请尝试正确输入！")
                continue

            if chip_last_tmp > player_list[i].handchip:
                print('你的筹码不足！')
            elif chip_last_tmp > sum(chips.chip_num):
                print('加注超过底池筹码！')
            elif chip_last_tmp == player_list[i].handchip:
                print('你已经all in！')
                chips.all_in[i] = 1
                break
            else:
                break
            
        sig = chip_last_tmp + chip_round[i] - max(chip_round)
        if sig > 0:
            rounds[i] = max(rounds) + 1
        elif sig <= 0: 
            rounds[i] = max(rounds)               
            
        chips.chip_num[i] += chip_last_tmp
        chip_round[i] += chip_last_tmp
        player_list[i].handchip -= chip_last_tmp
        if chip.lower() != 'q':
            print(player_list[i].name)
            print("玩家%s加注%s!%s" % (player_list[i].name, chip_last_tmp, allin[chips.all_in[i]]))
        """格式化输出"""
        symbol_num = player_num * 15
        print('%s' % ('=' * symbol_num))
        for j in range(player_num):
            print('%15s' % player_list[j].name, end = '')
        print('\n')            
        for j in range(player_num):
            if player_list[j].drop == 1:
                print("%15s" % ('(Quit) '+str(chips.chip_num[j])), end = '')
            elif chips.all_in[j] == 1:
                print("%15s" % ('(Allin) '+str(chips.chip_num[j])), end = '')
            else:
                print("%15s" % str(chips.chip_num[j]), end = '')
        print('\n%s' % ('=' * symbol_num))
        print(rounds)
        """"""
        if (rounds == [max(rounds)] * player_num) and (at_last >= player_num):
            flag = False
        i += 1
        
        drop_num = sum([player_list[i].drop for i in range(player_num)])
        if (player_num - drop_num) == 1:
            return True
 
def chip_balance(player_list,chips):
    player_num = len(player_list)
    result = player_rank(player_list[:])
    for i in range(player_num):
        if player_list[i].drop == 1:
            result[i] = max(result) + 1
    sumchips = 0
    for i in range(max(result)+1):
        if sum(chips.chip_num) == 0:
            break
        else:
            tmp = result.count(i)
            win = []
            for j in range(tmp):
                k_min = 0
                for k in range(len(result)):
                    if (result[k] == i) and (k not in win):
                        if result[k_min] != i:
                            k_min = k
                        elif chips.chip_num[k] < chips.chip_num[k_min]:
                            k_min = k
                win.append(k_min)
                chip_min = chips.chip_num[k_min]
                for m in range(len(result)):
                    if chips.chip_num[m] <= chip_min:
                        sumchips += chips.chip_num[m]
                        chips.chip_num[m] = 0
                    else:
                        sumchips += chip_min
                        chips.chip_num[m] -= chip_min
                sumchips_div = round(sumchips / (tmp - j))
                player_list[k_min].handchip += sumchips_div
                sumchips -= sumchips_div
                print("玩家%s获胜！ 赢得%d筹码！" % \
                      (player_list[k_min].name,sumchips_div))
def print_chips(player_list):
    player_num = len(player_list)
    symbol_num = player_num * 15
    print('%s' % ('=' * symbol_num))
    for j in range(player_num):
        print('%15s' % player_list[j].name, end = '')
    print('\n')            
    for j in range(player_num):
        print("%15s" % player_list[j].handchip, end = '')
    print('\n%s' % ('=' * symbol_num))
       
        

    