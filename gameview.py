import os
import celltypes as CellTypes
import cellsymbols as CellSymbols
import ansicodes as ANSI


def screen_shape():
    """ Returns the 2D dimensions of the terminal as tuple

    Returns:
        (int, int)  Terminal dimensions in row major order
    """
    return os.popen('stty size', 'r').read().split()


def clear_screen():
    print("\033[H\033[J")


def render_cell(cell_code):
    if cell_code == CellTypes.UNKNOWN:
        return '{}{}'.format(ANSI.RESET_ALL, CellSymbols.UNKNOWN)
    elif cell_code == CellTypes.MINE:
        return '{}{}'.format(ANSI.FG_RED, CellSymbols.MINE)
    elif cell_code == CellTypes.CURSOR:
        return '{}{}'.format(ANSI.FG_MAGENTA, CellSymbols.CURSOR)


def render_minefield(minefield, cursor):
    #  minefield_view = np.chararray((minefield.height, minefield.width),
    #                                unicode=True)
    minefield_view = []
    for row_idx in range(len(minefield.minefield)):
        view_row = []
        minefield_row = minefield.minefield[row_idx]
        for col_idx in range(len(minefield_row)):
            if row_idx == cursor[0] and col_idx == cursor[1]:
                view_row.append(render_cell(CellTypes.CURSOR))
            else:
                cell = minefield_row[col_idx]
                view_row.append(render_cell(cell))
        minefield_view.append(view_row)
    return minefield_view


def print_screen(minefield, cursor):
    minefield_view = render_minefield(minefield, cursor)
    for row in minefield_view:
        print(''.join(row))
