class OXGame:

    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]

    def display_board(self):
        for row in self.board:
            print(" ".join(row))