#Function to find the final co-ordinate the "attacking" piece is going to go to

def final_co_ordinate_finder(strs):

    final_rank = 8 - int(strs[len(strs)-1])

    #Hash map to define the a-h files with nums

    hash = {
        "a" : 0,
        "b" : 1,
        "c" : 2,
        "d" : 3,
        "e" : 4,
        "f" : 5,
        "g" : 6,
        "h" : 7
    }

    alpha_placeholder = strs[len(strs)-2]

    final_file = hash[alpha_placeholder]

    return [final_rank,final_file]

#Function to determine if the move inputted is a capture type

def is_capture_move(strs):
    if(strs[1].upper() == "X"):
        return True
    else:
        return False
    
#Function to find the piece type from notation
    
def get_piece_name(strs: str) -> str:
    
    if len(strs) == 2:
        return "Pawn"

    piece_map = {
        "R": "Rook",
        "N": "Knight",
        "B": "Bishop",
        "Q": "Queen",
        "K": "King"
    }
   
    first_char = strs[0].upper()


    return piece_map.get(first_char, "Error")


    

