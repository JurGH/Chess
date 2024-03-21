import Functionality.constants as c

# color should be used when creating pieces, so only one function has to be written. 
class Player():
    def __init__(self, name, color, score=0):
        self.name: str
        self.color: str
        self.score: int
        self.check_state: bool
        self.on_turn: bool
        self.active_pieces: list[object]
        self.selected_piece: object
        self.name = name
        self.color = color
        self.score = score
        self.check_state = False
        self.on_turn = False
        self.active_pieces = []
        self.selected_piece = None

        if color == c.PLAYER_COLORS[c.WHITE]:
            self.on_turn = True
            self.long_king_castle_square = c.WHITE_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.WHITE_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_WHITE_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.WHITE_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.WHITE_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_WHITE_SHORT_CASTLE_SQUARES
        else:
            self.on_turn = False
            self.long_king_castle_square = c.BLACK_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.BLACK_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_BLACK_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.BLACK_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.BLACK_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_BLACK_SHORT_CASTLE_SQUARES
        return

    def set_active_pieces(self, pieces: list[object]) -> None:
        self.active_pieces = []
        self.active_pieces = pieces
        return

    def select_piece(self, piece: object) -> None:
        self.selected_piece = piece
        self.selected_piece.toggle_selected()
        return

    def deselect_piece(self) -> None:
        self.selected_piece.toggle_selected()
        self.selected_piece = None
        return
    
    def change_turn(self) -> None:
        if self.on_turn is True:
            self.on_turn = False
        elif self.on_turn is False:
            self.on_turn = True
        else:
            raise Exception("Changing turn not successful, expected True or False")
        return
    
    def set_check(self) -> None:
        self.check_state = True
        return
    
    def reset_check(self) -> None:
        self.check_state = False
        return
    
    def add_score(self) -> None:
        self.score += 1
        return
    
    def change_color(self) -> None:
        if self.color == c.PLAYER_COLORS[c.WHITE]:
            self.color = c.PLAYER_COLORS[c.BLACK]
        else:
            self.color = c.PLAYER_COLORS[c.WHITE]

    def reset_player(self) -> None:
        self.change_color()
        if self.color == c.PLAYER_COLORS[c.WHITE]:
            self.on_turn = True
            self.long_king_castle_square = c.WHITE_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.WHITE_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_WHITE_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.WHITE_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.WHITE_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_WHITE_SHORT_CASTLE_SQUARES
        else:
            self.on_turn = False
            self.long_king_castle_square = c.BLACK_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.BLACK_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_BLACK_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.BLACK_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.BLACK_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_BLACK_SHORT_CASTLE_SQUARES
        return
       