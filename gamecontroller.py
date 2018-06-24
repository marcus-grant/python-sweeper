#  import termios
#  import sys
#  import tty
from minefieldmodel import MinefieldModel
import gameview as gv
import curses


class GameController:
    def __init__(self, game_width, game_height, num_mines, screen):
        self.minefield = MinefieldModel(game_width, game_height, num_mines)
        #  self.screen = self.init_screen()
        self.screen = screen
        self.game_is_running = True
        self.screen = ''
        gv.clear_screen()

    def map_input_to_game_action(self, inp):
        if inp == 'KEY_UP' or inp == 'k' or inp == 'w':
            self.minefield.move_cursor_vertically(-1)
        elif inp == 'KEY_DOWN' or inp == 'j' or inp == 's':
            self.minefield.move_cursor_vertically(1)
        elif inp == 'KEY_LEFT' or inp == 'h' or inp == 'a':
            self.minefield.move_cursor_horizontally(-1)
        elif inp == 'KEY_RIGHT' or inp == 'l' or inp == 'd':
            self.minefield.move_cursor_horizontally(1)
        elif inp == 'q':
            self.game_is_running = False

    def play(self, screen):
        self.screen = screen
        while self.game_is_running:
            # First print the screen
            #  gv.print_screen(self.minefield.minefield, self.minefield.cursor)
            print(self.minefield.cursor)
            # Then wait for user input to determine what to do next
            key = self.screen.getkey()
            print(key)
            #  key = self.screen.getch()
            self.map_input_to_game_action(key)
