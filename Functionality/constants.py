SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800
BACKGROUND_COLOR = (168, 168, 168)
COLORS = {
     'WHITE': (0, 0, 0)
    ,'BLACK': (0, 0, 0)
    ,'GREY' : (128, 128, 128)
    }
PAWN_HEIGHT_SCALE = 0.0625
PAWN_WIDTH_SCALE = 0.075
ROOK_HEIGHT_SCALE = 0.08333333
ROOK_WIDTH_SCALE = 0.0916666
KNIGHT_HEIGHT_SCALE = 0.0916666
KNIGHT_WIDTH_SCALE = 0.0916666
BIG_PIECE_HEIGHT_SCALE = 0.1083333
BIG_PIECE_WIDTH_SCALE = 0.1

PAWN_IMAGE_SIZE = (SCREEN_HEIGHT * PAWN_HEIGHT_SCALE, SCREEN_WIDTH * PAWN_WIDTH_SCALE)
ROOK_IMAGE_SIZE = (SCREEN_HEIGHT * ROOK_HEIGHT_SCALE, SCREEN_WIDTH * ROOK_WIDTH_SCALE)
KNIGHT_IMAGE_SIZE = (SCREEN_HEIGHT * KNIGHT_HEIGHT_SCALE, SCREEN_WIDTH * KNIGHT_WIDTH_SCALE)
BIG_PIECE_IMAGE_SIZE = (SCREEN_HEIGHT * BIG_PIECE_HEIGHT_SCALE, SCREEN_WIDTH * BIG_PIECE_WIDTH_SCALE)

PLAYER_NAMES = ["Player1", "Player2"]
PLAYER_COLORS = ["WHITE", "BLACK"]
WHITE = 0
BLACK = 1

NUM_OF_ROWS = 8
NUM_OF_COLS = 8

SQUARE_HEIGHT = SCREEN_HEIGHT / NUM_OF_ROWS
SQUARE_WIDTH = SCREEN_WIDTH / NUM_OF_COLS

SQUARE_COLOR = (219, 219, 219)

POSITION_IDX = 0
COLOR_IDX = 1
COLUMN_IDX = 0
ROW_IDX = 1
LEFT = 1


BOARD_COLUMNS = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
BOARD_ROWS = [8, 7, 6, 5, 4, 3, 2, 1]

WHITE_LONG_CASTLE_KING_SQUARE = "31"
WHITE_SHORT_CASTLE_KING_SQUARE = "71"
BLACK_LONG_CASTLE_KING_SQUARE = "38"
BLACK_SHORT_CASTLE_KING_SQUARE = "78"

WHITE_LONG_CASTLE_ROOK_SQUARE = "11"
WHITE_SHORT_CASTLE_ROOK_SQUARE = "81"
BLACK_LONG_CASTLE_ROOK_SQUARE = "18"
BLACK_SHORT_CASTLE_ROOK_SQUARE = "88"

TO_CHECK_WHITE_LONG_CASTLE_SQUARES = ["21", "31", "41"]
TO_CHECK_WHITE_SHORT_CASTLE_SQUARES = ["61", "71"]
TO_CHECK_BLACK_LONG_CASTLE_SQUARES = ["28", "38", "48"]
TO_CHECK_BLACK_SHORT_CASTLE_SQUARES = ["68", "78"]


ALL_PIECES = {
    "rook": {
          "WHITE": ["11", "81"]
         ,"BLACK": ["18", "88"]
        },
    "knight": {
          "WHITE": ["21", "71"]
         ,"BLACK": ["28", "78"]
        },
    "bishop": {
          "WHITE": ["31", "61"]
         ,"BLACK": ["38", "68"]
        },
    "queen": {
          "WHITE": ["41"]
         ,"BLACK": ["48"]
        },
    "king": {
          "WHITE": ["51"]
         ,"BLACK": ["58"]
        },
    "pawn": {
          "WHITE": ["12", "22", "32", "42", "52", "62","72","82"]
         ,"BLACK": ["17", "27", "37", "47", "57", "67","77","87"]
        },
}


TO_CHECK_LONG_CASTLE_POSITIONS = {
    # WHITE KING
     "51": ["41", "31"]
    # BLACK KING
    ,"58" : ["48", "38"]
}

TO_CHECK_SHORT_CASTLE_POSITIONS = {
    # WHITE KING
     "51" : ["61", "71"]
    # BLACK KING
    ,"58" : ["68", "78"]
}

ROOK_CASTLE_SQUARES = {
    # WHITE ROOKS
    "11" : "41"
   ,"81" : "61"
   # BLACK ROOKS
   ,"18" : "48"
   ,"88" : "68"
}

KING_LONG_CASTLE_SQUARES = {
    # WHITE KING
     "51": "31"
    # BLACK KING
    ,"58": "38"
}

KING_SHORT_CASTLE_SQUARES = {
    # WHITE KING
     "51" :"71"
    # BLACK KING
    ,"58" :"78"
}

PIECE_IMAGES = [
    {
      "name": "black_pawn"
     ,"normal_path" :"black_pawn.png"
     ,"selected_path" :"selected_black_pawn.png" 
     ,"scale" : PAWN_IMAGE_SIZE
    },
    {
      "name": "black_rook"
     ,"normal_path" :"black_rook.png" 
     ,"selected_path" :"selected_black_rook.png" 
     ,"scale" : ROOK_IMAGE_SIZE
    },
    {
      "name": "black_knight"
     ,"normal_path" :"black_knight.png" 
     ,"selected_path" :"selected_black_knight.png" 
     ,"scale" : KNIGHT_IMAGE_SIZE
    },
    {
     "name": "black_bishop"
     ,"normal_path" :"black_bishop.png" 
     ,"selected_path" :"selected_black_bishop.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "black_king"
     ,"normal_path" :"black_king.png" 
     ,"selected_path" :"selected_black_king.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "black_queen"
     ,"normal_path" :"black_queen.png" 
     ,"selected_path" :"selected_black_queen.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    },
    {
      "name": "white_pawn"
     ,"normal_path" :"white_pawn.png" 
     ,"selected_path" :"selected_white_pawn.png" 
     ,"scale" : PAWN_IMAGE_SIZE
    },
    {
      "name": "white_rook"
     ,"normal_path" :"white_rook.png" 
     ,"selected_path" :"selected_white_rook.png" 
     ,"scale" : ROOK_IMAGE_SIZE
    },
    {
      "name": "white_knight"
     ,"normal_path" :"white_knight.png" 
     ,"selected_path" :"selected_white_knight.png" 
     ,"scale" : KNIGHT_IMAGE_SIZE
    },
    {
     "name": "white_bishop"
     ,"normal_path" :"white_bishop.png" 
     ,"selected_path" :"selected_white_bishop.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "white_king"
     ,"normal_path" :"white_king.png" 
     ,"selected_path" :"selected_white_king.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "white_queen"
     ,"normal_path" :"white_queen.png" 
     ,"selected_path" :"selected_white_queen.png" 
     ,"scale" : BIG_PIECE_IMAGE_SIZE
    }
]

STRAIGHT = ["queen", "rook"]
DIAGONAL = ["queen", "bishop"]
KNIGHT = ["knight"]
PAWN = ["pawn"]
KING = ["king"]