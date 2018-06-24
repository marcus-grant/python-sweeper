import numpy as np
import random
import celltypes as CellTypes
from functools import reduce


class MinefieldModel:
    def __init__(self, width, height, num_mines):
        """ Initializes the minefield with randomly located mines

        Parameters
        ----------

        width (int)     Width of minefield
        height (int)    Height of minefield
        num_mines (int) Number of mines in minefield
        """
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.mines_remaining = num_mines
        self.minefield = np.full(shape=(width, height),
                                 fill_value=CellTypes.UNKNOWN,
                                 dtype=np.uint8)
        self.place_mines()

    def copy_minefield(self):
        return self.minefield.copy()

    def place_mines(self):
        num_cells = self.width * self.height
        locations = random.sample(range(num_cells), self.num_mines)
        for loc in locations:
            row = loc // self.width
            col = loc % self.height
            self.minefield[row][col] = CellTypes.MINE

    def cell_is_revealed(self, row, col):
        return True if self.minefield[row][col] < 9 else False

    def cell_has_mine(self, row, col):
        return self.minefield[row][col] == CellTypes.MINE

    def adjacent_locations(self, row, col):
        up = row - 1 if row > 0 else row
        down = row + 1 if row < (self.height - 1) else row
        left = col - 1 if col > 0 else col
        right = col + 1 if col < (self.width - 1) else col
        return [(up, left), (up, col), (up, right),
                (row, left), (row, right),
                (down, left), (down, col), (down, right)]

    def num_adjacent_mines(self, row, col):
        return reduce((lambda x, y: x + y), self.adjacent_locations(row, col))

#  def reveal_cell(self, row, col):
#      """ Reveals the contents of a cell.
#
#      When the user uncovers a cell the game needs to know if it's a mine,
#      so it can end the game.
#      If it's an empty cell, how many mines are adjacent.
#      If its neighbors have 0 adjacent mines recursively reveal them as well.
#      If it's an already revealed cell do nothing.
#      """
#      if self.cell_is_revealed(row, col):
#          return
