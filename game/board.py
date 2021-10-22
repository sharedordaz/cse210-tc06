import random
class Board:
    """Save the numbers that are guessed"""
    def __init__(self):
        pass
    def get_info(self, p_name, guessed_number, game_info):
        return (f"Player {p_name}: {guessed_number}, {game_info}")

    def get_number(self):
        num_list = []
        number1 = random.randint(0, 9)
        number2 = random.randint(0, 9)
        number3 = random.randint(0, 9)
        number4 = random.randint(0, 9)
        num_list.append(number1)
        num_list.append(number2)
        num_list.append(number3)
        num_list.append(number4)
        return num_list


"""
x = Board()
print(x.get_number())"""
