from pieces import Pawn, Rook, Queen, King, Bishop, Knight
from validator import is_move_valid

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

    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece != 0 and piece.name == "King" and piece.color == color:
                    return piece.position
        return None

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return False

        opponent_color = "Black" if color == "White" else "White"
        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece != 0 and piece.color == opponent_color:
                    if is_move_valid(piece.name, piece.color, king_pos, piece.position, self.grid, color):
                        return True
        return False

    def is_in_checkmate(self, color):
        if not self.is_in_check(color):
            return False

        for r in range(8):
            for c in range(8):
                piece = self.grid[r][c]
                if piece != 0 and piece.color == color:
                    initial_pos = piece.position
                    for tr in range(8):
                        for tc in range(8):
                            target_coords = [tr, tc]
                            target_item = self.grid[tr][tc]
                            target_piece_color = None if target_item == 0 else target_item.color
                            
                            if is_move_valid(piece.name, piece.color, target_coords, initial_pos, self.grid, target_piece_color):
                                # Temporarily make the move
                                original_piece = self.grid[tr][tc]
                                self.grid[tr][tc] = piece
                                self.grid[r][c] = 0
                                piece.position = [tr, tc]

                                # Check if the king is still in check
                                if not self.is_in_check(color):
                                    # Undo the move and return False (not checkmate)
                                    self.grid[r][c] = piece
                                    self.grid[tr][tc] = original_piece
                                    piece.position = initial_pos
                                    return False

                                # Undo the move
                                self.grid[r][c] = piece
                                self.grid[tr][tc] = original_piece
                                piece.position = initial_pos
        
        return True

    def move(self, piece_name, color, target_coords):
        target_row, target_col = target_coords

        # bounds check
        if not (0 <= target_row < 8 and 0 <= target_col < 8):
            return False

        for r in range(8):
            for c in range(8):
                item = self.grid[r][c]
                if item == 0:
                    continue
                if item.name != piece_name or item.color != color:
                    continue

                target_item = self.grid[target_row][target_col]
                target_piece_color = None if target_item == 0 else target_item.color

                if is_move_valid(item.name, item.color, [target_row, target_col], [r, c], self.grid, target_piece_color):
                    # perform move
                    self.grid[target_row][target_col] = item
                    self.grid[r][c] = 0
                    item.position = [target_row, target_col]
                    
                    opponent_color = "Black" if color == "White" else "White"
                    if self.is_in_check(opponent_color):
                        print(f"{opponent_color} is in check!")
                        if self.is_in_checkmate(opponent_color):
                            print(f"Checkmate! {color} wins.")

                    return True

        return False
            
    def display(self):

        print("\n  a b c d e f g h") # Column labels
        for r in range(7, -1, -1): 

            row_string = f"{r+1} "

            for c in range(8):

                item = self.grid[r][c]
                if item == 0:
                    row_string += ". " 
                else:
    
                    char = item.name[0] if item.color == "White" else item.name[0].lower()
                    row_string += f"{char} "

            print(row_string)
        print("  a b c d e f g h\n")
