import random

def makeCards(numdecks):
   suit = ["K","Q","J","10","9","8","7","6","5","4","3","2","A"]
   deck = suit
   for i in range(0,numdecks-1):
      for k in range(0,13):
         deck.append(suit[k])
   return deck


