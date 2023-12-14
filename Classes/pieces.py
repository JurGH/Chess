import Functionality.constants as c
import Functionality.movement_functions as mf
import Functionality.check_evaluation as ce

from abc import ABC, abstractmethod

'''
THIS FILE IS USED TO HANDLE ALL PIECE MOVEMENT. THE SEPERATE CLASSES ACCEPT COLUMN NAMES AND ROW NUMBERS
TO DEFINE WHICH POSITION SHOULD THEORETICALLY ALL BE AVAILABLE. THE CODE IN THIS FILE DOES NOT HANDLE OCCUPATION OF 
SQUARES. THAT IS DONE SEPERATELY IN BOARD.PY.
TO DO: MOVEMENT FUNCTIONS AS PARAMETER OF THE ROOK FUNCTION TO INHERIT METHODS & PROPERTIES
'''
class Piece(ABC):

    def __init__(self, position: str, color: str):
        self.position = position
        self.color = color

    @abstractmethod
    def get_available_positions(self):
        pass

    @abstractmethod
    def evaluate_available_position(self):
        pass

    @abstractmethod
    def remove_available_positions(self):
        pass

    @abstractmethod
    def set_eval_position(self):
        pass

    @abstractmethod
    def reset_eval_position(self):
        pass

    @abstractmethod
    def toggle_selectable(self):
        pass

    @abstractmethod
    def toggle_selected(self):
        pass

    @abstractmethod
    def move_piece(self):
        pass

class Rook(Piece):
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.type = "rook"
        try:
            if int(self.position[c.COLUMN_IDX]) == 1:
                self.castle_type = "long"
            else:
                self.castle_type = "short"
        except ValueError as e:
            print("unable to convert position[column] to int. messed up instantiation of rook class")
        self.turn_counter = 0
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = mf.get_valid_straight_directions()
        self.castle_dest_square = c.ROOK_CASTLE_SQUARES[self.position]

    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        self.available_positions = []
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        self.available_positions = mf.get_available_positions_in_line_movement(
            current_column, current_row, self.valid_directions, occupied_squares, self.color, self.available_positions
        )
        return
        
    def evaluate_available_position(self, eval_occupied_squares: dict[str:str, str:str, str:str]) -> bool:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return

    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return
    
    def move_piece(self, position: str) -> None:
        self.position = position
        self.turn_counter += 1
        return

    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return

    # to be able to highlight pieces when selected
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True
        return

class Knight(Piece):
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.type = "knight"
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = mf.get_valid_knight_directions()

    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        self.available_positions = []
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        self.available_positions = mf.get_available_single_movement_positions(
            current_column, current_row, self.valid_directions, occupied_squares, self.color
        )
        return
        
    def evaluate_available_position(self, eval_occupied_squares: dict[str:str, str:str, str:str]) -> None:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return

    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return
    
    def move_piece(self, position: str) -> None: 
        self.position = position
        return
    
    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return

    # to be able to highlight pieces when selected
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True

class Bishop(Piece):
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.type = "bishop"
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = mf.get_valid_diagonal_directions()

    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        self.available_positions = []
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        self.available_positions = mf.get_available_positions_in_line_movement(
            current_column, current_row, self.valid_directions, occupied_squares, self.color, self.available_positions
        )
        return
        
    def evaluate_available_position(self, eval_occupied_squares: dict[str:str, str:str, str:str]) -> None:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return

    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return
    
    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return

    # to be able to highlight pieces when selected
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True
        return
    
    def move_piece(self, position: str) -> None:  
        self.position = position
        return


class Queen(Piece):
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.type = "queen"
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = self.get_valid_directions()

    def get_valid_directions(self) -> list[tuple]:
       valid_directions = []
       valid_straight_directions = mf.get_valid_straight_directions()
       valid_diagonal_directions = mf.get_valid_diagonal_directions()
       valid_directions.extend(valid_straight_directions)
       valid_directions.extend(valid_diagonal_directions)
       return valid_directions


    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        self.available_positions = []
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        self.available_positions = mf.get_available_positions_in_line_movement(
            current_column, current_row, self.valid_directions, occupied_squares, self.color, self.available_positions
        )
        return
        
    def evaluate_available_position(self, eval_occupied_squares: dict[str:str, str:str, str:str]) -> None:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return

    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return

    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return
    
    # to be able to highlight pieces when selected
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True
        return
    
    def move_piece(self, position: str) -> None: 
        self.position = position
        return

class King(Piece):
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.check = False
        self.type = "king"
        self.turn_counter = 0
        self.available_castle_positions = []
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = mf.get_valid_king_directions()
        self.long_castle_dest_square = c.KING_LONG_CASTLE_SQUARES[self.position]
        self.short_castle_dest_square = c.KING_SHORT_CASTLE_SQUARES[self.position]
        self.to_check_long_castle_squares = c.TO_CHECK_LONG_CASTLE_POSITIONS[self.position]
        self.to_check_short_castle_squares = c.TO_CHECK_SHORT_CASTLE_POSITIONS[self.position]

    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        self.available_positions = mf.get_available_single_movement_positions(
            current_column, current_row, self.valid_directions, occupied_squares,self.color
        )
        return

    def evaluate_available_position(self, eval_occupied_squares: dict[str:str, str:str, str:str]) -> None:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return
    
    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return        
    
    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return
    
    # will be used to highlight pieces when selected. 
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True
        return

    def move_piece(self, position: str) -> None: # "11" etc. 
        self.position = position
        self.turn_counter += 1
        return

class Pawn(Piece): 
    def __init__(self, position, color):
        self.position = position
        self.eval_position = None #eval_position is None, except if the piece is being evaluated
        self.color = color
        self.promotion_type = None # stores the string value of the piece that will be created after reaching end of board
        self.type = "pawn"
        self.turn_counter = 0
        self.available_positions = []
        self.selectable = False
        self.selected = False
        self.valid_directions = self.get_valid_directions()
        self.first_move_directions = self.valid_directions[0]
        self.regular_directions = self.valid_directions[1]
        self.striking_directions = self.valid_directions[2]
    
    def get_valid_directions(self) -> list[tuple]:
        first_move_directions = mf.get_pawn_first_move_direction(self.color)
        valid_regular_directions = mf.get_valid_pawn_regular_directions(self.color)
        valid_striking_directions = mf.get_valid_pawn_striking_directions(self.color)
        return first_move_directions, valid_regular_directions, valid_striking_directions

    def get_available_positions(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        self.available_positions = []
        current_column = int(self.position[0])
        current_row = int(self.position[1])
        first_move_position = None
        if self.turn_counter == 0:
            first_move_position = mf.get_available_regular_pawn_move_positions(
                            current_column, current_row, self.first_move_directions, occupied_squares, self.color)
            # only happens when pawn hasn't moved yet
        regular_positions = mf.get_available_regular_pawn_move_positions(
            current_column, current_row, self.regular_directions, occupied_squares,self.color
        )
        striking_positions = mf.get_available_pawn_striking_positions(
            current_column, current_row, self.striking_directions, occupied_squares,self.color
        )

        self.available_positions.extend(regular_positions)
        # check if first square in front of pawn is free, if not free no double square move possible
        if len(self.available_positions) > 0 and first_move_position is not None:
            self.available_positions.extend(first_move_position) 
        self.available_positions.extend(striking_positions)
        return
        
    def evaluate_available_position(self, eval_occupied_squares: dict[str, str, str]) -> None:
        square_available = ce.evaluate_position(self.color, eval_occupied_squares)
        if square_available is True:
            return True
        else:
            return False
        
    def remove_available_positions(self, positions_to_remove: list[str]) -> None:
        for position in self.available_positions[::-1]:
            if position in positions_to_remove:
                self.available_positions.remove(position)
        return

    def set_eval_position(self, eval_position) -> None:
        eval_position_column = str(eval_position[c.COLUMN_IDX])
        eval_position_row = str(eval_position[c.ROW_IDX])
        self.eval_position = eval_position_column + eval_position_row
        return
    
    def reset_eval_position(self) -> None:
        self.eval_position = None
        return

    def toggle_selectable(self) -> None:
        #at least 1 position where own king is not on check state available
        if len(self.available_positions) > 0:
            self.selectable = True
        else:
            self.selectable = False
        return
    
    # will be used to highlight pieces when selected. 
    def toggle_selected(self) -> None:
        if self.selected is True:
            self.selected = False
        else:
            self.selected = True
        return
       
    def move_piece(self, position: str) -> None:
        if self.color == "WHITE" and int(position[c.ROW_IDX]) == max(c.BOARD_ROWS):
            self.promote_pawn("queen")
        elif self.color == "BLACK" and int(position[c.ROW_IDX]) == min(c.BOARD_ROWS):
            self.promote_pawn("queen")
        self.position = position
        return
    
    def promote_pawn(self, type) -> None:
        self.promotion_type = type
        return

# used to handle creation of piece based on piece type from constants file
PIECE_CREATION_DICT = {
     "rook" : Rook
    ,"knight": Knight
    ,"bishop": Bishop
    ,"queen": Queen
    ,"king": King
    ,"pawn": Pawn
}