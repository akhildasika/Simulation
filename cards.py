deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

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

print(deck)

        
