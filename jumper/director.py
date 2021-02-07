from game.console import Console
from game.jumper import Jumper
from game.word import Word
import random

class Director:

    def __init__(self):
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
    
    def start_game(self):
        #Iniciates the game loop to control the game
        while self.keep_playing:
            self.get_input()
            self.updates()
            self.do_outputs()
        

    def get_input(self):
        #Gets the new guess at the beginning of each round
        message = self.jumper.get_guess()
        self.console.write(message)
        tries = self.console.read_letter()
        self.jumper.move(tries)
        

    def updates(self):
        #Updates the game inforamtion(The jumper watches the word)

        self.word.get_word(self.jumper.tries)



    def do_outputs(self):
        #Outputs the game information for each round(Word & Jumper)
        
        word = self.word.get_word()
        parachute = self.jumper.display_jumper(self.word.tries)
        self.console.write(word)
        self.console.write(parachute)
        self.keep_playing = (self.word.result)
        
