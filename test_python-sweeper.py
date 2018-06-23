import Minefield from python-sweeper
import unittest

class TestMinefield:
    """ Test the Minefield class
    """

    def test_minefield_params(self):
        """ Test that the minefield gets initialized with correct parameters
        """
        tminefield = Minefield(10, 10)
        print(Minefield.min
