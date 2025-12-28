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



    
    

    