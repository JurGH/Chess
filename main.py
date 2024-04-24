import pygame
import game as g 
import Classes.board as b
import Functionality.constants as c
import Functionality.start_screen as ssc
import Classes.players as p
import Classes.pieces as pi
import Classes.castle as ca
import create_assets as crea
import create_sounds as crs
import draw as d
from os import path 
from time import sleep

def create_players(player_names) -> list[p.Player]:
    all_players = []
    all_players.append(p.Player(player_names[0], c.PLAYER_COLORS[0]))
    all_players.append(p.Player(player_names[1], c.PLAYER_COLORS[1]))
    return all_players

def create_pieces() -> list[pi.Piece]:
    created_pieces = []
    for name, colors_and_positions in c.ALL_PIECES.items():
        for color, positions in colors_and_positions.items():
            for position in positions:
                created_pieces.append(pi.PIECE_CREATION_DICT[name](position, color))
    return created_pieces

if __name__ == "__main__":
    sound_library = crs.create_sounds()
    WIN = pygame.display.set_mode((c.SCREEN_HEIGHT, c.SCREEN_WIDTH))
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()

    def main():

        # creating all game elements
        board = b.Board()
        all_players = create_players(["player1", "player2"])
        all_pieces = create_pieces()
        castling = ca.Castling()

        # setting up game class with game elements stored
        game = g.Game(board, all_players, all_pieces, castling)

        # assign pieces to players and fill board squares with pieces
        game.set_up_game()
        # creating draw class to display all game elements to pygame client
        draw = d.Draw_board()
        draw.load_piece_images(crea.PIECE_IMAGES)
        draw.load_selected_piece_images(crea.PIECE_IMAGES)
        draw.load_asset_images(crea.ASSET_IMGS)

        # draw.get_start_screen_input_box()
        # # running start screen
        # start_game = False
        # input_box_is_active = False
        # player_names = []
        # player_name = ''
        # player_1_name = ''
        # player_2_name = ''
        # entered_names = 0
        
        # while not start_game:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
                
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_q:
        #                 pygame.quit()
                
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if draw.input_box.collidepoint(event.pos):
        #                 input_box_is_active = True
                    
        #         if event.type == pygame.KEYDOWN:
        #             if input_box_is_active:
        #                 if event.key == pygame.K_RETURN:
        #                     player_names.insert(0, player_name)
        #                     if entered_names == 0:
        #                         player_1_name = player_name
        #                         entered_names += 1
        #                         player_name = ''
        #                         input_box_is_active = False
        #                     else:
        #                         player_2_name = player_name
        #                         entered_names += 1
        #                 elif event.key == pygame.K_BACKSPACE:
        #                     player_name = player_name[:-1]
        #                 else:
        #                     if len(player_name) >= 10:
        #                         pass
        #                     else:
        #                         player_name += event.unicode
        #     """
        #     These surfaces are for the input of player names
        #     """
        #     WIN.fill(c.BACKGROUND_COLOR)
        #     draw.draw_input_box(WIN, player_name)
        #     if len(player_names) == 1: 
        #         draw.draw_player_1_name(WIN, player_1_name)
        #     else:
        #         draw.draw_player_1_name(WIN, player_1_name)
        #         draw.draw_player_2_name(WIN, player_2_name)
        #     pygame.display.update()
        #     if len(player_names) >= 2:
        #         sleep(2)
        #         start_game = True

    # running the game

        run = True
        game_on = True
        while run:

            WIN.fill(c.BACKGROUND_COLOR)
            draw.draw_board(game, WIN)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()

                    elif event.key == pygame.K_s:
                        game.board.toggle_square_coordinates()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_on is True: # game_on is false when checkmate or stalemate is true, so game ends but drawing continues
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
                                game_on = False
                            if game.stalemate is True:
                                print("It's a draw")
                                game_on = False
                    else: #game on false so end screen shown
                        if event.button == c.LEFT:
                            click_x, click_y = event.pos
                            decision = game.get_clicked_button(click_x, click_y
                                                    ,draw.play_again_button_range_x
                                                    ,draw.play_again_button_range_y
                                                    ,draw.quit_button_range_x
                                                    ,draw.quit_button_range_y)
                            print(decision)
                            if decision == c.QUIT:
                                pygame.quit()
                            
                            if decision == c.PLAY_AGAIN:
                                board = b.Board()
                                all_pieces = create_pieces()
                                castling = ca.Castling()
                                for player in all_players:
                                    player.reset_player()
                                # setting up game class with game elements stored
                                game = g.Game(board, all_players, all_pieces, castling)
                                game.set_up_game()
                                game_on = True

                        
                draw.draw_board(game, WIN)

if __name__ == "__main__":
    main()

