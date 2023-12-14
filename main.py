import pygame
import game as g 
import Classes.board as b
import Functionality.constants as c
import Classes.players as p
import Classes.pieces as pi
import Classes.castle as ca
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
         c.PIECE_MOVED: move_piece_sound
        ,c.STRIKED: strike_piece_sound
        ,c.CASTLED: castling_sound
        ,c.INVALID_MOVE: error_sound}

    WIN = pygame.display.set_mode((c.SCREEN_HEIGHT, c.SCREEN_WIDTH))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    # creating all game elements
    board = b.Board()
    all_players = create_players()
    all_pieces = create_pieces()
    castling = ca.Castling()


    # setting up game class with game elements stored
    game = g.Game(board, all_players, all_pieces, castling)

    # assign pieces to players and fill board squares with pieces
    game.set_up_game()
    # creating draw class to display all game elements to pygame client
    draw = d.Draw_board()
    draw.load_images(c.PIECE_IMAGES)
    draw.load_selected_images(c.PIECE_IMAGES)



    num_of_click_in_turn = 0
    # running the game
    run = True
    while run:

        WIN.fill(c.BACKGROUND_COLOR)
        draw.draw_board(game.board.active_square_coordinates, board.occupied_squares, game.all_pieces, game.selected_piece, game.check, WIN)
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
                    clicked_square = game.get_clicked_square(click_x, click_y)
                    if clicked_square is None:
                        print("this should never happen, clicked square is none")

                    game.handle_player_action(clicked_square)
                    if game.state_turn != c.PIECE_SELECTED and game.state_turn != c.PIECE_NOT_SELECTED and game.state_turn != c.PIECE_NOT_MOVED:
                        sound_library[game.state_turn].play(0)

                    else:
                        pass
                    
                    game.reset_turn()
                    
                    if game.checkmate is True:
                        for player in all_players:
                            if player.on_turn is False:
                                print(f"Gratz {player.name} you won!!")
                            if player.on_turn is True:
                                print(f"You lost {player.name}")
                    if game.stalemate is True:
                        print("It's a draw")

   
            draw.draw_board(game.board.active_square_coordinates, board.occupied_squares, game.all_pieces, game.selected_piece, game.check, WIN)