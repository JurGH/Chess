import Functionality.constants as ca

# should be called at initialization of piece, depending on the piece type
def get_valid_straight_directions() -> list[tuple]:
    column_movement_directions = [1, 0, -1]
    row_movement_directions = [1, 0, -1]
    valid_directions: list[tuple]
    valid_columns = []
    valid_rows = []
    valid_directions = []
    for col_move_d in column_movement_directions:
        for row_move_d in row_movement_directions:
            if abs(col_move_d) != abs(row_move_d):
                valid_columns.append(col_move_d)
                valid_rows.append(row_move_d)
            else:
                continue
    valid_directions = list(zip(valid_columns, valid_rows))
    if len(valid_directions) == 0:
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    else:
        return valid_directions

# should be called at initialization of piece, depending on the piece type
def get_valid_diagonal_directions() -> list[tuple]:
    column_movement_directions = [1, -1]
    row_movement_directions = [1, -1]
    valid_directions: list[tuple]
    valid_columns = []
    valid_rows = []
    valid_directions = []
    for col_move_d in column_movement_directions:
        for row_move_d in row_movement_directions:
            valid_columns.append(col_move_d)
            valid_rows.append(row_move_d)
    valid_directions = list(zip(valid_columns, valid_rows))
    if len(valid_directions) == 0:
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    return valid_directions

# need to write this
def get_valid_knight_directions() -> list[tuple]:
    column_movement_directions = [1, 2, -2, -1]
    row_movement_directions = [1, 2, -2, -1]
    valid_directions: list[tuple]
    valid_directions = []
    valid_columns = []
    valid_rows = []
    for col_move_d in column_movement_directions:
        for row_move_d in row_movement_directions:
            # knight movement is always 2 cols up/down 1 row up/down or the other way around.
            if abs(row_move_d) == abs(col_move_d):
                continue
            elif abs(row_move_d) != abs(col_move_d):
                valid_columns.append(col_move_d)
                valid_rows.append(row_move_d)
    valid_directions = list(zip(valid_columns, valid_rows))
    if len(valid_directions) == 0:
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    return valid_directions
    
def get_valid_king_directions() -> list[tuple]:
    column_movement_directions = [1, 0, -1]
    row_movement_directions = [1, 0, -1]
    valid_directions: list[tuple]
    valid_directions = []
    valid_columns = []
    valid_rows = []
    for col_move_d in column_movement_directions:
        for row_move_d in row_movement_directions:
            if col_move_d == 0 and row_move_d == 0:
                continue
            else:
                valid_columns.append(col_move_d)
                valid_rows.append(row_move_d)
    valid_directions = list(zip(valid_columns, valid_rows))
    if len(valid_directions) == 0: 
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    return valid_directions

def get_pawn_first_move_direction(piece_color: str):
    col_move_d = 0
    if piece_color == "WHITE":
        row_move_d = 2
    elif piece_color == "BLACK":
        row_move_d = -2
    first_move_direction = [(col_move_d, row_move_d)]
    if len(first_move_direction) == 0: 
        raise Exception(f"No movement combinations were added. length of list = {len(first_move_direction)}")
    return first_move_direction

# only for the pawn there should be two movement sets. One for regular moves (either +1 or -1 rows, depending on color)
# and the striking direction, which is alway diagonal, where the row is either +1 or -1 based on color.
def get_valid_pawn_regular_directions(piece_color: str) -> list[tuple]:
    col_move_d = 0
    if piece_color == "WHITE":
        row_move_d = 1
    elif piece_color == "BLACK":
        row_move_d = -1
    valid_directions = [(col_move_d, row_move_d)]
    if len(valid_directions) == 0: 
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    return valid_directions

def get_valid_pawn_striking_directions(piece_color) -> list[tuple]:
    column_movement_directions = [1, -1]
    valid_directions: list[tuple]
    valid_directions = []

    if piece_color == "WHITE":
        row_move_d = 1
    elif piece_color == "BLACK":
        row_move_d = -1

    for col_move_d in column_movement_directions:
        valid_directions.append((col_move_d, row_move_d))
    if len(valid_directions) == 0: 
        raise Exception(f"No movement combinations were added. length of list = {len(valid_directions)}")
    return valid_directions

# recursive function
def get_available_positions_in_line_movement(
        current_column: int, 
        current_row: int, 
        valid_directions: list[tuple], 
        occupied_squares: list[dict[str, str, str]],
        piece_color: str, 
        available_positions=[],
        direction_loop_idx=0, 
        to_check_column=None,
        to_check_row=None
        ):
    
    available_positions: list[tuple]
    to_loop_direction: tuple

    # Only base case needed: check if all directions are evaluated
    if direction_loop_idx >= len(valid_directions):
        return available_positions
    
    to_loop_direction = valid_directions[direction_loop_idx]
    available_positions = available_positions

    if len(valid_directions) == 0:
        raise Exception("no valid direction was entered in get_available_movement function")
    
    # first loop of current direction
    if to_check_column is None and to_check_row is None:
        to_check_column = current_column + to_loop_direction[ca.COLUMN_IDX]
        to_check_row = current_row + to_loop_direction[ca.ROW_IDX]

    else: # any loop after the first of current direction
        to_check_column = to_check_column + to_loop_direction[ca.COLUMN_IDX]
        to_check_row = to_check_row + to_loop_direction[ca.ROW_IDX]

    # checking if position is still within the board
    if to_check_column not in ca.BOARD_COLUMNS.keys() or to_check_row not in ca.BOARD_ROWS:
        direction_loop_idx += 1
        # start next recursive case with edited values
        return get_available_positions_in_line_movement(
                current_column, 
                current_row, 
                valid_directions, 
                occupied_squares, 
                piece_color,
                available_positions, 
                direction_loop_idx
                )
    
    else: # position is within the board grid
        square_occupied = check_if_square_occupied(to_check_column, to_check_row, piece_color, occupied_squares)
        if len(square_occupied) == 2:
            direction_loop_idx += 1
            # reset column and row, because new direction will be used in next loop
            to_check_column = None
            to_check_row = None
            position = square_occupied[1]
            if position not in available_positions:
                # opponent piece found on square, adding square to available positions
                available_positions.append(position)
            else:
                pass

        elif len(square_occupied) == 1:
            if square_occupied[0] is True:
                direction_loop_idx += 1
                # reset column and row, because new direction will be used in next loop
                to_check_column = None
                to_check_row = None
            else:
                # don't reset column and row because the same direction will be used in next loop. 
                # square not occupied. adding square to available positions
                available_positions.append((to_check_column, to_check_row))

        # starting next recursive case with edited values
        return get_available_positions_in_line_movement(
                current_column, 
                current_row, 
                valid_directions, 
                occupied_squares,
                piece_color,
                available_positions,
                direction_loop_idx, 
                to_check_column,
                to_check_row
                )

def get_available_regular_pawn_move_positions(
        current_column: int,
        current_row: int,
        valid_directions: list[tuple],
        occupied_squares: list[dict[str, str, str]],
        piece_color: str
        ) -> list[tuple]:
    
    available_positions: list[tuple]
    available_positions = []
    #index 0 is the only tuple in the list
    to_check_column = current_column + valid_directions[0][ca.COLUMN_IDX]
    to_check_row = current_row + valid_directions[0][ca.ROW_IDX]

    if piece_color == "WHITE" and current_row == max(ca.BOARD_ROWS):
        print("Shouldn't happen, pawn should not exist on this square anymore")
        return []
    elif piece_color == "BLACK" and current_row == min(ca.BOARD_ROWS):
        print("Shouldn't happen, pawn should not exist on this square anymore")
        return []
    
    if to_check_column not in ca.BOARD_COLUMNS.keys() or to_check_row not in ca.BOARD_ROWS:
        return
    else:
        square_occupied = check_if_square_occupied(to_check_column, to_check_row, piece_color, occupied_squares)
        if square_occupied[0] is False:
            # no piece found in square with regular pawn move, so square is available. 
            available_positions.append((to_check_column, to_check_row))
        elif square_occupied[0] is True:
            # opponent piece found in square with regular pawn move, so square not available. 
            pass
        else:
            raise Exception("Should never happen, occupied square should always either be true or false")
    return available_positions 

def get_available_pawn_striking_positions(
        current_column: int, 
        current_row: int,
        valid_directions: list[tuple],
        occupied_squares: list[dict[str, str, str]],
        piece_color: str
        ):
    available_positions: list[tuple]
    available_positions = []
    for valid_direction in valid_directions:
        to_check_column = current_column + valid_direction[ca.COLUMN_IDX]
        to_check_row = current_row + valid_direction[ca.ROW_IDX]
        if to_check_column not in ca.BOARD_COLUMNS.keys() or to_check_row not in ca.BOARD_ROWS:
            continue
        else:
            square_occupied = check_if_square_occupied(to_check_column, to_check_row, piece_color, occupied_squares)
            if square_occupied[0] is False:
                # no piece found in square with striking pawn move, so square is not available. 
                pass
            #piece found in square
            elif square_occupied[0] is True:
                if len(square_occupied) == 2: #opponent piece found
                    available_positions.append((to_check_column, to_check_row))
                else: #own piece found
                    pass
            else:
                raise Exception("Should never happen, occupied square should always either be true or false")
    return available_positions    

def get_available_single_movement_positions(
        current_column: int,
        current_row: int, 
        valid_directions: list[tuple], 
        occupied_squares: list[dict[str, str, str]],
        piece_color: str
        ):
    available_positions: list[tuple]
    available_positions = []
    for valid_direction in valid_directions:
        to_check_column = current_column + valid_direction[ca.COLUMN_IDX]
        to_check_row = current_row + valid_direction[ca.ROW_IDX]
        if to_check_column not in ca.BOARD_COLUMNS.keys() or to_check_row not in ca.BOARD_ROWS:
            continue
        else:
            square_occupied = check_if_square_occupied(to_check_column, to_check_row, piece_color, occupied_squares)
            if square_occupied[0] is False:
                # no piece found in square so square is available. 
                available_positions.append((to_check_column, to_check_row))
            # piece found on square
            elif square_occupied[0] is True:
                # opponent piece found so square is available
                if len(square_occupied) == 2: 
                    available_positions.append((to_check_column, to_check_row))       
                # own piece found so square is not available, not adding to available positions
                else: 
                    pass
            else:
                raise Exception("Should never happen, occupied square should always either be true or false")
    return available_positions    


def check_if_square_occupied(
        to_check_column: int,
        to_check_row: int,
        piece_color: str,
        occupied_squares: list[dict[str, str, str]]
        ):
    square_occupied: bool
    position_to_add: str
    square_occupied = False
    position_to_add = False
    result_of_function = []
    for occ_square_dict in occupied_squares:
        occ_square_position = occ_square_dict["position"] 
        occ_square_color = occ_square_dict["color"]
        occ_square_col = int(occ_square_position[ca.COLUMN_IDX])
        occ_square_row = int(occ_square_position[ca.ROW_IDX])

        if occ_square_col == to_check_column and occ_square_row == to_check_row:
            if occ_square_color == piece_color:
                square_occupied = True
                break

            elif occ_square_color != piece_color:
                # different piece color, so this is an accepted spot. extending tuple
                square_occupied = True
                position_to_add = (to_check_column, to_check_row)
                break
            
            else:
                raise Exception("This should never happen. occupied square doesn't have a color")
        else:
            continue
    # probably not the best way to achieve returning col and row when locating opponent only. 
    if position_to_add is not False:
        result_of_function.append(square_occupied)
        result_of_function.append(position_to_add)
    else:
        result_of_function.append(square_occupied)

    return result_of_function