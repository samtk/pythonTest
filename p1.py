import random

def makeCards(numdecks):
   suit = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
   deck = []
   for i in range(0,numdecks*4):
      for k in range(0,13):
         deck.append(suit[k])
   return deck

def drawboard(dealer,player, dvalue, pvalue):
   print("---------------")
   print("dealer's hand ("+ str(dvalue)+")")
   print("")
   for x in range(len(dealer)):
      print(dealer[x], end = " ", flush = True)
   print("")
   print("---------------")
   print("player's hand ("+ str(pvalue) + ")")
   print("")
   for x in range(len(player)):
      print(player[x],end = " ", flush = True)
   print("")
   print("---------------")  

def getCardValue(card):
   value = 0
   if(card == "K" or card == "Q" or card == "J"):
      value = 10
   elif(card == "A"):
      value = 0
   else:
      value = str(card)
   return value

def game():
   print("Game starting, type quit to exit program")
   deck = makeCards(8)
   dealerdraw = random.randint(0,len(deck)-1) 
   playerdraw = random.randint(0,len(deck)-1)
   dealerhand = []
   playerhand = []
   dealerhand.append(deck[dealerdraw])
   playerhand.append(deck[playerdraw])
   dealerhandvalue = getCardValue(dealerhand[0])
   playerhandvalue = getCardValue(playerhand[0])
   if(dealerhandvalue==0):
      dealerhandvalue = 11
   if(playerhandvalue == 0):
      ace = input("Would you like the ace to be 1 or 11?  ")
      playerhandvalue = int(ace)

   drawboard(dealerhand, playerhand, dealerhandvalue, playerhandvalue)
   playerinput = ""

   playerhold = False
   dealerhold = False
   while(playerinput.lower() != "quit"):
      playerinput = input("Would you like to hit or miss?  ")
      if(playerinput == "hit"):
         playerdraw = random.randint(0,len(deck)-1)
         playerhand.append(deck[playerdraw])
         cardval = getCardValue(playerhand[0])
         if(cardval = 0):
            ace = input("Would you like the ace to be 1 or 11?  ")
            playerhandvalue += int(ace)
         else:
            playerhandvalue += cardval
      else(playerinput == "miss"):
         playerhold = True      
