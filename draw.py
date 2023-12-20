import pygame
import os
import Functionality.constants as c

class Draw_board():
    
    def __init__(self):
        self.piece_image_info: list[dict[str:str, str: pygame.Surface, str: tuple]]
        self.piece_image_info: list[dict[str:str, str: pygame.Surface, str: tuple]]
        self.piece_image_info = []
        self.piece_selected_image_info = []
        self.current_directory = os.path.dirname(__file__)
        self.assets_directory = os.path.join(self.current_directory, "Assets")
        self.assets_directory_2 = os.path.join(self.assets_directory, "img\\")
        self.red_dot_path = os.path.join(self.assets_directory_2, "red_dot.png")
        self.yellow_dot_path = os.path.join(self.assets_directory_2, "yellow_dot.png")
        self.yellow_strike_path = os.path.join(self.assets_directory_2, "yellow_strike_dot.png")
        self.yellow_skull_path = os.path.join(self.assets_directory_2, "yellow_skull.png")
        self.red_strike_path = os.path.join(self.assets_directory_2, "red_strike_dot.png")
        self.red_skull_path = os.path.join(self.assets_directory_2, "red_skull.png")
        self.yellow_bell_path = os.path.join(self.assets_directory_2, "yellow_bell.png")
        self.red_bell_path = os.path.join(self.assets_directory_2, "red_bell.png")
        self.red_dot_image = pygame.image.load(self.red_dot_path)
        self.red_dot_image = pygame.transform.scale(self.red_dot_image, (c.DOT_IMAGE_SIZE))
        self.yellow_dot_image = pygame.image.load(self.yellow_dot_path)
        self.yellow_dot_image = pygame.transform.scale(self.yellow_dot_image, (c.DOT_IMAGE_SIZE))
        self.yellow_strike_image = pygame.image.load(self.yellow_strike_path)
        self.yellow_strike_image = pygame.transform.scale(self.yellow_strike_image, (c.STRIKED_DOT_IMAGE_SIZE))
        self.yellow_skull_image = pygame.image.load(self.yellow_skull_path)
        self.yellow_skull_image = pygame.transform.scale(self.yellow_skull_image, (c.SKULL_IMAGE_SIZE))
        self.red_strike_image = pygame.image.load(self.red_strike_path)
        self.red_strike_image = pygame.transform.scale(self.red_strike_image, (c.STRIKED_DOT_IMAGE_SIZE))
        self.red_skull_image = pygame.image.load(self.red_skull_path)
        self.red_skull_image = pygame.transform.scale(self.red_skull_image, (c.SKULL_IMAGE_SIZE))
        self.yellow_bell_image = pygame.image.load(self.yellow_bell_path)
        self.yellow_bell_image = pygame.transform.scale(self.yellow_bell_image, (c.CASTLE_DOT_IMAGE_SIZE))
        self.red_bell_image = pygame.image.load(self.red_bell_path)
        self.red_bell_image = pygame.transform.scale(self.red_bell_image, (c.CASTLE_DOT_IMAGE_SIZE))


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
                        piece_scale = pii["scale"]
            else:
                for pii in self.piece_image_info:
                    if pii["name"] == piece_color_and_type:
                        piece_image = pii["image"]
                        piece_scale = pii["scale"]

            piece_x_coordinate = (square_coordinates[piece.position][0] - piece_scale[0] / 2) + (c.SQUARE_HEIGHT / 2)
            piece_y_coordinate = (square_coordinates[piece.position][1] - piece_scale[1] / 2) + (c.SQUARE_WIDTH / 2)
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
        if selected_piece.color == "WHITE":
            dot_image = self.yellow_dot_image
            strike_image = self.yellow_strike_image
        else:
            dot_image = self.red_dot_image
            strike_image = self.red_strike_image

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
        if selected_piece.color == "WHITE":
            castle_image = self.yellow_bell_image
        else:
            castle_image = self.red_bell_image

        piece_x_coordinate = (square_coordinates[castle_square][c.COLUMN_IDX] - c.CASTLE_DOT_IMAGE_SIZE[0] / 2) + (c.SQUARE_HEIGHT / 2)
        piece_y_coordinate = (square_coordinates[castle_square][c.ROW_IDX] - c.CASTLE_DOT_IMAGE_SIZE[1] / 2) + (c.SQUARE_WIDTH / 2)
        piece_coordinates = (piece_x_coordinate, piece_y_coordinate)
        
        win.blit(castle_image, piece_coordinates)
    
            
    def draw_skull(self, active_square_coordinates, occupied_squares, win):
        skull_image = self.yellow_skull_image
        win.blit(skull_image, (400, 25))

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
        if check:
            self.draw_skull(square_coordinates, occupied_squares, win)
        else:
            pass

    def load_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_normal_path = piece["normal_path"]
            piece_scale = piece["scale"]
            piece_image_path = f'{self.assets_directory_2}{piece_normal_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_scale))
            self.piece_image_info.append({"name": piece_name, "image": piece_image, "scale": piece_scale})
        return
    
    def load_selected_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_selected_path = piece["selected_path"]
            piece_scale = piece["scale"]
            piece_image_path = f'{self.assets_directory_2}{piece_selected_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_scale))
            self.piece_selected_image_info.append({"name": piece_name, "image": piece_image, "scale": piece_scale})
        return