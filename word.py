import random

class Word:

    def __init__(self):
        #This constructor uses the word_list to get a random word
        self.word_list = ['chimichaga', 'tortellini', 'turtle', 'pencil', 'death', 'destruction']
        self.word = random.choice(self.word_list)
        self.tries = 0

    def get_word(self):
        #Returns the random word to be used in the director class
        return self.word.upper()
    
    def play(self, letter):
        #Determines if the letter that was guesses is in the word
        result = "Guess the word, or die!"
        if letter in self.word:
            result = f'{letter} is in the word!'
        elif letter not in self.word:
            result = f'{letter} is NOT in the word!'
            self.tries += 1
        return result

        


        # word_completion = "_" * len(word)
        # guessed = False
        # guessed_letters = []
        # guessed_words = []
        # tries = 5