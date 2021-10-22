class Player:
    """Guess the numbers that you need to guess"""
    pass
    def __init__(self, name):
        self.name = name
    def ask_number(self):
        guess = input("What is your guess? ")
        return guess
