import random

class Card:

    def __init__(self):

        self.keep_playing = True
        while self.keep_playing == True:
            self.draw_card
        else:
            print("Game Over")


    def score(self):
        self.score = 300


    def keep_playing(self):
        
        if self.score > 0:
            choice = input("Keep playing? [y/n]")
            self.keep_playing = (choice == "y")
        elif self.score <= 0:
            print ("Game Over")
        else:
            self.keep_playing = False
