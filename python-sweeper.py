#!/usr/bin/env python3
import curses
import sys
from argparser import get_args
from gamecontroller import GameController


def init_screen(keypad_mode=False):
    _s = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if keypad_mode:
        _s.keypad(True)
    return _s


def stop_screen(screen):
    curses.echo()
    curses.nocbreak()
    screen.keypad(False)
    curses.endwin()


def exit_app(ecode, screen):
    stop_screen(screen)
    sys.exit(ecode)


if __name__ == '__main__':
    a = get_args()
    s = init_screen()
    g = GameController(a[0], a[1], a[2], s)
    try:
        curses.wrapper(g.play)
    except KeyboardInterrupt:
        exit_app(1, s)
    except curses.error:
        print("Please don't resize the window!")
        exit_app(1, s)
    except RuntimeError as e:
        print(str(e))
        exit_app(1, s)

    exit_app(0, s)
