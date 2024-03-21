import pygame
import os
import Functionality.constants as c

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
        self.play_again_button_range_x = ()
        self.play_again_button_range_y = ()
        self.quit_button_range_x = ()
        self.quit_button_range_y = ()
        

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

        if game.checkmate or game.stalemate:
            for asset in self.assets:
                if asset["name"] == "skull" and game.checkmate: 
                    end_screen_image = asset["image"]
                    break
                if asset["name"] == "stalemate" and game.stalemate:
                    end_screen_image = asset["image"]
                    break
                else:
                    pass

            self.draw_game_over(win, game, end_screen_image)

    def create_end_screen(self, game: object) -> dict[pygame.Rect]:
        
        end_screen_dict = {}
        
        if game.checkmate:
            top_text = f'{game.winning_player.name} has won'
            
        if game.stalemate:
            top_text = "It's a draw"

        
        top_text_size = self.font.size(top_text)
        top_start_y = ((c.SCREEN_HEIGHT / 4) - top_text_size[c.HEIGHT])
        top_start_x = ((c.SCREEN_WIDTH / 2) - (top_text_size[c.WIDTH] / 2))
        top_text_box = self.font.render(top_text, True, c.COLORS["GOLD"])
        top_text_rect = top_text_box.get_rect()
        top_rect = pygame.Rect(top_start_x, top_start_y,  top_text_size[c.WIDTH] * 1.05, top_text_size[c.HEIGHT] * 1.05)
        top_text_rect.center = top_rect.center

        bottom_text = "Would you like to play again?"
        bottom_text_size = self.font.size(bottom_text)
        bottom_start_y = ((c.SCREEN_HEIGHT * 0.75) + bottom_text_size[c.HEIGHT])
        bottom_start_x = ((c.SCREEN_WIDTH / 2) - (bottom_text_size[c.WIDTH] / 2))
        bottom_text_box = self.font.render(bottom_text, True, c.COLORS["GOLD"])
        bottom_text_rect = bottom_text_box.get_rect()
        bottom_rect = pygame.Rect(bottom_start_x, bottom_start_y,  bottom_text_size[c.WIDTH] * 1.05, bottom_text_size[c.HEIGHT] * 1.05)
        bottom_text_rect.center = bottom_rect.center

        play_again_text = "Play Again"
        play_again_size = bottom_rect.size
        play_again_width = play_again_size[0] / 2
        play_again_start_y = (bottom_rect[1] + bottom_rect[3])
        play_again_start_x = bottom_start_x
        play_again_text_box = self.font.render(play_again_text, True, "green")
        play_again_text_rect = play_again_text_box.get_rect()
        play_again_rect = pygame.Rect(play_again_start_x, play_again_start_y, play_again_width, play_again_size[c.HEIGHT])
        play_again_text_rect.center = play_again_rect.center

        quit_text = "Quit"
        quit_size = bottom_rect.size
        quit_width = quit_size[0] / 2
        quit_start_y = (bottom_rect[1] + bottom_rect[3])
        quit_start_x = bottom_start_x + play_again_width
        quit_text_box = self.font.render(quit_text, True, "red")
        quit_text_rect = quit_text_box.get_rect()
        quit_rect = pygame.Rect(quit_start_x, quit_start_y, quit_width, quit_size[c.HEIGHT])
        quit_text_rect.center = quit_rect.center

        end_screen_dict.update({"top_text_box": top_text_box
                                ,"top_text_rect": top_text_rect
                                ,"top_rect": top_rect
                                ,"bottom_text_box": bottom_text_box
                                ,"bottom_text_rect": bottom_text_rect
                                ,"bottom_rect": bottom_rect
                                ,"play_again_text_box": play_again_text_box
                                ,"play_again_text_rect": play_again_text_rect
                                ,"play_again_rect": play_again_rect
                                ,"quit_text_box": quit_text_box
                                ,"quit_text_rect": quit_text_rect
                                ,"quit_rect": quit_rect
                                })
        
        return end_screen_dict
    
    def get_end_screen_buttons(self, end_screen_dict: dict) -> dict:
        play_again_button_x_min = end_screen_dict["play_again_rect"][0]
        play_again_button_x_max = end_screen_dict["play_again_rect"][0] + end_screen_dict["play_again_rect"][2]
        play_again_button_y_min = end_screen_dict["play_again_rect"][1]
        play_again_button_y_max = end_screen_dict["play_again_rect"][1] + end_screen_dict["play_again_rect"][3]
        quit_button_x_min = end_screen_dict["quit_rect"][0]
        quit_button_x_max = end_screen_dict["quit_rect"][0] + end_screen_dict["play_again_rect"][2]
        quit_button_y_min = end_screen_dict["quit_rect"][1]
        quit_button_y_max = end_screen_dict["quit_rect"][1] + end_screen_dict["play_again_rect"][3]

        self.play_again_button_range_x = (play_again_button_x_min, play_again_button_x_max)
        self.play_again_button_range_y = (play_again_button_y_min, play_again_button_y_max)
        self.quit_button_range_x = (quit_button_x_min, quit_button_x_max)
        self.quit_button_range_y = (quit_button_y_min, quit_button_y_max)
        

    
    def draw_game_over(self, win: object, game: object, end_screen_image: pygame.image) -> None:
        # self.draw_board(game, win)
        
        end_screen_dict = self.create_end_screen(game)
        self.get_end_screen_buttons(end_screen_dict)
        pygame.draw.rect(win, 'black', end_screen_dict["top_rect"], 0, 6, 6, 6, 6)
        win.blit(end_screen_dict["top_text_box"], end_screen_dict["top_text_rect"])
        pygame.draw.rect(win, 'black', end_screen_dict["bottom_rect"], 0, 6, 6, 6, 6)
        win.blit(end_screen_dict["bottom_text_box"], end_screen_dict["bottom_text_rect"])
        pygame.draw.rect(win, 'black', end_screen_dict["play_again_rect"], 0, 6, 6, 6, 6)
        win.blit(end_screen_dict["play_again_text_box"], end_screen_dict["play_again_text_rect"])
        pygame.draw.rect(win, 'black', end_screen_dict["quit_rect"], 0, 6, 6, 6, 6)
        win.blit(end_screen_dict["quit_text_box"], end_screen_dict["quit_text_rect"])
        end_screen_y = ((c.SCREEN_HEIGHT / 2) - (c.END_SCREEN_IMAGE_SIZE[c.HEIGHT]/2))
        end_screen_x= ((c.SCREEN_WIDTH / 2) - (c.END_SCREEN_IMAGE_SIZE[c.WIDTH]/2))
        win.blit(end_screen_image, (end_screen_y, end_screen_x))


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
        
