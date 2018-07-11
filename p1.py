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
      print(dealer[x])
   print("")
   print("---------------")
   print("player's hand")
   print("")
   for x in range(len(player)):
      print(str(player[x]))
   print("")
   print("---------------")  

def game():
   print("Game starting, type quit to exit program")
   deck = makeCards(8)
   number = random.randint(0,len(deck)-1) 
   
