import Functionality.constants as c
import Functionality.movement_functions as mf

def evaluate_line_movement(
        current_column: int,
        current_row: int, 
        valid_directions: list[tuple],
        direction_types:list[str],
        eval_occupied_squares:list[dict[str:str, str:str, str:str]],
        piece_color: str,
        direction_loop_idx = 0,
        to_check_column = None, 
        to_check_row = None,
        position_valid = True # starting out as true, exiting recursion whenever False
        ) -> bool:
    
    # should never happen
    if len(valid_directions) == 0:
        raise Exception("No valid direction to evaluate")
    
    # found opponent piece with striking line on king. Position not valid
    if position_valid is False:
        return False 
    
    # if this base case is reached all directions are valid, 
    # so king not at check on evaluated board state
    if direction_loop_idx >= len(valid_directions):
        return True 
    
    to_check_direction = valid_directions[direction_loop_idx]
    if to_check_column is None and to_check_row is None:
        to_check_column = current_column + to_check_direction[c.COLUMN_IDX]
        to_check_row = current_row + to_check_direction[c.ROW_IDX]
    else:
        to_check_column = to_check_column + to_check_direction[c.COLUMN_IDX]
        to_check_row = to_check_row + to_check_direction[c.ROW_IDX]

    # not within board range, moving on to next direction loop
    if to_check_column not in c.BOARD_COLUMNS.keys() or to_check_row not in c.BOARD_ROWS:
        direction_loop_idx += 1
        # resetting for next direction loop
        to_check_column = None
        to_check_row = None
        # only direction loop is edited, square not within board range
        return evaluate_line_movement(
                                        current_column, 
                                        current_row, 
                                        valid_directions, 
                                        direction_types, 
                                        eval_occupied_squares, 
                                        piece_color, 
                                        direction_loop_idx,
                                        to_check_column,
                                        to_check_row,
                                        position_valid
                                    )
    else:
        square_occupied_by_line_striking_piece = \
        check_if_square_occupied(
                                    to_check_column, 
                                    to_check_row, 
                                    piece_color, 
                                    direction_types, 
                                    eval_occupied_squares
                                )
        if square_occupied_by_line_striking_piece:
            # Found opponent piece in striking line, 
            # setting position valid to trigger base case
            position_valid = False

        elif square_occupied_by_line_striking_piece is False:
            # found own piece, go to next direction, resetting to_check_column and row
            direction_loop_idx += 1
            to_check_column = None
            to_check_row = None
            position_valid = True

        else: # don't reset to_check_column and row so next position in line will be evaluated
            pass

        # recursive case with edited values
        return evaluate_line_movement(
                                        current_column, 
                                        current_row, 
                                        valid_directions, 
                                        direction_types, 
                                        eval_occupied_squares, 
                                        piece_color, 
                                        direction_loop_idx,
                                        to_check_column,
                                        to_check_row,
                                        position_valid
                                    ) 

def evaluate_single_movement(
            current_column: int, 
            current_row: int,
            valid_directions: list[tuple], 
            direction_type: list[str],
            eval_occupied_squares: list[dict[str:str, str:str, str:str]], 
            piece_color: str
        ):
    for valid_direction in valid_directions:
        to_check_column = None
        to_check_row = None
        to_check_column = current_column + valid_direction[c.COLUMN_IDX]
        to_check_row = current_row + valid_direction[c.ROW_IDX]
        if to_check_column not in c.BOARD_COLUMNS.keys() or to_check_row not in c.BOARD_ROWS:
            continue
        else:
            square_occupied_by_opponent_king_or_knight = \
                    check_if_square_occupied(
                        to_check_column, 
                        to_check_row, 
                        piece_color, 
                        direction_type, 
                        eval_occupied_squares
                    )
            if square_occupied_by_opponent_king_or_knight:
                # opponent king or knight found on diagonal squares opposite side of player color
                # position not valid
                return False
            else:
                continue
    # all directions checked, no Knight or King found
    return True


# valid directions in arguments so function can be called the same way as other movement functions
# from dict at the bottom of this file    
def evaluate_pawn_movement(
            current_column: int, 
            current_row: int,
            valid_directions: list[tuple],
            direction_type: list[str],
            eval_occupied_squares: list[dict[str:str, str:str, str:str]], 
            piece_color: str
        ):
    column_increment = [1, -1]

    for increment in column_increment:
        to_check_column = None
        to_check_row = None
        to_check_column = current_column + increment
        # check on piece color, white king looks down, black pawn strikes up
        if piece_color == "WHITE":
            to_check_row = current_row + 1
        elif piece_color == "BLACK":
            to_check_row = current_row - 1
        else:
            raise Exception("piece_color neither black or white, should never happen")
         
        if to_check_column not in c.BOARD_COLUMNS.keys() or to_check_row not in c.BOARD_ROWS:
            continue
        else:
            square_occupied_by_opponent_pawn = \
            check_if_square_occupied(
                    to_check_column, 
                    to_check_row, 
                    piece_color, 
                    direction_type, 
                    eval_occupied_squares
                )
            if square_occupied_by_opponent_pawn:
                # opponent pawn found on diagonal squares opposite side of player color, so position not valid
                return False
            else:
                continue
    # no opponent pawn found on diagonal squares opposite side of player color
    return True

'''might want to rewrite this. Fixed issue where a square can be occupied by pieces of two colors'''
def check_if_square_occupied(
        to_check_column: int,
        to_check_row: int, 
        piece_color: str, 
        direction_types: list[str], 
        eval_occupied_squares: list[dict[str, str, str]]
        ):
    for occ_square_dict in eval_occupied_squares:
        occ_square_position = occ_square_dict["position"] 
        occ_square_color = occ_square_dict["color"]
        occ_square_type = occ_square_dict["type"]
        occ_square_col = int(occ_square_position[c.COLUMN_IDX])
        occ_square_row = int(occ_square_position[c.ROW_IDX])

        if occ_square_col == to_check_column and occ_square_row == to_check_row:
            if occ_square_color == piece_color:
               # own piece found so king is not in check state 
               # (could be after own piece has striked opponent piece on this square)
               return False

    # looping again, because two pieces can be on the same occupied_square, since opponent piece is not yet striked
    for occ_square_dict in eval_occupied_squares:
        occ_square_position = occ_square_dict["position"] 
        occ_square_color = occ_square_dict["color"]
        occ_square_type = occ_square_dict["type"]
        occ_square_col = int(occ_square_position[c.COLUMN_IDX])
        occ_square_row = int(occ_square_position[c.ROW_IDX])
        # check if current square is in occupied squares
        if occ_square_col == to_check_column and occ_square_row == to_check_row:
            # found occupied square, checking for opponent pieces
            if occ_square_color != piece_color:
                # checking if opponent piece can strike the king
                for dir in direction_types:
                    if dir == occ_square_type:
                        #o pponent piece found that can strike the king
                        return True
                    # opponent piece found, but isn't able to strike based on the direction type
                return False
            
            else:
                raise Exception("This should never happen. occupied square doesn't have a color")
        else:
            continue
    
    return None 

def evaluate_position(
        piece_color: str, 
        eval_occupied_squares: dict[str:str, str:str, str:str],
        position_eval_type = c.CHECK_EVAL,
        to_check_square = None):
    if position_eval_type == c.CHECK_EVAL:
        for idx, occupied_square in enumerate(eval_occupied_squares):
            try:
                # retrieve king position on eval_board
                if occupied_square["type"] == "king" and occupied_square["color"] == piece_color:
                    king_square = eval_occupied_squares[idx]
                    king_position = king_square["position"]
                    king_position_column = int(king_position[c.COLUMN_IDX])
                    king_position_row = int(king_position[c.ROW_IDX])
            except UnboundLocalError as e:
                print(f"you beat the developer, king removed from board shown by this error: {e}")
    else:
        king_position = to_check_square
        king_position_column = int(king_position[c.COLUMN_IDX])
        king_position_row = int(king_position[c.ROW_IDX])
    # From king position go to squares in all possible directions and check for occupation on squares
    # If occupied by opponent piece and it can strike king based on the striking move set of that piece:
    # position is not valid
    for eval_func_dir in EVAL_FUNCTIONS_AND_DIRECTIONS: # dict is on the bottom of this file
        movement_direction = eval_func_dir["movement"]
        direction_type = eval_func_dir["direction_type"]
        movement_function = eval_func_dir["function"]
        square_available = movement_function(
                                                king_position_column, 
                                                king_position_row, 
                                                movement_direction,
                                                direction_type,
                                                eval_occupied_squares,
                                                piece_color
                                            )
        if square_available is False:
            return False
        
        else:
            # go to next movement direction 
            continue
    # all movement directions checked, opponent not able to check the king when player piece is 
    # moved to this square so square is available
    return True


STRAIGHT_DIRECTIONS = mf.get_valid_straight_directions()
DIAGONAL_DIRECTIONS = mf.get_valid_diagonal_directions()
KNIGHT_DIRECTIONS = mf.get_valid_knight_directions()
KING_DIRECTIONS = mf.get_valid_king_directions()
    
EVAL_FUNCTIONS_AND_DIRECTIONS = [
    {
     "movement": STRAIGHT_DIRECTIONS
    ,"direction_type" : ["queen", "rook"]
    ,"function" : evaluate_line_movement
    },
    {
     "movement": DIAGONAL_DIRECTIONS
    ,"direction_type" : ["queen", "bishop"]
    ,"function" : evaluate_line_movement
    }, 
    {
     "movement": KNIGHT_DIRECTIONS
    ,"direction_type" : ["knight"]
    ,"function" : evaluate_single_movement
    }, 
    {
     "movement": [(0, 0)] # default value, isn't used in function
    ,"direction_type" : ["pawn"]
    ,"function" : evaluate_pawn_movement
    }, 
    {
     "movement": KING_DIRECTIONS
    ,"direction_type" : ["king"]
    ,"function" : evaluate_single_movement
    }]