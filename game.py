import Functionality.constants as c
import Assets as a
import Classes.board as b
import Classes.pieces as pi
import Classes.players as p
import Functionality.check_evaluation as ce

class Game():
    def __init__(self, board: b.Board, players: list[p.Player], all_pieces: list[pi.Piece]):
        self.board = board
        self.players = players
        self.all_pieces = all_pieces
        self.num_of_click_in_turn = 0
        self.active_player = None
        self.piece_striked = False
        self.check = False
        self.short_king_castle_square = None
        self.long_king_castle_square = None
        self.short_rook_castle_square = None
        self.long_rook_castle_square = None
        self.to_check_long_castle_squares = None
        self.to_check_short_castle_squares = None
        self.long_castle_possible = None
        self.short_castle_possible = None
        self.winning_player = None
        self.losing_player = None
        self.check = False
        self.stalemate = False
        self.checkmate = False
    
    def set_up_game(self) -> None:
        self.set_active_player()
        self.assign_pieces_to_players()
        self.set_long_and_short_castle_squares()
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
    
    def set_long_and_short_castle_squares(self) -> None:
        if self.active_player.color == c.PLAYER_COLORS[c.WHITE]:
            self.long_king_castle_square = c.WHITE_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.WHITE_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_WHITE_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.WHITE_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.WHITE_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_WHITE_SHORT_CASTLE_SQUARES
        else:
            self.long_king_castle_square = c.BLACK_LONG_CASTLE_KING_SQUARE
            self.long_rook_castle_square = c.BLACK_LONG_CASTLE_ROOK_SQUARE
            self.to_check_long_castle_squares = c.TO_CHECK_BLACK_LONG_CASTLE_SQUARES
            self.short_king_castle_square = c.BLACK_SHORT_CASTLE_KING_SQUARE
            self.short_rook_castle_square = c.BLACK_SHORT_CASTLE_ROOK_SQUARE
            self.to_check_short_castle_squares = c.TO_CHECK_BLACK_SHORT_CASTLE_SQUARES
        return
                
    def store_available_positions_player_pieces(self) -> None:
        for piece in self.active_player.active_pieces:
            piece.get_available_positions(self.board.occupied_squares)
        return

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
    
    def handle_player_first_action(self, click_x: float, click_y: float) -> None:
        clicked_square = None
        for name, coordinates in self.board.active_square_coordinates.items():
            if click_x > coordinates[0] and click_x < coordinates[0] + c.SQUARE_WIDTH:
                if click_y > coordinates[1] and click_y < coordinates[1] + c.SQUARE_HEIGHT:
                    clicked_square = name
        # click invalid, not within coordinates of any square.
        if clicked_square is None:
            return
        for piece in self.active_player.active_pieces:
            if piece.position == clicked_square and piece.selectable is True:
                self.active_player.select_piece(piece)
                self.num_of_click_in_turn = 1
                # selected a piece so returning True to play sound
                return True
            else:
                continue

        # didn't click on a square where own piece is currently, so resetting click counter.
        # if piece.selected is False:
        #no piece selected so returning False to play sound
        return False

    def handle_player_second_action(self, click_x: float, click_y: float) -> bool:
        clicked_square = None
        for name, coordinates in self.board.active_square_coordinates.items():
            if click_x > coordinates[0] and click_x < coordinates[0] + c.SQUARE_WIDTH:
                if click_y > coordinates[1] and click_y < coordinates[1] + c.SQUARE_HEIGHT:
                    clicked_square = name

        # conversion to tuple so it can be evaluated against available positions within piece
        # which are stored as tuples. 
        try:
            clicked_sq_tup = (int(clicked_square[0]), int(clicked_square[1]))
        except TypeError as e: # Nonetype can happen when the edge of a square is clicked. 
            self.active_player.deselect_piece()
            print(f"{e}")
            return

        if clicked_sq_tup in self.active_player.selected_piece.available_positions:
            try:
                self.active_player.selected_piece.turn_counter += 1
            except AttributeError as e:
                print(f"{e}, so not incrementing turn_counter for this piece")
            # checking for strike after each succesful move. No piece on square does nothing. 
            self.strike_piece(clicked_square)
            self.active_player.selected_piece.move_piece(clicked_square)
            # reposition pieces on occupied squares after moving piece
            self.active_player.deselect_piece()
            return True
        
        castled = self.castle(clicked_square)
        self.active_player.deselect_piece()
        return castled

    def pawn_promotion(self) -> None:
        for index, piece in enumerate(self.all_pieces):
            if piece.type == "pawn":
                if piece.promotion_type is not None:
                    piece_position = piece.position
                    piece_color = piece.color
                    piece_type = piece.promotion_type
                    print(f"removing {self.all_pieces[index]} from game because of promotion")
                    del self.all_pieces[index]
                    self.all_pieces.append(pi.PIECE_CREATION_DICT[piece_type](piece_position, piece_color))
                    return
        return

    def strike_piece(self, position) -> None:
        for idx, piece in enumerate(self.all_pieces):
            if position == piece.position:
                self.piece_striked = True
                print(f"removing {self.all_pieces[idx]} from game")
                del self.all_pieces[idx]
                break
            else:
                continue
        return

    def castling_eval(self) -> None:
        short_castle_possible = False
        long_castle_possible = False
        for piece in self.active_player.active_pieces:
            if piece.type == "king":
                if piece.turn_counter > 0:
                    return
            if piece.type == "rook":
                if piece.position == self.short_rook_castle_square:
                    if piece.turn_counter == 0:
                        short_castle_possible = True
            if piece.type == "rook":
                if piece.position == self.long_rook_castle_square:
                    if piece.turn_counter == 0:
                        long_castle_possible = True
        if long_castle_possible:
            self.long_castle_eval(self.board.occupied_squares)
        else:
            self.long_castle_possible = False
        if short_castle_possible: 
            self.short_castle_eval(self.board.occupied_squares)
        else:
            self.short_castle_possible = False
        return
    
    def long_castle_eval(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        for square in self.to_check_long_castle_squares:
            long_castle_possible = ce.castle_evaluation(square, occupied_squares, self.active_player.color)
            if long_castle_possible is False:
                break
            else:
                continue
        self.long_castle_possible = long_castle_possible
        return

    def short_castle_eval(self, occupied_squares: dict[str:str, str:str, str:str]) -> None:
        for square in self.to_check_short_castle_squares:
            short_castle_possible = ce.castle_evaluation(square, occupied_squares, self.active_player.color)
            if short_castle_possible is False:
                break
            else:
                continue
        self.short_castle_possible = short_castle_possible
        return
    
    def castle(self, clicked_square) -> bool:
        """
        check of de click_square de long of short castle square is
        als Long, check of long_castle_possible True is idem short
        als true dan koning verzetten en rook verzetten
        move piece king(long_castle_square) en move piece rook(castle_square)
        """
        castled = False

        if clicked_square == self.long_king_castle_square and self.long_castle_possible:
            for piece in self.active_player.active_pieces:
                if piece.type == "king":
                    piece.move_piece(piece.long_castle_square)
                    castled = True
                if piece.type =="rook" and (piece.position == "11" or piece.position == "18"):
                    piece.move_piece(piece.castle_square)

        if clicked_square == self.short_king_castle_square and self.short_castle_possible:
            for piece in self.active_player.active_pieces:
                if piece.type == "king":
                    piece.move_piece(piece.short_castle_square)
                    castled = True
                if piece.type =="rook" and (piece.position == "81" or piece.position == "88"):
                    piece.move_piece(piece.castle_square)
        
        return castled

    def set_active_player(self) -> None:
        for player in self.players:
            if player.on_turn is True:
                self.active_player = player
            else:
                continue
        return
    
    def eval_check_or_stalemate(self) -> None:
        self.checkmate = None
        for piece in self.active_player.active_pieces:
            if len(piece.available_positions) > 0:
                self.checkmate = False
                return
        if self.check is True:
            self.checkmate = True
            for player in self.players:
                if player.on_turn is True:
                    self.losing_player = player
                else:
                    self.winning_player = player
        else:
            self.stalemate = True
        return

    def reset_turn(self, moved: bool) -> None:
        self.num_of_click_in_turn = 0
        self.selected_piece = None
        self.piece_striked = False
        if moved is True:
            self.pawn_promotion()
            # always reposition the pieces after a turn, because piece promotion might have happened
            self.board.position_pieces(self.all_pieces)
            for player in self.players:
                player.change_turn()
            self.set_active_player()
            # make sure new piece after pawn promotion is assigned to the correct player
            self.assign_pieces_to_players()
            self.set_long_and_short_castle_squares()
            self.castling_eval()
            self.store_available_positions_player_pieces()
            self.edit_available_positions_player_pieces()
            # no available positions in piece = not selectable
            self.define_selectable_player_pieces() # no available positions in piece = not selectable
            self.eval_check_or_stalemate()
            return
        else:
            return








