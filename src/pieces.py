#Classes for pieces

class Piece():
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position



class Bishop(Piece):
    def __init__(self, color, position):

        super().__init__("Bishop", color, position)

class Knight(Piece):
    def __init__(self, color, position):

        super().__init__("Knight", color, position)

class Rook(Piece):
    def __init__(self, color, position):

        super().__init__("Rook", color, position)

class King(Piece):
    def __init__(self, color, position):

        super().__init__("King", color, position)

class Queen(Piece):
    def __init__(self, color, position):

        super().__init__("Queen", color, position)

class Pawn(Piece):
    def __init__(self, color, position):

        super().__init__("Pawn", color, position)



