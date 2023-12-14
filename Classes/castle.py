#import Functionality.constants as c
import Functionality.check_evaluation as ce
import Functionality.constants as c

class Castling():
    def __init__(self):
        self.long_castle_possible = False
        self.short_castle_possible = False
    
    def castling_eval(self, active_player: object, board: object) -> None:
        long_castle_req_met = False
        short_castle_req_met = False
        for piece in active_player.active_pieces:
            if piece.type == "king":
                if piece.turn_counter > 0:
                    return
            if piece.type == "rook":
                if piece.turn_counter == 0:
                    if piece.castle_type == "long":
                        long_castle_req_met = True
                    if piece.castle_type == "short":
                        short_castle_req_met = True
                else:
                    continue      

        if long_castle_req_met:
            self.long_castle_eval(active_player, board.occupied_squares)
        else:
            self.long_castle_possible = False
        if short_castle_req_met: 
            self.short_castle_eval(active_player, board.occupied_squares)
        else:
            self.short_castle_possible = False
        return
    
    def long_castle_eval(self, active_player: object, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        for square in active_player.to_check_long_castle_squares:
            square_possible = ce.evaluate_position(active_player.color, occupied_squares, c.CASTLE_EVAL, square)
            if square_possible is False:
                break
            else:
                continue
        self.long_castle_possible = square_possible
        return

    def short_castle_eval(self, active_player: object, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        for square in active_player.to_check_short_castle_squares:
            square_possible = ce.evaluate_position(active_player.color, occupied_squares, c.CASTLE_EVAL, square)
            if square_possible is False:
                break
            else:
                continue
        self.short_castle_possible = square_possible
        return
    