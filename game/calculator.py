class Calculator:
    """Calculate the numbers and return a correct answer"""
    pass
    def __init__(self):
        pass
    def gen_asterisk(self):
        ast_list = ["*","*","*","*"]
        return ast_list

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