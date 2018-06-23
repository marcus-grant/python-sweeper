from .models import GameBoard
import game_view as view
#  import time


class GameController:
    def __init__(self, game_width, game_height, num_mines):
        self.minefield = GameBoard(game_width, game_height, num_mines)
        view.clear_screen()
        view.render_minefield()
        print(view.screen_shape())
