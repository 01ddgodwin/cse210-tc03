import random

class Console:

    def __init__(self):
        pass

    def read_letter(self, prompt):

        # Gets text input from the user

        # Args:
        #     self: screen
        #     prompt: The prompt to display to the user
        
        # Returns:
        #     string: The user's input as text

        return input(prompt)

    def write(self, text):

        # Displays the text on the screen

        # Args:
        #     self: screen
        #     text: The text to display

        print(text)
