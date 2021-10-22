class Player:
    """Guess the numbers that you need to guess"""
    pass
    def __init__(self, name):
        self.name = name
    def ask_number(self):
        guess = int(input("What is your guess? "))
        while guess > 9999:
            print("Please write a number of only four digits\n")
            self.ask_number()    
        return guess
        
    def numToList(self, guess):
        guess_list = []
        guess = str(guess)
        for x in guess:
            guess_list.append(x)