import os


def screen_shape():
    """ Returns the 2D dimensions of the terminal as tuple

    Returns:
        (int, int)  Terminal dimensions in row major order
    """
    return os.popen('stty size', 'r').read().split()


def clear_screen():
    print("\033[H\033[J")


def render_minefield():
    print("""
          MINEFIELD
          .........
          .........
          .........
          """)
