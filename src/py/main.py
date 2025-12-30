#Game loop
from board import Board
from translator import get_piece_name, final_co_ordinate_finder

game_board = Board()

move_list = []
white_turn = True
is_checkmate = False

while not is_checkmate:
    game_board.display()
    if white_turn:
        
        move_input = input("White to move (e.g., e4 or Ra1a2): ")
        
        # Get piece name and destination
        piece_name = get_piece_name(move_input)
        dest_coords = final_co_ordinate_finder(move_input)
        
        if piece_name == "Error":
            print("Invalid format!")
            continue
        
        success = game_board.move(piece_name, "White", dest_coords)
        
        if success:
            white_turn = False
            move_list.append(move_input)
        else:
            print("Illegal move!")
    
    else:
        move_input = input("Black to move (e.g., e5 or ra7a5): ")
        
        # Get piece name and destination
        piece_name = get_piece_name(move_input)
        dest_coords = final_co_ordinate_finder(move_input)
        
        if piece_name == "Error":
            print("Invalid format!")
            continue
        
        success = game_board.move(piece_name, "Black", dest_coords)
        
        if success:
            white_turn = True
            move_list.append(move_input)
        else:
            print("Illegal move!")
        
        



        