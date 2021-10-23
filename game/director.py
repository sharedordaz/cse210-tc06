from game import calculator
from game.board import Board
from game.player import Player
from game.console import Console
from game.calculator import Calculator

class Director:
    def __init__(self):
        self.console = Console()
        self.board = Board()
        self.calculator = Calculator()
    def start_game(self):
        self.create_players()
        self.print_game()
        self.assign_numbers()

        while True:
            self.turns()
            win1 = self.calculator.check_if_win(self.player1.info)
            win2 = self.calculator.check_if_win(self.player2.info)
            win3 = self.calculator.check_if_win(self.player3.info)
            if win1 != None: 
                self.console.print_whatever(f"Player 1 won the game")
                break
            elif win2 != None:  
                self.console.print_whatever(f"Player 2 won the game")
                break
            elif win3 != None:
                self.console.print_whatever(f"Player 3 won the game")
                break
            

    def create_players(self):
        player1_name = input("Enter a name for player 1: ")
        player2_name = input("Enter a name for player 2: ")
        player3_name = input("Enter a name for player 3: ")
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player3 = Player(player3_name)

    def assign_numbers(self):
        self.player1.number = self.board.get_number()
        self.player2.number = self.board.get_number()
        self.player3.number = self.board.get_number()


    def print_game(self, guess=["-","-","-","-"]):
        info1 = self.board.get_info(self.player1.name, " ".join(map(str, self.player1.guess)), " ".join(map(str, self.player1.info)))
        info2 = self.board.get_info(self.player2.name, " ".join(map(str, self.player2.guess)), " ".join(map(str, self.player2.info)))
        info3 = self.board.get_info(self.player3.name, " ".join(map(str, self.player3.guess)), " ".join(map(str, self.player3.info)))
        self.console.print_info(info1, info2, info3)

    def turns(self):
        guess = self.player1.ask_number(self.player1.name)
        
        list_guess = self.player1.numToList(guess)

        self.player1.guess = list_guess

        self.player1.info = self.calculator.game_info(self.player1.number, self.player1.guess)
        self.print_game(self)
        #####
        guess = self.player2.ask_number(self.player2.name)
        
        list_guess = self.player2.numToList(guess)

        self.player2.guess = list_guess

        self.player2.info = self.calculator.game_info(self.player2.number, self.player2.guess)
        self.print_game(self)
        #####
        guess = self.player3.ask_number(self.player3.name)
        
        list_guess = self.player3.numToList(guess)

        self.player3.guess = list_guess

        self.player3.info = self.calculator.game_info( self.player3.number, self.player3.guess)
        self.print_game(self)