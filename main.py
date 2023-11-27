import pygame
import game as g 
import Classes.board as b
import Functionality.constants as c
import Classes.players as p
import Classes.pieces as pi
import draw as d
import os

def create_players() -> list[p.Player]:
    all_players = []
    all_players.append(p.Player(c.PLAYER_NAMES[0], c.PLAYER_COLORS[0]))
    all_players.append(p.Player(c.PLAYER_NAMES[1], c.PLAYER_COLORS[1]))
    return all_players

def create_pieces() -> list[pi.Piece]:
    created_pieces = []
    for name, colors_and_positions in c.ALL_PIECES.items():
        for color, positions in colors_and_positions.items():
            for position in positions:
                created_pieces.append(pi.PIECE_CREATION_DICT[name](position, color))
    return created_pieces

current_directory = os.path.dirname(__file__)
sound_files_directory = os.path.join(current_directory, "Assets")

if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    # need to fix that this points to a relative position instead of absolute path
    move_piece_sound_path = os.path.join(sound_files_directory, "move_piece.mp3")
    strike_piece_sound_path = os.path.join(sound_files_directory, "strike_piece.wav")
    castled_sound_path = os.path.join(sound_files_directory, "castling_3.wav")
    error_sound_path = os.path.join(sound_files_directory, "error.mp3")
    move_piece_sound = pygame.mixer.Sound(move_piece_sound_path)
    strike_piece_sound = pygame.mixer.Sound(strike_piece_sound_path)
    error_sound = pygame.mixer.Sound(error_sound_path)
    castling_sound = pygame.mixer.Sound(castled_sound_path)

    WIN = pygame.display.set_mode((c.SCREEN_HEIGHT, c.SCREEN_WIDTH))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    # creating all game elements
    board = b.Board()
    all_players = create_players()
    all_pieces = create_pieces()

    # setting up game class with game elements stored
    game = g.Game(board, all_players, all_pieces)

    # assign pieces to players and fill board squares with pieces
    game.set_up_game()
    # creating draw class to display all game elements to pygame client
    draw = d.Draw_board()
    draw.load_images(c.PIECE_IMAGES)
    draw.load_selected_images(c.PIECE_IMAGES)

    # running the game
    run = True
    while run:

        WIN.fill(c.BACKGROUND_COLOR)
        draw.draw_board(game.board.active_square_coordinates, game.all_pieces, WIN)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                elif event.key == pygame.K_s:
                    game.board.toggle_square_coordinates()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == c.LEFT:
                    click_x, click_y = event.pos
                    if game.num_of_click_in_turn == 0:
                        game.handle_player_first_action(click_x, click_y)

                    elif game.num_of_click_in_turn == 1:
                        game.handle_player_second_action(click_x, click_y)
                        print(f"game.piece_moved = {game.piece_moved}")
                        if game.castled is True:
                            castling_sound.play(0)
                            game.reset_turn()
                            game.castled = False
                            break

                        if game.piece_striked is True:
                            strike_piece_sound.play(0)
                            game.reset_turn()
                            if game.checkmate is True:
                                print(f"winning_player = {game.winning_player.name}")
                                print(f"losing_player = {game.losing_player.name}")

                        elif game.piece_moved is True:
                            move_piece_sound.play(0)
                            #calculating positions all pieces after moving a piece
                            game.reset_turn()
                            if game.checkmate is True:
                                print(f"winning_player = {game.winning_player.name}")
                                print(f"losing_player = {game.losing_player.name}")
                        elif game.piece_moved is None:
                            print("piece moved is none")
                            game.reset_turn()
                            if game.checkmate is True:
                                print(f"winning_player = {game.winning_player.name}")
                                print(f"losing_player = {game.losing_player.name}")
                        else:
                            error_sound.play(0)
                            if game.checkmate is True:
                                print(f"winning_player = {game.winning_player.name}")
                                print(f"losing_player = {game.losing_player.name}")
                            game.reset_turn()                           



                
            draw.draw_board(game.board.active_square_coordinates, game.all_pieces, WIN)