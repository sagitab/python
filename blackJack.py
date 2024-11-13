import random
money = 1000
bet=0
def init():
    global playerCards
    global dealerCards
    global money
    playerCards = []
    dealerCards = []
    money = 1000
def noAcardsSum(cards):
    sum=0
    for card in cards:
        if card==1:
            continue
        elif card==11 or card==12 or card==13:
            sum+=10
        else:
            sum+=card
    return sum            



#name=input("what is your name? ")
def trueValue(num,cards,hasA):
    if int(num) == 11 or int(num) == 12 or int(num) == 13:
        return 10
    elif num==1:
        noASum=noAcardsSum(cards)
        if noASum>10:
            return 1
        else:
            if hasA:
              return 1
            else:
              hasA=True
              return 11
    return num
def isLost(cards):#replace in 
    sum=getSum(cards)
    if sum>21:
        return True
    return False
def getSum(cards):
    sum=0
    hasA=False
    for card in cards:
        sum+=trueValue(card,cards,hasA)
        if card==1:
            hasA=True
    return sum    
def addCard(cards):
    newCard=random.randint(1, 13)
    cards.append(newCard)
    return isLost(cards) 
def dealerRes():
    contin=True
    while contin:
        if getSum(dealerCards)<=16:
            if addCard(dealerCards):
                return getSum(dealerCards)
        else:
            contin=False
    return getSum(dealerCards)            
def printCards(cards):
    for card in cards:
        print(str(card)+" ")
def status():
    dealerSum=getSum(dealerCards)
    playerSum=getSum(playerCards)
    print("dealer cards- ")
    printCards(dealerCards)
    print("dealer sum-",dealerSum  )
    
    print("player cards- ") 
    printCards(playerCards)     
    print("player sum-",playerSum  )

def endGame(dealer=0):
     global money
     global playerCards
     global bet
     dealerSum=0
     if dealer==0:
         dealerSum=dealerRes()
     else:
         dealerSum=dealer    
     print(f"dealer sum- {dealerSum}")
     playerSum=getSum(playerCards)
     print(f"player sum- {playerSum}")
     if playerSum>21:
        money-=int(bet)
        print(f"loser you have {money} ")    
     elif dealerSum>21:
            money+=int(bet)
            print(f"winner winner winner you have {money} ")
            return
        
    
     if dealerSum>playerSum:
            money-=int(bet)
            print(f"loser you have {money} ")
            
     elif playerSum>dealerSum:
            money+=int(bet)
            print(f"winner winner winner you have {money} ")
                
            
     else:
            print (f"eaqual you have money {money}")
                


   
def selectAction(dealer=0):
    status()
    global bet
    global money
    action=input("h-hit d-double s-stay sp-split- ")
    match action:
        case "h":
            print("hit")
            if addCard(playerCards):
                money-=int(bet)
                print(f"you have {getSum(playerCards)}")
                print(f"loser you have {money} ")
                return False
            return True

        case "s":
            print("stay")
            endGame(dealer)
            return False
           
            
          
        case "sp":
            print("split")
            if len(playerCards)>2:
                print("cant split to late")
                return True
            if playerCards[0]!=playerCards[1]:
                print("not same number")
                return True
            else:
                num=playerCards[0]
                sumDealerSplit=dealerRes()
                turn(num,sumDealerSplit)
                turn(num,sumDealerSplit)
                return False
        case "d":
            print("double")
            bet=int(bet)*2
            if addCard(playerCards):
                money-=int(bet)
                print(f"you have {getSum(playerCards)}")
                print(f"loser you have {money} ")

            endGame(dealer)
            return False    
            
        case _:
            print("not a valid action")        


def turn(num=0,dealerSum=0):
    
    global money
    global bet
    if num==0:
        toContinu=True
        bet=0
        while toContinu:
            bet=input("enter a bet- ")
            intBet=int(bet)
            if intBet<=money:
                toContinu=False
            else :
                print("unvalid bet") 
        rounds=0
        while selectAction():
            rounds+=1
       
    else:
        playerCards=[num]
        rounds=0
        while selectAction(dealerSum):
            rounds+=1
        playerCards[:]=[]
        dealerCards[:]=[]  
    newCard=random.randint(1, 13)
    newCard2=random.randint(1, 13)
    playerCards.append(newCard)  
    dealerCards.append(newCard2)


  
init()  
# newCard=random.randint(1, 13)
# newCard2=random.randint(1, 13)
# playerCards.append(newCard)  
# dealerCards.append(newCard2) 
dealerCards=[1]
playerCards=[2,2]
turn()   


