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
        self.turns()

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


    def print_game(self):

        info1 = self.board.get_info(self.player1.name, self.player1.number, self.player1.info)
        info2 = self.board.get_info(self.player2.name, self.player2.number, self.player2.info)
        info3 = self.board.get_info(self.player3.name, self.player3.number, self.player3.info)
        self.console.print_info(info1, info2, info3)

    def turns(self):
        self.player1.ask_number(self.player1.name)
        self.player1.info = self.calculator.game_info(self.player1.number, self.player1.guess)
        self.print_game()