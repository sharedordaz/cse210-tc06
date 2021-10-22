class Player:
    """Guess the numbers that you need to guess"""
    def __init__(self, name, number=0, guess=[0,0,0,0], info="****"):
        self.name = name
        self.number = number
        self.guess = guess
        self.info = info

    def ask_number(self, user):
        guess = int(input(f"{user}: What is your guess? "))
        if guess > 9999:
            print("Please write a number of only four digits\n")
            self.ask_number()
            print(self.guess)
        return guess

    def numToList(self, guess):
        guess = str(guess)
        guess_list = []

        for x in guess:
            guess_list.append(x)

        return guess_list