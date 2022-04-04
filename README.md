# BlackJack



Command line Blackjack!

Player is shown their hand and a dealer hand, then is asked to either hit, stay or quit:
#
---Hit - A player will draw a card, add it to their displayed hand, and add its value to their hand

        - If the player goes beyond 21 by hitting, they will lose
        
---Quit - Exit game

---Stay - The player is done drawing cards and next the dealer will draw until they go beyond 16 in hand value

#
After Dealer is done hitting:

--- Win - If the dealer has a lower value hand than the player OR the dealer busts by going above 21, the player wins

--- Lose - If the dealer has a higher value hand than the player OR the player previously went beyond 21, they will lose

--- Push - If the dealer and the player have the same value hand, they tie (push)

#
Some interesting Notes:

--- Aces ---

While blackjack is a solved game, some interesting developments came when determining how aces are handled. Every card has one value in BlackJack except for an ace.

-- To solve the double value issue we use a counter to keep track of if the BlackJack hand has an Ace as an Eleven

    -If the hand goes beyond 21 and there exists an Ace that is calculated as an 11, we now remove an Eleven, add a one, and remove 10 in value from the hand
    
--- Suits ---

If using suits for a single deck game (perhaps for card counting practice). I would suggest expanding the pool of cards to 52 to prevent duplicates. Since most BlackJack is played with multiple decks, suits become irrelevant and could just be randomized on draw
