import pygame
import Functionality.constants as c
from os import path

current_directory = path.dirname(__file__)
asset_files_directory = path.join(current_directory, "Assets")

def create_sounds():
    pygame.init()
    pygame.mixer.init()

    move_piece_sound_path = path.join(asset_files_directory, "move_piece.mp3")
    strike_piece_sound_path = path.join(asset_files_directory, "strike_piece.wav")
    castled_sound_path = path.join(asset_files_directory, "castling_3.wav")
    error_sound_path = path.join(asset_files_directory, "error_2.wav")

    move_piece_sound = pygame.mixer.Sound(move_piece_sound_path)
    strike_piece_sound = pygame.mixer.Sound(strike_piece_sound_path)
    error_sound = pygame.mixer.Sound(error_sound_path)
    error_sound.set_volume(0.2)
    castling_sound = pygame.mixer.Sound(castled_sound_path)

    sound_library = {
         c.PIECE_MOVED: move_piece_sound
        ,c.STRIKED: strike_piece_sound
        ,c.CASTLED: castling_sound
        ,c.INVALID_MOVE: error_sound}
    
    return sound_library