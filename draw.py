import pygame
import Functionality.constants as c

class Draw_board():
    
    # With a unicode key the character of a chess piece is retrieved
    # These characters are rendered as an image making use of the square coordinates
    # To do: Selected pieces will be rendered differently, maybe bigger font, bold or highlighted
    # textRect is x,y should be x,y,w,h size should be the entire square to centre & select
    def draw_pieces(self, square_coordinates: dict[str:tuple], pieces: list[object], win: object) -> None:
        chess_piece_font_bold = pygame.font.SysFont("segoeuisymbol", 80, italic = True)
        chess_piece_font = pygame.font.SysFont("segoeuisymbol", 80, italic = False)
        for piece in pieces:
            unicode_key = f'{piece.color}_{piece.type}'.lower()
            rendertext = c.UNICODE_PIECES[unicode_key]
            color = piece.color.upper()
            
            if piece.selected is True:
                text = chess_piece_font_bold.render(rendertext,True, c.COLORS[color])
                char_size = text.get_size()
                # not sure if x and y are correct, x seems to hold the wrong value. 
                textRect = text.get_rect(x = (square_coordinates[piece.position][0] - char_size[0] / 2) + (c.SQUARE_HEIGHT / 2)  
                                         , y = (square_coordinates[piece.position][1] - char_size[1] / 2) + (c.SQUARE_WIDTH / 2))
            elif piece.selected is False:
                text = chess_piece_font.render(rendertext,True, c.COLORS[color])
                char_size = text.get_size()
                textRect = text.get_rect(x = (square_coordinates[piece.position][0] - char_size[0] / 2) + (c.SQUARE_HEIGHT / 2)
                                         , y = (square_coordinates[piece.position][1] - char_size[1] / 2) + (c.SQUARE_WIDTH / 2))
            win.blit(text, textRect)

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