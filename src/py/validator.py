#Move validation checking

def is_move_valid(piece_name,piece_color,final_pos,initial_pos,game_board,target_piece) -> bool:

    match piece_name:

        case "Knight":

            knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
            for i in knight_moves:

                new_x = i[0] + initial_pos[0]
                new_y = i[1] + initial_pos[1]

                if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
                    continue

                if new_x == final_pos[0] and new_y == final_pos[1]:
                    if target_piece == None:
                        return True
                    if target_piece != piece_color:
                        return True
                    elif target_piece == piece_color:
                        return False
                
            return False

        case "King":
            king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for i in king_moves:

                new_x = i[0] + initial_pos[0]
                new_y = i[1] + initial_pos[1]

                if new_x > 7 or new_x < 0 or new_y > 7 or new_y < 0:
                    continue
                
                if new_x == final_pos[0] and new_y == final_pos[1]:
                    
                    if target_piece == None:
                        return True
                    if target_piece != piece_color:
                        return True
                    elif target_piece == piece_color:
                        return False
                    
            return False
        case "Rook":
            # Rook moves in straight lines along rows or columns
            r0, c0 = initial_pos
            r1, c1 = final_pos

            # must move in same row or same column
            if r0 != r1 and c0 != c1:
                return False

            # determine step direction
            dr = 0 if r1 == r0 else (1 if r1 > r0 else -1)
            dc = 0 if c1 == c0 else (1 if c1 > c0 else -1)

            # check path is clear (exclude final square)
            cr, cc = r0 + dr, c0 + dc
            while (cr, cc) != (r1, c1):
                if game_board[cr][cc] != 0:
                    return False
                cr += dr; cc += dc

            # final square must be empty or contain opponent
            if target_piece == None:
                return True
            return target_piece != piece_color

        case "Bishop":
            # Bishop moves diagonally
            r0, c0 = initial_pos
            r1, c1 = final_pos
            if abs(r1 - r0) != abs(c1 - c0):
                return False

            dr = 1 if r1 > r0 else -1
            dc = 1 if c1 > c0 else -1

            cr, cc = r0 + dr, c0 + dc
            while (cr, cc) != (r1, c1):
                if game_board[cr][cc] != 0:
                    return False
                cr += dr; cc += dc

            if target_piece == None:
                return True
            return target_piece != piece_color

        case "Queen":
            # Queen is rook + bishop
            r0, c0 = initial_pos
            r1, c1 = final_pos

            # straight
            if r0 == r1 or c0 == c1:
                dr = 0 if r1 == r0 else (1 if r1 > r0 else -1)
                dc = 0 if c1 == c0 else (1 if c1 > c0 else -1)
                cr, cc = r0 + dr, c0 + dc
                while (cr, cc) != (r1, c1):
                    if game_board[cr][cc] != 0:
                        return False
                    cr += dr; cc += dc
                if target_piece == None:
                    return True
                return target_piece != piece_color

            # diagonal
            if abs(r1 - r0) == abs(c1 - c0):
                dr = 1 if r1 > r0 else -1
                dc = 1 if c1 > c0 else -1
                cr, cc = r0 + dr, c0 + dc
                while (cr, cc) != (r1, c1):
                    if game_board[cr][cc] != 0:
                        return False
                    cr += dr; cc += dc
                if target_piece == None:
                    return True
                return target_piece != piece_color

            return False

        case "Pawn":
            # Pawn moves depend on color and captures
            r0, c0 = initial_pos
            r1, c1 = final_pos

            direction = 1 if piece_color == "White" else -1
            start_row = 1 if piece_color == "White" else 6

            # forward one
            if c0 == c1 and r1 == r0 + direction:
                if target_piece == None:
                    return True
                else:
                    return False

            # forward two from starting position
            if c0 == c1 and r0 == start_row and r1 == r0 + 2 * direction:
                mid_r = r0 + direction
                if game_board[mid_r][c0] == 0 and target_piece == None:
                    return True
                return False

            # capture diagonally
            if abs(c1 - c0) == 1 and r1 == r0 + direction:
                if target_piece != None and target_piece != piece_color:
                    return True
                return False

            return False



