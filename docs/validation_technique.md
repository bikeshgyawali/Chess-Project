Dec 29 2025

For validating moves I am going to have to use mostly math (Which is the fun part!). So I am thinking of a switch case system and returning a true or false. Something like

def func(piece_name) -> bool:
    switch piece_name:
        case "Foo"                                  <--- This structure was not used 
            if capture_type:
                x
            else:
                if x:
                    return True
                else:
                    return False

I can see how difficuly it may get to follow through, but I dont see how OOP would be able to help in this case? Also the validation for each piece is unique so I think it must done in a functional way.

I did implement it, but it feels very iffy. I think im going to leave it up till the knight for today, more tomorrow.

Dec 30 2025

Move validation for the king is done. Of course, it is quite similar to the knight so I could easily just copy and paste the same block. I just add to tweak some offsets and variables.


