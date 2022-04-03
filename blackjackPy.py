#######################
# Ryan Anderson
# Black Jack in Python!
#######################


import random


class BlackJackHand:
    def __init__(self):
        self.handVal = 0
        self.cards = []
        self.aces = 0
        self.elevens = 0

    def hit(self):
        card = random.randrange(1,13)
        if card == 1:
            if(self.handVal < 11):      #We keep track of aces and elevens to know when to properly adjust deck value <21
                self.handVal += 11
                self.elevens += 1
            elif(self.handVal>10):
                self.handVal += 1
                self.aces += 1          
            self.cards.append("Ace ")
        elif card == 2:
            self.handVal +=2
            self.cards.append("2 ")
        elif card == 3:
            self.handVal +=3
            self.cards.append("3 ")
        elif card == 4:
            self.handVal +=4
            self.cards.append("4 ")
        elif card == 5:
            self.handVal +=5
            self.cards.append("5 ")
        elif card == 6:
            self.handVal +=6
            self.cards.append("6 ")
        elif card == 7:
            self.handVal +=7
            self.cards.append("7 ")
        elif card == 8:
            self.handVal +=8
            self.cards.append("8 ")
        elif card == 9:
            self.handVal +=9
            self.cards.append("9 ")
        elif card == 10:
            self.handVal +=10
            self.cards.append("10 ")
        elif card == 11:
            self.handVal +=10
            self.cards.append("Jack ")
        elif card == 12:
            self.handVal +=10
            self.cards.append("Queen ")
        elif card == 13:
            self.handVal +=10
            self.cards.append("King ")

        #####Ace 1 or 11 updating#######
        if self.handVal > 21 and self.elevens > 0:
            self.handVal -= 10
            self.elevens -= 1
            self.aces += 1
            

    def clearHand(self):
        self.handVal = 0
        self.cards.clear()
        self.aces = 0


def loseGame(pHand, dHand):
    print("###############You lose!###################")
    print("###########################################")
    pHand.clearHand()
    dHand.clearHand()
    newGamePrompt(pHand, dHand)

def winGame(pHand, dHand):
    print("***************You WIN!*******************")
    print("******************************************")
    pHand.clearHand()
    dHand.clearHand()
    newGamePrompt(pHand, dHand)

def pushGame(pHand, dHand):
    print("*#*#*#*#*#*#*#*You Pushed*#*#*#*#*#*#*#*#*")
    print("*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    pHand.clearHand()
    dHand.clearHand()
    newGamePrompt(pHand, dHand)

def printPlayer(pHand):
    print("           Your hand: ")
    print("".join(map(str, pHand.cards)))
    print("\nTotal: ", pHand.handVal)
    print("###########################################")

def printDealer(dHand):
    print("###########################################")
    print("           Dealer hand: ")
    print("".join(map(str, dHand.cards)))
    print("\nDealer total: ", dHand.handVal)
    print("///////////////////////////////////////////")

def newGamePrompt(pHand, dHand):
    pInput = input("Play again? { y/n }: ")
    print("\n")
    if pInput == "n":
        self.playing = 0
    if pInput == "y":
        newGame(pHand, dHand)

def newGame(pHand, dHand):
    dHand.hit()         #Begin dealer hand
    printDealer(dHand)

    pHand.hit()         #Begin player hand
    printPlayer(pHand)



            
def main():

    playing = 1
    
    playerHand = BlackJackHand()
    dealerHand = BlackJackHand()

    newGame(playerHand, dealerHand)

    while(playing):

        if playerHand.handVal > 21: #Player Busts for >21
            loseGame(playerHand, dealerHand)


        pInput = input("What would you like to do? { stay }{ hit }{ quit }: ")


        if pInput == "quit":
            playing = 0

        if pInput == "hit": 
            printDealer(dealerHand)
            playerHand.hit()
            printPlayer(playerHand)

        if pInput == "stay":  #Dealer must now hit
            while dealerHand.handVal <= 17:

                dealerHand.hit()
                printDealer(dealerHand)


            if(dealerHand.handVal > 21): #dealer busts
                winGame(playerHand, dealerHand)

            elif playerHand.handVal > dealerHand.handVal: #player beats dealer
                winGame(playerHand, dealerHand)

            elif playerHand.handVal == dealerHand.handVal: #dealer and player push
                pushGame(playerHand, dealerHand)

            elif playerHand.handVal < dealerHand.handVal: #dealer beats player
                loseGame(playerHand, dealerHand)

if __name__ == '__main__':
    main()