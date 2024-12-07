class OXGame:

    def __init__(self):
        self.board = [['-'] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.check_status = "Continue"
        self.game_over = False

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
        
    def check_game_status(self):
        for i in range(3):
             #縦の判定
             if self.board[i][0] == self.board[i][1] == self.board[i][2] != '-':
                self.check_status = f"{self.board[i][0]} Wins"
                self.game_over = True
                return self.check_status
            #横の判定
             if self.board[0][i] == self.board[1][i] == self.board[2][i] != '-':
                self.check_status = f"{self.board[0][i]} Wins"
                self.game_over = True
                return self.check_status
            #斜めの判定
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            self.check_status = f"{self.board[1][1]} Wins"
            self.game_over = True
            return self.check_status
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            self.check_status = f"{self.board[1][1]} Wins"
            self.game_over = True
            return self.check_status

        if self.game_over != False and all(self.board[x][y] != '-' for x in range(3) for y in range(3)):
                self.check_status = "DRAW"
                self.game_over = True
                return self.check_status
        self.check_status = "Continue"
        return self.check_status
    
    def reset_or_exit(self):
        while True:
            choice = input("Type 'reset' to restart or 'exit' to quit: ").lower()
            if choice == 'reset':
                self.__init__()
                print("Shall We Play A Game ?")
                return
            elif choice == 'exit':
                print("Bye !")
                exit()
            else:
                print("Invalid input. You can choose 'reset' or 'exit'.")

            