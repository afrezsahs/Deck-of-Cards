import random

## Conditional If .. Else
def checkOdd(x) :
    if ( x % 2 ) : 
        return 'odd'
    else : return 'even'

print(checkOdd(2))

## Conditional If .. Elif .. Else

def checkWin(x,y):
    if (x > y) : result = 'win' 
    elif (x < y) : result = 'lose'
    else : result = 'draw'
    return result

print(checkWin(6,8))

## loops 

suit = ['Diamond','Club','Heart','Spade']
rank = []
i = 0
while i < 13:
    i+=1
    rank.append(i)
    
print(rank)

for i in range(len(rank)) :
    if (i == 0) : rank[i] = 'Ace' 
    elif (i == 10) : rank[i] = 'Jack'
    elif (i == 11) : rank[i] = 'Queen'
    elif (i == 12) : rank[i] = 'King'
    else: rank[i] = str(rank[i])

print(rank)

deck_of_cards = []

for i in range(len(suit)) :
    for j in range(len(rank)) : 
        deck_of_cards.append(suit[i]+' '+rank[j])

random.shuffle(deck_of_cards)


def drawCard(x,deck) :
    hand = []
    i = 0
    while i < x : 
        hand.append(deck[i])
        i += 1
    return hand

print(drawCard(5,deck_of_cards))

     
