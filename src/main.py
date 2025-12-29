#Game loop
from board import Board
from translator import get_piece_name, final_co_ordinate_finder

game_board = Board()

move_list = []
white_turn = True
black_turn = False
is_checkmate = False

while(is_checkmate == False):

    if(white_turn == True):
        
        white_turn_tracker = input("White to move : ")
        white_turn = False
        black_turn = True
        move_list.append(white_turn_tracker)

    elif(black_turn == True):
        black_turn_tracker = input("Black to move : ")
        black_turn = False
        white_turn = True
        move_list.append(black_turn_tracker)
        



        