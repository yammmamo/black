#coding:utf-8 

import random

RANK, SUIT = 0,1
def card_deck(): #デッキを作る
        suits = ['S','H','D','C']
        ranks = range(1,14)
        deck = [(x,y) for x in ranks for y in suits]
        random.shuffle(deck)
        return deck


def get_point(hand):
        result = 0 #数字の合計保存
        ace_flag = False
        for card in hand:
                num = card[RANK]
                if card[RANK] == 1: #カードがAかどうか判定
                        ace_flag = True
                if card[RANK] > 10 :
                        num = 10
                result = result + num
                if ace_flag == True  and result <= 11: #Aが含まれていて、合計が11以下かどうか判定
                        result = result +10 #Aを11と考えresultに10を加える

        return result

    #print('Player:',format(player_hand)) #プレイヤーの手札を表示
    #print(getpoint_point(player_hand)) #プレイヤーの手札の合計を表示
    #print('Player:',format(player_hand)) #ディーラーの手札を表示
    #print(getpoint_point(dealer_hand)) #ディーラーの手札の合計を表示

def main():
    player_hand = [] #プレイヤー手札の格納リスト
    dealer_hand = [] #ディーラー手札の格納リスト
    deck = card_deck() #デッキの作成
       	#print(deck)
    card = deck.pop() #カードを引く
    for i in range(2): #２枚ずつ引く
        player_hand.append(deck.pop()) #プレイヤーの手札を引く
        dealer_hand.append(deck.pop()) #ディーラーの手札を引く
	#print('Player:',format(player_hand)) #プレイヤーの手札を表示
	#print('Dealer:',format(dealer_hand)) #ディーラーの手札を表示
    print('Player:',format(player_hand)) #プレイヤーの手札を表示
    print(get_point(player_hand)) #プレイヤーの手札の合計を表示
    print('Dealer:',format(dealer_hand)) #ディーラーの手札を表示
    print(get_point(dealer_hand)) #ディーラーの手札の合計を表示

#Player
    while (1):
        op = input('Player,もう1枚引く:1,もう引かないよ:2 =')
        if op == 1:
            print('[Player:もう1枚引く]')
            player_hand.append(deck.pop()) #プレイヤーが手札を引く
            print(player_hand)  #引いた手札の表示
            print(get_point(player_hand)) #引いた手札の合計を表示
        elif  op == 2:  
            print('[Player:もう引かないよ]')
            break
        else:
            continue
        if get_point(player_hand) > 21: #プレイヤーの手札が21より大きい場合
            print('[Player Burst]')
            break
    
#Dealer
    while get_point(player_hand) <=21: #プレイヤーの手札の合計が21以下の場合
        if get_point(dealer_hand)>=17: #ディラーの手札の合計が17以上の場合
            print('[Dealer:もう引きません]')
            print(get_point(dealer_hand))
            break
        else:
            dealer_hand.append(deck.pop())
            print('[Dealer:もう一枚引く]')
            print(dealer_hand)
            print(get_point(dealer_hand))

    if get_point(player_hand) >21:
        print('[Dealer Win]')
        print('[Player]',get_point(player_hand),'[Dealer]',get_point(dealer_hand))
    elif get_point(player_hand) > get_point(dealer_hand):
        print('[Player Win]')
        print('[Player]',get_point(player_hand),'[Dealer]',get_point(dealer_hand))
    elif get_point(dealer_hand) > 21:
        print('[Player Win]')
        print('[Player]',get_point(player_hand),'[Dealer]',get_point(dealer_hand))
    elif get_point(dealer_hand) > get_point(player_hand):
        print('[Dealer Win]')
        print('[Player]',get_point(player_hand),'[Dealer]',get_point(dealer_hand))
    elif get_point(dealer_hand) == get_point(player_hand):
        print('[Draw]')
        print('[Player]',get_point(player_hand),'[Dealer]',get_point(dealer_hand))

if __name__ == '__main__':
	main()
