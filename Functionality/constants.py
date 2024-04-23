SCREEN_HEIGHT = 1200
SCREEN_WIDTH = 1200
NUM_OF_ROWS = 8
NUM_OF_COLS = 8

BACKGROUND_COLOR = (168, 168, 168)
COLORS = {
     'WHITE': (0, 0, 0)
    ,'BLACK': (0, 0, 0)
    ,'GREY' : (128, 128, 128)
    ,'GOLD' : (255, 201, 14)
    }


''' 
DIT MOET NOG GEFIXT. HARD CODED
!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@!@
'''
END_SCREEN_TEXT_TOP = 200, 50, 400, 50 
END_SCREEN_TEXT_BOTTOM = 200, 650, 400, 50

INPUT_BOX = round((SCREEN_WIDTH / 2) - ((SCREEN_WIDTH * 0.8) / 2))\
            ,round((SCREEN_HEIGHT / 2) -((SCREEN_HEIGHT * 0.2) / 2))\
            ,SCREEN_WIDTH * 0.8\
            ,SCREEN_HEIGHT * 0.2
PLAYER_NAME_BOX = round((SCREEN_WIDTH / 2) - ((SCREEN_WIDTH * 0.8) / 2))\
            ,round(SCREEN_HEIGHT - (SCREEN_HEIGHT * 0.2)) \
            ,SCREEN_WIDTH * 0.4\
            ,SCREEN_HEIGHT * 0.1
print(INPUT_BOX)
PLAYER_NAMES = ["Player1", "Player2"]
PLAYER_COLORS = ["WHITE", "BLACK"]
WHITE = 0
BLACK = 1

PIECE_NOT_SELECTED = 0
PIECE_SELECTED = 1
PIECE_MOVED = 2
PIECE_NOT_MOVED = 3
CASTLED = 4
STRIKED = 5
INVALID_MOVE = 6

CHECK_EVAL = 0
CASTLE_EVAL = 1

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
LONG = 1
SHORT = 2
FIRST = 1
SECOND = 2
WIDTH = 0
HEIGHT = 1


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

NO_DECISION = 0
PLAY_AGAIN = 1
QUIT = 2


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

STRAIGHT = ["queen", "rook"]
DIAGONAL = ["queen", "bishop"]
KNIGHT = ["knight"]
PAWN = ["pawn"]
KING = ["king"]

