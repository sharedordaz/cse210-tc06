from game.board import Board
from game.player import Player
from game.console import Console
from game.calculator import Calculator

class Director:
    pass
    def __init__(self):
        pass
    def start_game(self):
        pass
    def create_players(self):
        player1_name = input("Enter a name for player 1: ")
        player2_name = input("Enter a name for player 2: ")
        player2_name = input("Enter a name for player 3: ")
        player1 = Player(player1_name)
        player2 = Player(player2_name)
        player3 = Player(player3_name)
