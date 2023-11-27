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
        self.image_directory = os.path.join(self.current_directory, "Assets")
        self.image_directory_2 = os.path.join(self.image_directory, "img\\")
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
     
    def draw_available_squares_in_move(self, win: object) -> None:
        pass

    def draw_board(self, square_coordinates: dict[str:tuple], pieces:list[object], win:object) -> None:
        self.draw_squares(win)
        self.draw_pieces(square_coordinates, pieces, win)

    def load_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_normal_path = piece["normal_path"]
            piece_scale = piece["scale"]
            piece_image_path = f'{self.image_directory_2}{piece_normal_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_scale))
            self.piece_image_info.append({"name": piece_name, "image": piece_image, "scale": piece_scale})
        return
    
    def load_selected_images(self, pieces_image_data: c.PIECE_IMAGES):
        for piece in pieces_image_data:
            piece_name = piece["name"]
            piece_selected_path = piece["selected_path"]
            piece_scale = piece["scale"]
            piece_image_path = f'{self.image_directory_2}{piece_selected_path}'
            piece_image = pygame.image.load(piece_image_path)
            piece_image = pygame.transform.scale(piece_image, (piece_scale))
            self.piece_selected_image_info.append({"name": piece_name, "image": piece_image, "scale": piece_scale})
        return



    