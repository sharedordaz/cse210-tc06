class Console:
    """Printer"""
    pass
    def __init__(self):
        pass

    def print_info(self,info1, info2, info3):
        print("\n--------------------")
        print(info1)
        print(info2)
        print(info3)
        print("--------------------\n")

    def print_whatever(self, whatever):
        print(whatever)

    def input_whatever(self, whatever):
        input(whatever)