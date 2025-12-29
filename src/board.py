from pieces import Pawn, Rook, Queen, King, Bishop, Knight
from main import move_list

#Using 2d vector for chess board mapping

class Board:
    def __init__(self):

        self.grid = [[0 for _ in range(8)] for _ in range(8)]
        
        for i in range(8):
            self.grid[6][i] = Pawn("Black", [6, i])
            self.grid[1][i] = Pawn("White", [1, i])

        # White
        self.grid[0][0] = Rook("White", [0, 0])
        self.grid[0][7] = Rook("White", [0, 7])
        self.grid[0][1] = Knight("White", [0, 1])
        self.grid[0][6] = Knight("White", [0, 6])
        self.grid[0][2] = Bishop("White", [0, 2])
        self.grid[0][5] = Bishop("White", [0, 5])
        self.grid[0][3] = Queen("White", [0, 3])
        self.grid[0][4] = King("White", [0, 4])

        # Black
        self.grid[7][0] = Rook("Black", [7, 0])
        self.grid[7][7] = Rook("Black", [7, 7])
        self.grid[7][1] = Knight("Black", [7, 1])
        self.grid[7][6] = Knight("Black", [7, 6])
        self.grid[7][2] = Bishop("Black", [7, 2])
        self.grid[7][5] = Bishop("Black", [7, 5])
        self.grid[7][3] = Queen("Black", [7, 3])
        self.grid[7][4] = King("Black", [7, 4])

    def move(self, piece_name, color, target_coords):

        target_row, target_col = target_coords

        for r in range(8):
            for c in range(8):
                item = self.grid[r][c]
                

                if item != 0 and item.name == piece_name and item.color == color:
                    

                    self.grid[target_row][target_col] = item

                    self.grid[r][c] = 0

                    item.position = [target_row, target_col]
                    
                    return True 
                    
        return False 
            

my_chess_board = Board()




