import random
import sys

deck = []
suits = ["♠", "♥", "♦", "♣"]
d=[]
s=["♠","♥","♦","♣"]
f={1:"A",11:"J",12:"Q",13:"K"}

for i in range (1, 4):
    for o in range(1, 14):
        if(o == 1):
            value = "A"
        elif(o == 2):
            value = "2"
        elif(o == 3):
            value = "3"
        elif(o == 4):
            value = "4"
        elif(o == 5):
            value = "5"
        elif(o == 6):
            value = "6"
        elif(o == 7):
            value = "7"
        elif(o == 8):
            value = "8"
        elif(o == 9):
            value = "9"
        elif(o == 10):
            value = "10"
        elif(o == 11):
            value = "J"
        elif(o == 12):
            value = "Q"
        elif(o == 13):
            value = "K"
        deck.append(f"[{value} {suits[i]}]")

    

def randomize (deck): 
    for i in range(o-1,0,-1): 
        j = random.randint(0,i+1) 
  

        deck[i],deck[j] = deck[j],deck[i] 
    return deck

def deal(deck):
    d=[]
    s=["♠","♥","♦","♣"]
    f={1:"A",11:"J",12:"Q",13:"K"}
    for i in range(4):
        for j in range(1,14):
            d.append(f"{f[j] if j in f else j}{s[i]}")
    return d

def selectionSort(s, f):
   d=[]
   for i in range(len(s)):

     
       minPosition = i

       for j in range(i+1, len(s)):
           if s[minPosition] > s[j]:
               minPosition = j
                
       temp = s[i]
       s[i] = s[minPosition]
       s[minPosition] = temp         
       temp = s[i]
       f[i] = f[minPosition]
       f[minPosition] = temp
       f[minPosition] = temp
d.append(f"{f[j] if i in f else j}{s[j]}")   

print(deal(deck))
print("shuffled deck") 
print(randomize(deck))
print("sorted deck")
print(selectionSort(s, f))
        
