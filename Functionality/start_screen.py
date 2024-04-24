import pygame
import create_assets as crea

def create_start_input_box(font: pygame.font, player_names=""):          
    input_box = pygame.Rect(crea.INPUT_BOX)
    text_color = pygame.Color("black")
    txt_surface = font.render(player_names, True, text_color)
    txt_surface_rect = txt_surface.get_rect()
    txt_surface_rect.center = input_box.center
    return input_box, txt_surface ,txt_surface_rect

def create_player_1_box(font, player_name):
    text_color = pygame.Color("black")
    player_1_text = f'{player_name}'
    player_1_surface = font.render(player_1_text, True, text_color)
    player_1_surface_rect = player_1_surface.get_rect()
    player_1_box = pygame.Rect(crea.PLAYER_1_NAME_BOX)
    player_1_surface_rect.center = player_1_box.center
    return player_1_box, player_1_surface, player_1_surface_rect

def create_player_2_box(font, player_name):
    text_color = pygame.Color("black")
    player_2_text = f'{player_name}'
    player_2_surface = font.render(player_2_text, True, text_color)
    player_2_surface_rect = player_2_surface.get_rect()
    player_2_box = pygame.Rect(crea.PLAYER_2_NAME_BOX)
    player_2_surface_rect.center = player_2_box.center
    return player_2_box, player_2_surface, player_2_surface_rect
    