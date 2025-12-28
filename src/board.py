from pieces import Pawn, Rook, Queen, King, Bishop, Knight

#Using 2d vector for chess board mapping

class Board:
    def __init__(self):

        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        
        for i in range(8):
            self.grid[6][i] = Pawn("Black", [6, i])
            self.grid[1][i] = Pawn("White", [1, i])


my_chess_board = Board()




