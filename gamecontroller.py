import termios
import sys
import tty
from minefieldmodel import MinefieldModel
import gameview as gv


def getch():
    """gets a single character input from STDIN
    """
    def getch_helper():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return getch_helper()


class GameController:
    def __init__(self, game_width, game_height, num_mines):
        self.minefield = MinefieldModel(game_width, game_height, num_mines)
        self.cursor = (0, 0)
        gv.clear_screen()
        print('init with screen : {}'.format(gv.screen_shape()))

    def update_screen(self):
        gv.clear_screen()
        gv.print_screen(self.minefield, self.cursor)

    def cursor_up(self):
        _tmp = self.cursor[0]
        self.cursor[0] = _tmp - 1 if _tmp > 0 else _tmp

    def game_loop(self):
        while True:
            #  self.update_screen()
            input_key = getch()
            import pdb; pdb.set_trace()  # XXX BREAKPOINT
            print(repr(input_key))
            if input_key == 'q':
                sys.exit(0)

            if input_key == '\\x1b[A':
                #  self.cursor_up()
                print('up')
            elif input_key == '\x1b[B':
                    print("down")
            elif input_key == '\x1b[C':
                    print("right")
            elif input_key == '\x1b[D':
                    print("left")
