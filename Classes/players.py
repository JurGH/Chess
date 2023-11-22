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
        if color == "WHITE":
            self.on_turn = True
        else:
            self.on_turn = False

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
    
    def toggle_check(self) -> None:
        if self.check_state is False:
            self.check_state = True
        else:
            self.check_state = False
        return
    
    def add_score(self) -> None:
        self.score += 1
        return
