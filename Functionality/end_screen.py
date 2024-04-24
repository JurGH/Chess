import create_assets as crea
import Functionality.constants as c 
import pygame 

def create_end_screen(game: object, font: pygame.font) -> dict[pygame.Rect]:
        end_screen_dict = {}
        if game.checkmate:
            top_text = f'{game.winning_player.name} has won'
        if game.stalemate:
            top_text = "It's a draw"

        top_text_size = font.size(top_text)
        top_start_y = ((c.SCREEN_HEIGHT / 4) - top_text_size[c.HEIGHT])
        top_start_x = ((c.SCREEN_WIDTH / 2) - (top_text_size[c.WIDTH] / 2))
        top_text_box = font.render(top_text, True, c.COLORS["GOLD"])
        top_text_rect = top_text_box.get_rect()
        top_rect = pygame.Rect(top_start_x, top_start_y,  top_text_size[c.WIDTH] * 1.05, top_text_size[c.HEIGHT] * 1.05)
        top_text_rect.center = top_rect.center

        bottom_text = "Would you like to play again?"
        bottom_text_size = font.size(bottom_text)
        bottom_start_y = ((c.SCREEN_HEIGHT * 0.75) + bottom_text_size[c.HEIGHT])
        bottom_start_x = ((c.SCREEN_WIDTH / 2) - (bottom_text_size[c.WIDTH] / 2))
        bottom_text_box = font.render(bottom_text, True, c.COLORS["GOLD"])
        bottom_text_rect = bottom_text_box.get_rect()
        bottom_rect = pygame.Rect(bottom_start_x, bottom_start_y,  bottom_text_size[c.WIDTH] * 1.05, bottom_text_size[c.HEIGHT] * 1.05)
        bottom_text_rect.center = bottom_rect.center

        play_again_text = "Play Again"
        play_again_size = bottom_rect.size
        play_again_width = play_again_size[0] / 2
        play_again_start_y = (bottom_rect[1] + bottom_rect[3])
        play_again_start_x = bottom_start_x
        play_again_text_box = font.render(play_again_text, True, "green")
        play_again_text_rect = play_again_text_box.get_rect()
        play_again_rect = pygame.Rect(play_again_start_x, play_again_start_y, play_again_width, play_again_size[c.HEIGHT])
        play_again_text_rect.center = play_again_rect.center

        quit_text = "Quit"
        quit_size = bottom_rect.size
        quit_width = quit_size[0] / 2
        quit_start_y = (bottom_rect[1] + bottom_rect[3])
        quit_start_x = bottom_start_x + play_again_width
        quit_text_box = font.render(quit_text, True, "red")
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