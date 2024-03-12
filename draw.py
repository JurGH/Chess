import pygame
import os
import Functionality.constants as c
import time 

class Draw_board():
    
    def __init__(self):
        self.piece_image_info: list[dict[str:str, str:pygame.Surface, str:tuple]]
        self.piece_image_info: list[dict[str:str, str:pygame.Surface, str:tuple]]
        self.assets: list[dict[str:str, str:pygame.Surface, str:tuple]]
        self.piece_image_info = []
        self.piece_selected_image_info = []
        self.assets = []
        self.current_directory = os.path.dirname(__file__)
        self.assets_directory = os.path.join(self.current_directory, "Assets")
        self.assets_directory_2 = os.path.join(self.assets_directory, "img\\")
        self.font = pygame.font.Font(None,round(c.SCREEN_HEIGHT * c.FONT_SCALE))
        self.top_rect = pygame.Rect(c.END_SCREEN_TEXT_TOP)
        self.bottom_rect = pygame.Rect(c.END_SCREEN_TEXT_BOTTOM)
    # With a unicode key the character of a chess piece is retrieved
    # These characters are rendered as an image making use of the square coordinates
    # To do: Selected pieces will be rendered differently, maybe bigger font, bold or highlighted
    # textRect is x,y should be x,y,w,h size should be the entire square to centre & select
    def draw_pieces(self, square_coordinates: dict[str:tuple], pieces: list[object], win: object) -> None:
        for piece in pieces:
            piece_color_and_type = f"{piece.color}_{piece.type}".lower()
            if piece.selected:
                for pii in self.piece_selected_image_info:
                    if pii["name"] == piece_color_and_type:
                        piece_image = pii["image"]
                        piece_size = pii["size"]
            else:
                for pii in self.piece_image_info:
                    if pii["name"] == piece_color_and_type:
                        piece_image = pii["image"]
                        piece_size = pii["size"]

            piece_x_coordinate = (square_coordinates[piece.position][0] - piece_size[0] / 2) + (c.SQUARE_HEIGHT / 2)
            piece_y_coordinate = (square_coordinates[piece.position][1] - piece_size[1] / 2) + (c.SQUARE_WIDTH / 2)
            piece_coordinates = (piece_x_coordinate, piece_y_coordinate)
            win.blit(piece_image, piece_coordinates)

    # Draws board by looping through rows and columns, making sure rows and columns are checkered by checking if it's an even rows/column
    # Square color is drawn for every other row/column, the other squares have the background color
    def draw_squares(self, win: object) -> None:
        for row in range(c.NUM_OF_ROWS):
            if row % 2 != 0:
                for col in range(c.NUM_OF_COLS):
                    if col % 2 != 0:
                        pygame.draw.rect(win, c.SQUARE_COLOR, pygame.Rect\
                        (col * c.SQUARE_WIDTH, row * c.SQUARE_HEIGHT, \
                         c.SQUARE_WIDTH, c.SQUARE_HEIGHT))
                    else:
                        pass
            elif row % 2 == 0:
                for col in range(c.NUM_OF_COLS):
                    if col % 2 == 0:
                        pygame.draw.rect(win, c.SQUARE_COLOR, pygame.Rect\
                        (col * c.SQUARE_WIDTH, row * c.SQUARE_HEIGHT, \
                         c.SQUARE_WIDTH, c.SQUARE_HEIGHT))
                    else:
                        pass
     
    def draw_movement_dots(self, active_square_coordinates: list, occupied_squares: list[dict[str: str, str: str, str: str]], selected_piece: object, win: object) -> None:
        all_occupied_squares = []
        for square in occupied_squares:
            square_str = square["position"][c.COLUMN_IDX] + square["position"][c.ROW_IDX]
            all_occupied_squares.append(square_str)
        for asset in self.assets:
            if selected_piece.color == asset["color"]:
                if asset["name"] == "dot": 
                    dot_image = asset["image"]
                if asset["name"] == "strike_dot":
                    strike_image = asset["image"]
                else:
                    pass

        for available_position in selected_piece.available_positions:
            position_str = str(available_position[0]) + str(available_position[1])
            if position_str in all_occupied_squares:
                piece_x_coordinate = (active_square_coordinates[position_str][c.COLUMN_IDX] - c.STRIKED_DOT_IMAGE_SIZE[0] / 2) + (c.SQUARE_HEIGHT / 2)
                piece_y_coordinate = (active_square_coordinates[position_str][c.ROW_IDX] - c.STRIKED_DOT_IMAGE_SIZE[1] / 2) + (c.SQUARE_WIDTH / 2)
                piece_coordinates = (piece_x_coordinate, piece_y_coordinate)
                the_image = strike_image

            else:
                piece_x_coordinate = (active_square_coordinates[position_str][c.COLUMN_IDX] - c.DOT_IMAGE_SIZE[0] / 2) + (c.SQUARE_HEIGHT / 2)
                piece_y_coordinate = (active_square_coordinates[position_str][c.ROW_IDX] - c.DOT_IMAGE_SIZE[1] / 2) + (c.SQUARE_WIDTH / 2)
                piece_coordinates = (piece_x_coordinate, piece_y_coordinate)
                the_image = dot_image
            
            win.blit(the_image, piece_coordinates)

    def draw_castling_dot(self, square_coordinates, selected_piece: object, castle_square: str, win: object):

        for asset in self.assets:
            if selected_piece.color == asset["color"]:
                if asset["name"] == "bell": 
                    castle_image = asset["image"]
                else:
                    pass

        piece_x_coordinate = (square_coordinates[castle_square][c.COLUMN_IDX] - c.CASTLE_DOT_IMAGE_SIZE[0] / 2) + (c.SQUARE_HEIGHT / 2)
        piece_y_coordinate = (square_coordinates[castle_square][c.ROW_IDX] - c.CASTLE_DOT_IMAGE_SIZE[1] / 2) + (c.SQUARE_WIDTH / 2)
        piece_coordinates = (piece_x_coordinate, piece_y_coordinate)
        
        win.blit(castle_image, piece_coordinates)
    
            
    def draw_board(self, game:object, win:object) -> None:
        square_coordinates = game.board.active_square_coordinates
        occupied_squares = game.board.occupied_squares
        pieces = game.all_pieces
        selected_piece = game.active_player.selected_piece
        check = game.check
        long_castle = game.castling.long_castle_possible
        short_castle = game.castling.short_castle_possible

        self.draw_squares(win)
        self.draw_pieces(square_coordinates, pieces, win)
        if selected_piece is not None:
            self.draw_movement_dots(square_coordinates, occupied_squares, selected_piece, win)
            if selected_piece.type == "king":
                if long_castle:
                    self.draw_castling_dot(square_coordinates, game.active_player.selected_piece, game.active_player.long_king_castle_square, win)
                if short_castle:
                    self.draw_castling_dot(square_coordinates, game.active_player.selected_piece, game.active_player.short_king_castle_square, win)
            else:
                pass
        else:
            pass
        # if check:
        #     # self.draw_skull(square_coordinates, occupied_squares, win)
        # else:
        #     pass
        if game.checkmate:
            self.draw_checkmate(win)
                
    
    def draw_checkmate(self, win: object) -> None:
        print("drawing in checkmate now")
        # self.draw_board(game, win)
        
        for asset in self.assets:
            if asset["name"] == "skull": 
                skull_image = asset["image"]
                break
            else:
                pass
        top_text = self.font.render('Player 1 has won', True, 'black')
        width_rect = top_text.get_width()
        height_rect = top_text.get_height()
        pygame.draw.rect(win, 'white', self.top_rect, width_rect)
        win.blit(top_text, (200, 50))
        win.blit(skull_image, (200, 200))


    def load_piece_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_normal_path = piece["normal_path"]
            piece_size = piece["size"]
            piece_image_path = f'{self.assets_directory_2}{piece_normal_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_size))
            self.piece_image_info.append({"name": piece_name, "image": piece_image, "size": piece_size})
        return
    
    def load_selected_piece_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_selected_path = piece["selected_path"]
            piece_size = piece["size"]
            piece_image_path = f'{self.assets_directory_2}{piece_selected_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_size))
            self.piece_selected_image_info.append({"name": piece_name, "image": piece_image, "size": piece_size})
        return
    
    def load_asset_images(self, assets: c.ASSETS) -> None:
        for asset in assets: 
            asset_color = asset["color"]
            asset_name = asset["name"]
            asset_path = asset["path"]
            asset_size = asset["size"]
            asset_image_path = f"{self.assets_directory_2}{asset_path}"
            asset_image = pygame.image.load(asset_image_path)
            asset_image = pygame.transform.scale(asset_image, (asset_size))
            self.assets.append({"color": asset_color, "name": asset_name, "image": asset_image, "size": asset_size})
        
