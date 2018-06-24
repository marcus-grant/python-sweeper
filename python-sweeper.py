#!/usr/bin/env python3


if __name__ == '__main__':
    from gamecontroller import GameController
    #  from gameboard import GameBoard
    import argparse
    import sys

    prog_name = 'python-sweeper'
    prog_desc = 'A minesweeper clone for the command line.'
    parser = argparse.ArgumentParser(prog=prog_name, description=prog_desc)
    parser.add_argument('-x', '--width',
                        type=int, action='store', dest='x', default=16)
    parser.add_argument('-y', '--height',
                        type=int, action='store', dest='y', default=16)
    parser.add_argument('-m', '--mines',
                        type=int, action='store', dest='mines', default=0)
    args = parser.parse_args()
    board_width = args.x
    board_height = args.y
    num_game_tiles = board_width * board_height
    num_mines = args.mines

    if board_width <= 0 or board_height <= 0:
        print('[ERROR]: Board dimensions must be positive integers!')
        sys.exit(1)

    # set default number of bombs in game
    if num_mines == 0:
        num_mines = int((num_game_tiles) / 6)

    # make sure there are no more than width*height - 1 mines
    if num_mines >= num_game_tiles:
        error_msg = '[ERROR]: Number of mines ({}) can\'t exceed or equal '
        error_msg += 'number of game tiles ({})'
        error_msg = error_msg.format(num_mines, num_game_tiles)
        print(error_msg)
        sys.exit(1)

    #  GameBoard(board_width, board_height, num_mines)
    game_controller = GameController(board_width, board_height, num_mines)
    game_controller.game_loop()
