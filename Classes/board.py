import Functionality.constants as c
import Functionality.movement_functions as mf

"""
This script defines the Player and Board class.
In the Board class there's functions Create Pieces and to Draw the Board and Pieces
There's also a function to define available positions which should be improved and maybe moved
"""

class Board():
    def __init__(self) -> None:
        #self.occupied_squares: list[dict[str, str, str]] # position, color, type
        #Looping through rows and columns fills a dictionary with square name and coordinates: "A1" : (x,y)
        # The x,y coordinates are based on the square width and height, offset by -5 & 8 to make sure pieces are drawn in centre.
        self.occupied_squares: list[dict[str: str, str: str, str: str]]# {"position", "color" "type"}
        self.eval_occupied_squares: list[dict[str: str, str: str, str: str]]# {"position", "color" "type"}
        self.square_coordinates: dict[str: tuple] # "A1" : (x,y,w,h)
        self.occupied_squares = []
        self.eval_occupied_squares = []
        self.active_color_view = c.WHITE
        # should be evaluated if white or black player view should be applied. For now hard coded to white
        self.active_square_coordinates = self.get_square_coordinates_white_bottom()
        self.square_coordinates_white_bottom = self.get_square_coordinates_white_bottom()
        self.square_coordinates_black_bottom = self.get_square_coordinates_black_bottom()
        self.check_straight_directions = mf.get_valid_straight_directions()
        self.check_diagonal_directions = mf.get_valid_diagonal_directions()
        self.check_knight_directions = mf.get_valid_knight_directions()
        self.check_king_directions = mf.get_valid_king_directions()


    def position_pieces(self, pieces: list[object]) -> None :  #insert if occupied_square or eval_occupied_squares is filled, eval based on to_check_pos
        self.occupied_squares = []
        for piece in pieces:
            self.occupied_squares.append({"position": piece.position, "color": piece.color, "type": piece.type})
        return
    
    def position_eval_pieces(self, pieces: list[object]) -> None: #check if 2 functions or 1, see above
        self.eval_occupied_squares = []
        for piece in pieces:
            if piece.eval_position is not None:
                self.eval_occupied_squares.append({"position": piece.eval_position, "color": piece.color, "type": piece.type})
            else:
                self.eval_occupied_squares.append({"position": piece.position, "color": piece.color, "type": piece.type})
        return

    def get_square_coordinates_white_bottom(self) -> None:
        square_coordinates_white_bottom = {}
        for row in c.BOARD_ROWS:
            y = ((max(c.BOARD_ROWS) - 1) * c.SQUARE_HEIGHT) - ((row - 1) * c.SQUARE_HEIGHT)
            i = 0
            for index, col in enumerate(c.BOARD_COLUMNS.keys()):
                x = ((index) * c.SQUARE_WIDTH)
                i += 1
                square_coordinates_white_bottom.update({str(col) + str(row) : (x, y, c.SQUARE_WIDTH, c.SQUARE_HEIGHT)})
        return square_coordinates_white_bottom
    
    def get_square_coordinates_black_bottom(self) -> None:
        square_coordinates_black_bottom = {}
        for row in c.BOARD_ROWS:
            y = ((row - 1) * c.SQUARE_HEIGHT)
            i = 0
            for index, col in enumerate(c.BOARD_COLUMNS.keys()):
                x = ((max(c.BOARD_COLUMNS) -1) * c.SQUARE_WIDTH) - ((index) * c.SQUARE_WIDTH)
                i += 1
                square_coordinates_black_bottom.update({str(col) + str(row) : (x, y, c.SQUARE_WIDTH, c.SQUARE_HEIGHT)})
        return square_coordinates_black_bottom
  
    def toggle_square_coordinates(self) -> None:
        self.active_square_coordinates = {}
        if self.active_color_view == c.WHITE:
            self.active_color_view = c.BLACK
            self.active_square_coordinates = self.square_coordinates_black_bottom
        else:
            self.active_color_view = c.WHITE
            self.active_square_coordinates = self.square_coordinates_white_bottom
        return





        


                
        
        


        