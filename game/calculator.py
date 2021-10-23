class Calculator:
    """Calculate the numbers and return a correct answer"""
    pass
    def __init__(self):
        pass
    

    def game_info(self, number, guessed_number):
        info = ["*","*","*","*"]
        for x in range(4):
            if number[x-1] == guessed_number[x-1]:
                info[x-1] = ("x")
            elif  (number[x-1] != guessed_number[x-1]) and (guessed_number[x-1] in number):
                info[x-1] = ("o")
            else:
                info[x-1] = ("*")

        return info

    def check_if_win(self,list):
        if list == ["x","x","x","x"]:
            return "won the game"
# x=Calculator
# print(x.game_info(x, [4,4,4,4], [8,4,8,8]))


