import pygame
import game as g 
import Classes.board as b
import Functionality.constants as ca
import Classes.players as p
import Classes.pieces as pi
import Classes.castle as ca
import draw as d
import os
import time 

def create_players(player_names) -> list[p.Player]:
    all_players = []
    all_players.append(p.Player(player_names[0], ca.PLAYER_COLORS[0]))
    all_players.append(p.Player(player_names[1], ca.PLAYER_COLORS[1]))
    return all_players

def create_pieces() -> list[pi.Piece]:
    created_pieces = []
    for name, colors_and_positions in ca.ALL_PIECES.items():
        for color, positions in colors_and_positions.items():
            for position in positions:
                created_pieces.append(pi.PIECE_CREATION_DICT[name](position, color))
    return created_pieces

current_directory = os.path.dirname(__file__)
asset_files_directory = os.path.join(current_directory, "Assets")

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # need to fix that this points to a relative position instead of absolute path
    move_piece_sound_path = os.path.join(asset_files_directory, "move_piece.mp3")
    strike_piece_sound_path = os.path.join(asset_files_directory, "strike_piece.wav")
    castled_sound_path = os.path.join(asset_files_directory, "castling_3.wav")
    error_sound_path = os.path.join(asset_files_directory, "error_2.wav")

    move_piece_sound = pygame.mixer.Sound(move_piece_sound_path)
    strike_piece_sound = pygame.mixer.Sound(strike_piece_sound_path)
    error_sound = pygame.mixer.Sound(error_sound_path)
    error_sound.set_volume(0.2)
    castling_sound = pygame.mixer.Sound(castled_sound_path)


    sound_library = {
         ca.PIECE_MOVED: move_piece_sound
        ,ca.STRIKED: strike_piece_sound
        ,ca.CASTLED: castling_sound
        ,ca.INVALID_MOVE: error_sound}

    WIN = pygame.display.set_mode((ca.SCREEN_HEIGHT, ca.SCREEN_WIDTH))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    def main():
        start_game = False
        input_box = pygame.Rect(ca.INPUT_BOX)
        print(input_box.center)