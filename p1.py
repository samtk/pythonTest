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

def whoWins(dealervalue,playervalue):
   result = ""
   if(dealervalue > 21 and playervalue > 21):
      result = "no one"
   elif(dealervalue == playervalue):
      result ="no one"
   elif(dealervalue > 21):
      result = "player"
   elif(playervalue > 21):
      result = "dealer"
   elif(playervalue > dealervalue):
      result = "player"
   else:
      result = "dealer"
   return result

def game():
   money = 100
   print("Game starting, type quit to exit program")
   print("You currently have $" + str(money))
   bet = input("Enter bet amount (min $10)")
   deck = makeCards(8)
   dealerdraw = random.randint(0,len(deck)-1) 
   playerdraw = random.randint(0,len(deck)-1)
   dealerhand = []
   playerhand = []
   dealerhand.append(deck[dealerdraw])
   playerhand.append(deck[playerdraw])
   dealerhandvalue = int(getCardValue(dealerhand[0]))
   playerhandvalue = int(getCardValue(playerhand[0]))
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
      if(playerhandvalue > 21):
         playerhold = True
      if(playerhold == False):
         playerinput = input("Would you like to hit or miss?  ")
         if(playerinput == "hit"):
            playerdraw = random.randint(0,len(deck)-1)
            playerhand.append(deck[playerdraw])
            cardval = getCardValue(playerhand[len(playerhand)-1])
            if(cardval == 0):
               ace = input("Would you like the ace to be 1 or 11?  ")
               playerhandvalue += int(ace)
            else:
               playerhandvalue += int(cardval)
         elif(playerinput == "miss"):
            playerhold = True
      if(dealerhandvalue < 17):
         dealerdraw = random.randint(0,len(deck)-1)
         dealerhand.append(deck[dealerdraw]) 
         cardval = getCardValue(dealerhand[len(dealerhand)-1])
         if(cardval == 0):
            dealerhandvalue += 11
         else:
            dealerhandvalue += int(cardval) 
      else:
         dealerhold = True    
      drawboard(dealerhand, playerhand, dealerhandvalue, playerhandvalue)
      if((dealerhold and playerhold) or (dealerhandvalue > 21 and playerhandvalue > 21)):
         print(whoWins(dealerhandvalue,playerhandvalue) + " wins!") 
         dealerhand = []
         playerhand = []
         dealerhandvalue = 0
         playerhandvalue = 0
         playerhold = False
         dealerhold = False
