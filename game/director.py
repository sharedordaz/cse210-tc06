from game.board import Board
from game.player import Player
from game.console import Console
from game.calculator import Calculator

class Director:
    def __init__(self):
        self.console = Console()
        self.board = Board()
    def start_game(self):
        pass
    def create_players(self):
        player1_name = self.console.input_whatever("Enter a name for player 1: ")
        player2_name = self.console.input_whatever("Enter a name for player 2: ")
        player3_name = self.console.input_whatever("Enter a name for player 3: ")
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.player3 = Player(player3_name)

    def game(self):

        info1 = self.board.get_info(self.player1)
        info2 = self.board.get_info(self.player2)
        info3 = self.board.get_info(self.player3)
        
        self.console.print_info(info1, info2, info3)


