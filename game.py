import Functionality.constants as c
import Classes.board as b
import Classes.pieces as pi
import Classes.players as p
import Classes.castle as ca
import Functionality.check_evaluation as ce
from typing import Optional

class Game():
    def __init__(self, board: b.Board, players: list[p.Player], all_pieces: list[pi.Piece], castling: ca.Castling):
        self.board = board
        self.players = players
        self.all_pieces = all_pieces
        self.castling = castling

    def set_up_board (self) -> None:
        self.active_player = None
        self.selected_piece = None
        self.check = False  # needs to be set to False after testing
        self.stalemate = False
        self.checkmate = False
        self.state_turn = c.PIECE_NOT_SELECTED
        self.winning_player = None
    
    def set_up_game(self) -> None:
        self.set_up_board()
        self.set_active_player()
        self.assign_pieces_to_players()
        self.board.position_pieces(self.all_pieces)
        self.store_available_positions_player_pieces()
        self.edit_available_positions_player_pieces()
        self.define_selectable_player_pieces()
        return
    
    def assign_pieces_to_players(self) -> None:
        white_pieces = []
        black_pieces = []
        for piece in self.all_pieces:
            if piece.color == "WHITE":
                white_pieces.append(piece)
            else:
                black_pieces.append(piece)
        for player in self.players:
            if player.color == "WHITE":
                player.set_active_pieces(white_pieces)
            else:
                player.set_active_pieces(black_pieces)
        return
                  
    def store_available_positions_player_pieces(self) -> None:
        for piece in self.active_player.active_pieces:
            piece.get_available_positions(self.board.occupied_squares)
        return
    """
    comments needed
    """
    def edit_available_positions_player_pieces(self) -> None:
        for piece in self.active_player.active_pieces:
            to_remove_positions = []
            for available_position in piece.available_positions:
                piece.set_eval_position(available_position)
                self.board.position_eval_pieces(self.all_pieces)
                square_available = piece.evaluate_available_position(self.board.eval_occupied_squares)
                piece.reset_eval_position()
                if square_available is True:
                    continue
                else:
                    to_remove_positions.append(available_position)

            piece.remove_available_positions(to_remove_positions)
        return

    def define_selectable_player_pieces(self) -> None:
        for piece in self.active_player.active_pieces:
            piece.toggle_selectable()
        return
    
    def get_clicked_square(self, click_x: float, click_y: float) -> Optional[str]:
        for name, coordinates in self.board.active_square_coordinates.items():
            if click_x > coordinates[0] and click_x < coordinates[0] + c.SQUARE_WIDTH:
                if click_y > coordinates[1] and click_y < coordinates[1] + c.SQUARE_HEIGHT:
                    return name
        return
    
    def get_clicked_button(self, click_x: float, click_y: float
                           ,play_again_button_range_x: tuple
                           ,play_again_button_range_y: tuple
                           ,quit_button_range_x: tuple
                           ,quit_button_range_y: tuple) -> Optional[int]:
        decision = c.NO_DECISION

        print(f"click_x = {click_x}, click_y = {click_y}, play_again_button_range_x = {play_again_button_range_x}, play_again_button_range_y = {play_again_button_range_y}, quit_button_range_x = {quit_button_range_x}, quit_button_range_y = {quit_button_range_y} ")

        if click_x >= play_again_button_range_x[0] and click_x <= play_again_button_range_x[1]:
            if click_y >= play_again_button_range_y[0] and click_y <= play_again_button_range_y[1]:
                decision = c.PLAY_AGAIN
                return decision
    
        if click_x >= quit_button_range_x[0] and click_x <= quit_button_range_x[1]:
            if click_y >= quit_button_range_y[0] and click_y <= quit_button_range_y[1]:
                decision = c.QUIT
                return decision
            
        return decision
    
    def handle_player_action(self, clicked_square: str) -> bool:
        if self.state_turn != c.PIECE_SELECTED:
            self.handle_player_first_action(clicked_square)

        elif self.state_turn == c.PIECE_SELECTED:
            self.handle_player_second_action(clicked_square)
        
        else:
            print(f"{self.state_turn} self.state_turn not valid")
            return


    def handle_player_first_action(self, clicked_square: str) -> bool:
        # click invalid, not within coordinates of any square.
        for piece in self.active_player.active_pieces:
            if piece.position == clicked_square and piece.selectable is True:
                # evaluate if castling is possible when king is selected. 
                if piece.type == "king" and self.active_player.check_state is False:
                    self.castling.castling_eval(self.active_player, self.board)
                self.active_player.select_piece(piece)
                # selected a piece so returning True to play sound
                self.state_turn = c.PIECE_SELECTED
                self.selected_piece = piece
                return
            else:
                continue

        # didn't click on a square where own piece is currently, so resetting click counter.
        # if piece.selected is False:
        #no piece selected so returning False to play sound
        self.state_turn = c.PIECE_NOT_SELECTED
        return
    
    def get_king_castle_move_type(self, clicked_square: str) -> Optional[int]:
        if clicked_square == self.active_player.long_king_castle_square and self.castling.long_castle_possible:
            return c.LONG
        elif clicked_square == self.active_player.short_king_castle_square and self.castling.short_castle_possible:
            return c.SHORT
        else: 
            return

    def handle_player_second_action(self, clicked_square: str) -> bool:
        if self.active_player.selected_piece.type == "king":
            castle_move = self.get_king_castle_move_type(clicked_square)
            if castle_move is not None:
                self.castle(castle_move)
                self.state_turn = c.CASTLED
                return
        # conversion to tuple so it can be evaluated against available positions within piece
        # which are stored as tuples. 
        try:
            clicked_sq_tup = (int(clicked_square[0]), int(clicked_square[1]))
        except TypeError as e: # Nonetype can happen when the edge of a square is clicked. 
            print(f"{e}")
            self.state_turn = c.INVALID_MOVE
            return
        
        if clicked_square == self.active_player.selected_piece.position:
            self.state_turn = c.PIECE_NOT_MOVED
            return
        
        if clicked_sq_tup in self.active_player.selected_piece.available_positions:
            # checking for strike after each succesful move. No piece on square does nothing. 
            piece_striked = self.strike_piece(clicked_square)
            self.active_player.selected_piece.move_piece(clicked_square)
            if piece_striked:
                self.state_turn = c.STRIKED
                return
            else:
                # reposition pieces on occupied squares after moving piece
                self.state_turn = c.PIECE_MOVED
                return
        self.state_turn = c.INVALID_MOVE
        return

    def pawn_promotion(self) -> None:
        for index, piece in enumerate(self.all_pieces):
            if piece.type == "pawn":
                if piece.promotion_type is not None:
                    piece_position = piece.position
                    piece_color = piece.color
                    piece_type = piece.promotion_type
                    del self.all_pieces[index]
                    self.all_pieces.append(pi.PIECE_CREATION_DICT[piece_type](piece_position, piece_color))
                    return
        return

    def strike_piece(self, position) -> bool:
        for idx, piece in enumerate(self.all_pieces):
            if position == piece.position:
                del self.all_pieces[idx]
                return True
            else:
                continue
        return False

    def castle(self, castle_type: str) -> bool:
        if castle_type == c.LONG:
            for piece in self.active_player.active_pieces:
                if piece.type == "king":
                    piece.move_piece(piece.long_castle_dest_square)
                    self.castled = True
                if piece.type =="rook" and piece.castle_type == "long":
                    piece.move_piece(piece.castle_dest_square)
        elif castle_type == c.SHORT:
            for piece in self.active_player.active_pieces:
                if piece.type == "king":
                    piece.move_piece(piece.short_castle_dest_square)
                    self.castled = True
                if piece.type =="rook" and piece.castle_type == "short":
                    piece.move_piece(piece.castle_dest_square)
        else:
            pass
        return 

    def set_active_player(self) -> None:
        for player in self.players:
            if player.on_turn is True:
                self.active_player = player
            else:
                continue
        return
    
    def eval_check(self) -> None:
        eval_check = ce.evaluate_position(self.active_player.color, self.board.occupied_squares)
        if eval_check is True:
            self.check = False
        else:
            self.check = True
        return

    def eval_checkmate_or_stalemate(self) -> None:
        self.checkmate = False
        self.stalemate = False
        for piece in self.active_player.active_pieces:
            if len(piece.available_positions) > 0:
                self.checkmate = False
                self.stalemate = False
                return
        if self.check is True:
            self.checkmate = True
            for player in self.players:
                if player.on_turn is False:
                    self.winning_player = player
        else:
            self.stalemate = True
        return

    def reset_turn(self) -> None:
        if self.state_turn == c.PIECE_SELECTED or self.state_turn == c.PIECE_NOT_SELECTED:
            return
        if self.active_player.selected_piece is not None:
            self.active_player.deselect_piece()
            self.selected_piece = None
        if self.state_turn == c.INVALID_MOVE or self.state_turn == c.PIECE_NOT_MOVED:
            self.state_turn = c.PIECE_NOT_SELECTED
            return    
        self.pawn_promotion()
        # always reposition the pieces after a turn, because piece promotion might have happened
        self.board.position_pieces(self.all_pieces)
        for player in self.players:
            player.change_turn()
        self.set_active_player()
        self.active_player.reset_check()
        # make sure new piece after pawn promotion is assigned to the correct player
        self.assign_pieces_to_players()
        self.store_available_positions_player_pieces()
        self.edit_available_positions_player_pieces()
        # no available positions in piece = not selectable
        self.define_selectable_player_pieces() # no available positions in piece = not selectable
        self.eval_check()
        self.eval_checkmate_or_stalemate()
        self.state_turn = c.PIECE_NOT_SELECTED
        if self.check:
            self.active_player.set_check()
        return
    
    def reset_game(self) -> None:
        if self.checkmate:
            self.winning_player.add_score()
        for player in self.players:
            player.change_color()
            if player.color == c.PLAYER_COLORS[c.WHITE]:
                player.on_turn = True

        for piece in self.all_pieces:
            del piece
        self.set_up_game()

        