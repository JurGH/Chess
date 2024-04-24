import Functionality.constants as c

PAWN_HEIGHT_SCALE = 0.0625
PAWN_WIDTH_SCALE = 0.075
ROOK_HEIGHT_SCALE = 0.08333333
ROOK_WIDTH_SCALE = 0.0916666
KNIGHT_HEIGHT_SCALE = 0.0916666
KNIGHT_WIDTH_SCALE = 0.0916666
BIG_PIECE_HEIGHT_SCALE = 0.1083333
BIG_PIECE_WIDTH_SCALE = 0.1
DOT_SCALE = 0.025
STRIKE_DOT_SCALE = 0.12
CASTLE_DOT_SCALE = 0.05
FONT_SCALE = 0.08

PAWN_IMAGE_SIZE = (c.SCREEN_HEIGHT * PAWN_HEIGHT_SCALE, c.SCREEN_WIDTH * PAWN_WIDTH_SCALE)
ROOK_IMAGE_SIZE = (c.SCREEN_HEIGHT * ROOK_HEIGHT_SCALE, c.SCREEN_WIDTH * ROOK_WIDTH_SCALE)
KNIGHT_IMAGE_SIZE = (c.SCREEN_HEIGHT * KNIGHT_HEIGHT_SCALE, c.SCREEN_WIDTH * KNIGHT_WIDTH_SCALE)
BIG_PIECE_IMAGE_SIZE = (c.SCREEN_HEIGHT * BIG_PIECE_HEIGHT_SCALE, c.SCREEN_WIDTH * BIG_PIECE_WIDTH_SCALE)
DOT_IMAGE_SIZE = (c.SCREEN_HEIGHT * DOT_SCALE, c.SCREEN_WIDTH * DOT_SCALE)
STRIKED_DOT_IMAGE_SIZE = (c.SCREEN_HEIGHT * STRIKE_DOT_SCALE, c.SCREEN_WIDTH * STRIKE_DOT_SCALE)
CASTLE_DOT_IMAGE_SIZE = (c.SCREEN_HEIGHT * CASTLE_DOT_SCALE, c.SCREEN_WIDTH * CASTLE_DOT_SCALE)
END_SCREEN_IMAGE_SIZE = ((c.SCREEN_HEIGHT / 2), (c.SCREEN_WIDTH / 2))
SKULL_IMAGE_SIZE = (c.SCREEN_HEIGHT / c.NUM_OF_COLS, c.SCREEN_WIDTH / c.NUM_OF_ROWS)

END_SCREEN_TEXT_TOP = 200, 50, 400, 50 
END_SCREEN_TEXT_BOTTOM = 200, 650, 400, 50

INPUT_BOX = round((c.SCREEN_WIDTH / 2) - ((c.SCREEN_WIDTH * 0.8) / 2))\
            ,round((c.SCREEN_HEIGHT / 2) -((c.SCREEN_HEIGHT * 0.2) / 2))\
            ,c.SCREEN_WIDTH * 0.8\
            ,c.SCREEN_HEIGHT * 0.2
PLAYER_NAME_BOX = round((c.SCREEN_WIDTH / 2) - ((c.SCREEN_WIDTH * 0.8) / 2))\
            ,round(c.SCREEN_HEIGHT - (c.SCREEN_HEIGHT * 0.2)) \
            ,c.SCREEN_WIDTH * 0.4\
            ,c.SCREEN_HEIGHT * 0.1


PIECE_IMAGES = [
    {
      "name": "black_pawn"
     ,"normal_path" :"black_pawn.png"
     ,"selected_path" :"selected_black_pawn.png" 
     ,"size" : PAWN_IMAGE_SIZE
    },
    {
      "name": "black_rook"
     ,"normal_path" :"black_rook.png" 
     ,"selected_path" :"selected_black_rook.png" 
     ,"size" : ROOK_IMAGE_SIZE
    },
    {
      "name": "black_knight"
     ,"normal_path" :"black_knight.png" 
     ,"selected_path" :"selected_black_knight.png" 
     ,"size" : KNIGHT_IMAGE_SIZE
    },
    {
     "name": "black_bishop"
     ,"normal_path" :"black_bishop.png" 
     ,"selected_path" :"selected_black_bishop.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "black_king"
     ,"normal_path" :"black_king.png" 
     ,"selected_path" :"selected_black_king.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "black_queen"
     ,"normal_path" :"black_queen.png" 
     ,"selected_path" :"selected_black_queen.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    },
    {
      "name": "white_pawn"
     ,"normal_path" :"white_pawn.png" 
     ,"selected_path" :"selected_white_pawn.png" 
     ,"size" : PAWN_IMAGE_SIZE
    },
    {
      "name": "white_rook"
     ,"normal_path" :"white_rook.png" 
     ,"selected_path" :"selected_white_rook.png" 
     ,"size" : ROOK_IMAGE_SIZE
    },
    {
      "name": "white_knight"
     ,"normal_path" :"white_knight.png" 
     ,"selected_path" :"selected_white_knight.png" 
     ,"size" : KNIGHT_IMAGE_SIZE
    },
    {
     "name": "white_bishop"
     ,"normal_path" :"white_bishop.png" 
     ,"selected_path" :"selected_white_bishop.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "white_king"
     ,"normal_path" :"white_king.png" 
     ,"selected_path" :"selected_white_king.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    },
    {
     "name": "white_queen"
     ,"normal_path" :"white_queen.png" 
     ,"selected_path" :"selected_white_queen.png" 
     ,"size" : BIG_PIECE_IMAGE_SIZE
    }
]

ASSET_IMGS = [
    {
     "color": "WHITE"
    ,"name": "skull"
    ,"path": "yellow_skull.png"
    ,"size": END_SCREEN_IMAGE_SIZE
    },
    {
     "color": "BLACK"
    ,"name": "skull"
    ,"path": "red_skull.png"
    ,"size": END_SCREEN_IMAGE_SIZE
    },
    {
     "color": "WHITE"
    ,"name": "dot"
    ,"path": "yellow_dot.png"
    ,"size": DOT_IMAGE_SIZE
    },
    {
     "color": "BLACK"
    ,"name": "dot"
    ,"path": "red_dot.png"
    ,"size": DOT_IMAGE_SIZE
    },
    {
     "color": "WHITE"
    ,"name": "strike_dot"
    ,"path": "yellow_strike_dot.png"
    ,"size": STRIKED_DOT_IMAGE_SIZE
    },
    {
     "color": "BLACK"
    ,"name": "strike_dot"
    ,"path": "red_strike_dot.png"
    ,"size": STRIKED_DOT_IMAGE_SIZE
    },
    {
     "color": "WHITE"
    ,"name": "bell"
    ,"path": "yellow_bell.png"
    ,"size": CASTLE_DOT_IMAGE_SIZE
    },
    {
     "color": "BLACK"
    ,"name": "bell"
    ,"path": "red_bell.png"
    ,"size": CASTLE_DOT_IMAGE_SIZE
    },
    {
     "color": ""
    ,"name": "stalemate"
    ,"path": "stalemate.png"
    ,"size": END_SCREEN_IMAGE_SIZE
    }
]


