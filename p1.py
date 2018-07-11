import random

def makeCards(numdecks):
   suit = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
   deck = []
   for i in range(0,numdecks*4):
      for k in range(0,13):
         deck.append(suit[k])
   return deck

def drawboard(dealer,player):
   print("---------------")
   print("dealer's hand")
   print("")
   for x in range(len(dealer)):
      print(dealer[x], end = " ", flush = True)
   print("")
   print("---------------")
   print("player's hand")
   print("")
   for x in range(len(player)):
      print(str(player[x],end = " ", flush = True))
   print("")
   print("---------------")  

def getCardValue(card):
   value = 0
   if(card == "K" || card == "Q" || card == "J"):
      value = 10
   elif(card = "A"):
      value = 0
   else:
      value = str(card)
   return value

def game():
   print("Game starting, type quit to exit program")
   deck = makeCards(8)
   dealerDraw = random.randint(0,len(deck)-1) 
   playerDraw = random,randint(0,len(deck)-1)
   dealerHand = []
   playerHand = []
   dealerHand.append(deck[dealerDraw])
   playerHand.append(deck[dealerDraw])
   drawboard(dealerHand, playerHand)
   playerinput = input("Would you like to hit or miss?  ")
   while(playerinput.lower() != "quit"):
            
  
    
