import random
money = 1000
bet=0
doubleAfterSplit=False
def cardValue(card):
     if card==11:
          return "J"
     elif card==12:
          return "Q"
     elif card==13:
          return "K"
     elif card==1:
          return "A"
     else:
          return card
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
    if cards==None:
         return 0
    sum=0
    hasA=False
    for card in cards:
        sum+=trueValue(card,cards,hasA)
        if card==1:
            hasA=True
    return sum    
def addCard(cards):
    newCard=random.randint(1, 13)
    #newCard=2
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
        print(str(cardValue(card))+" ")
def status():
    dealerSum=getSum(dealerCards)
    playerSum=getSum(playerCards)
    print("************************************")
    print("dealer cards- ")
    printCards(dealerCards)
    print("dealer sum-",dealerSum  )
    print("************************************")
    print("player cards- ") 
    printCards(playerCards)     
    print("player sum-",playerSum  )
    print("************************************")
def whoWon(playerSum,dealerSum):
     global money
     global bet
     playerSum=int(playerSum)
     dealerSum=int(dealerSum)
     print("***************end***************")
     print(f"dealer sum- {dealerSum}")
     print(f"player sum- {playerSum}")
     if playerSum>21:
              money-=int(bet)
              print(f"loser you have {money} ") 
              return   
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


def endGame(splitCount=0,split1Cards=None):
     global money
     global playerCards
     global bet
     dealerSum=0
     if splitCount==0:
         dealerSum=dealerRes()
         playerSum=getSum(playerCards)
         whoWon(playerSum,dealerSum)
     elif splitCount==1:
         return  
     elif splitCount==2:
        dealerSum=dealerRes()
        print("************************************")
        print("split 1-")
        playerSum=getSum(split1Cards)
        if playerSum<=21:
            whoWon(playerSum,dealerSum)
        print("************************************")
        print("split 2-")
        playerSum=getSum(playerCards)
        whoWon(playerSum,dealerSum)
        
    
    
                


   
def selectAction(splitCount=0,split1Cards=None):
    status()
    global doubleAfterSplit
    global bet
    global money
    global dealerCards
    global playerCards
    action=input("h-hit d-double s-stay sp-split- ")
    if action=="h":
    
        print("hit")
        if addCard(playerCards):
                money-=int(bet)
                print(f"you have {getSum(playerCards)}")
                print(f"loser you have {money} ")
                return False
        return True

    elif action=="s":
            print("stay")
            endGame(splitCount,split1Cards)
            return False
           
            
          
    elif action=="sp":
            print("split")
            lengthPlayer=len(playerCards)
            if lengthPlayer>2 or lengthPlayer==1:
                print("can't split to late")
                return True
            if playerCards[0]!=playerCards[1]:
                print("not same number")
                return True
            else:
                num=playerCards[0]
                playerCards=[num]
                temp=dealerCards.copy()
                dealerCards=temp
                print("************************************")
                print("split 1-")
                split1Cards=turn(num,1)
                playerCards=[num]
                dealerCards=temp
                if doubleAfterSplit:
                     bet=bet/2
                print("************************************")
                print("split 2-")
                turn(num,2,split1Cards)
                return False
    elif action=="d":
            if splitCount!=0:
                 doubleAfterSplit=True
            print("double")
            bet=int(bet)*2
            if addCard(playerCards):
                money-=int(bet)
                print(f"you have {getSum(playerCards)}")
                print(f"loser you have {money} ")
            if splitCount!=0:
                 status()
            endGame(splitCount,split1Cards)
            return False    
            
    else:
            print("************************************")
            print("not a valid action")    
            print("************************************")    


def turn(num=0,splitCount=0,split1Cards=None):
    global playerCards
    global dealerCards
    global money
    global bet
    if num==0:
        toContinu=True
        bet=0
        while toContinu:
            bet=input("enter a bet- ")
            intBet=int(bet)
            if intBet==-1:
                 exit(0)
            elif bet==0:
                     print("************************************")
                     print("unvalid bet") 
                     print("************************************")
            elif intBet<=money:
                toContinu=False
             
            else :
                print("************************************")
                print("unvalid bet") 
                print("************************************")
        rounds=0
        while selectAction():
            rounds+=1
       
    else:
        playerCards=[num]
        rounds=0
        while selectAction(splitCount,split1Cards):
            rounds+=1
        if splitCount==1:
             return playerCards
    playerCards[:]=[]
    dealerCards[:]=[]  
    newCard=random.randint(1, 13)
    newCard2=random.randint(1, 13)
    playerCards.append(newCard)  
    dealerCards.append(newCard2)


  
init()  
newCard=random.randint(1, 13)
newCard2=random.randint(1, 13)
playerCards.append(newCard)  
dealerCards.append(newCard2) 
print("****************start****************")
#dealerCards=[1]
#playerCards=[2,2]
while True:
    if money==0:
                print("money is 0 like you")
                exit(0)
    turn()
     
   


