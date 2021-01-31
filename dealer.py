from game.card import Card

import random

class Dealer:

    def __init__(self):

        self.card1 = random.randinit(1, 13)
        self.card2 = random.randinit(1, 13)

        self.card = Card()

    def draw_card(self):
        print(f"The current card is {self.card1}")
        card1 = random.randint(1, 13)
        player_guess = print(input("Higher or lower? [h/l]"))
        print("The card is:", self.card2)
        if card1 > self.card2 and player_guess == "l":
            #score goes up 100
            print("Correct")
            self.score += 100
        elif card1 > self.card2 and player_guess == "h":
            #score goes down 75
            print('Wrong')
            self.score -= 75
        elif card1 < self.card2 and player_guess == "l":
            #score goes up 100
            print('Correct!')
            self.score += 100
        elif card1 < self.card2 and player_guess == "h":
            #score goes down 75
            print("Wrong")
            self.score -= 75
                
        

    # def keep_playing(self):

    #     print(card1)
        
    #     if self.dealer.can_draw():
    #         choice = input("Keep playing? [y/n]")
    #         self.keep_playing = (choice == "y")
    #     else:
    #         self.keep_playing = False
