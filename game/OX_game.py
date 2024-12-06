class OXGame:

    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print(" ".join(row))

    def make_move(self, x,y):
        if 0 <= x < 3 and 0 <= y < 3:
            if self.board[x][y] != '-':
                print("Already Occupied !!")
                return False
            else:
                self.board[x][y] = self.current_player
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                return True
        else:
            print("Invalid Cordinates !!")
            return False

                
