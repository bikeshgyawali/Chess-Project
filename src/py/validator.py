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
        
            
                