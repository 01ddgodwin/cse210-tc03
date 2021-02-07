import random
import string

class Jumper:
    """This is the jumper class. This is the poor victum that is stuck playing this 
    game by your willand wit to save him."""

    def __init__(self):
        """This is the constructor for the jumper class."""
        #self.guess
        # self.tries
        pass

    def get_guess(self):
        """This function gets the guess from the user."""
        guess = input("Guess a letter [a-z]: ").upper()
        return guess


    def display_jumper(self,tries):
        """This function will display the Jumper's situation/stages"""
        stages = [   """
                        ___
                       /___\ 
                       \   /
                        \ /
                         0
                        /|/
                        / /

                      ^^^^^^^ 
                     """,
                     """
            
                       /___\ 
                       \   /
                        \ /
                         0
                        /|/
                        / /

                      ^^^^^^^
                      """,
                      """
                         

                       \   /
                        \ /
                         0
                        /|/
                        / /

                      ^^^^^^^
                      """,
                      """


                      
                        \ /
                         0
                        /|/
                        / /

                      ^^^^^^^
                      """,
                      """


                      
                        
                         X
                        /|/
                        / /

                      ^^^^^^^
                      """


        ]
        return stages[tries]
