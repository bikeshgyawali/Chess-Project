#Function to find the final co-ordinate the "attacking" piece is going to go to

def final_co_ordinate_finder(strs):

    final_rank = int(strs[len(strs)-1])-1

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
    
def piece_type_finder(strs):
    if(len(strs) == 2):
        return "Pawn"
    elif(strs[0].upper() == "R"):
        return  "Rook"
    elif(strs[0].upper() == "N"):
        return  "Knight"
    elif(strs[0].upper() == "B"):
        return  "Bishop"
    elif(strs[0].upper() == "Q"):
        return  "Queen"
    elif(strs[0].upper() == "K"):
        return  "King"
    else:
        return "Error"
    


