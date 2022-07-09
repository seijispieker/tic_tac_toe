"""Tests functionality of the tic_tac_toe.tic_tac_toe module."""
import unittest

from tic_tac_toe import tic_tac_toe


class InitialTicTacToeTestCase(unittest.TestCase):
    """Tests the initialisation of TicTacToe object."""

    def setUp(self) -> None:
        """Create a TicTacToe object."""
        self.tic_tac_toe = tic_tac_toe.TicTacToe()

    def test_tic_tac_toe_initial_matrix(self) -> None:
        """Tests the initialisation of _matrix attribute of TicTacToe object."""
        E = tic_tac_toe.Player.EMPTY
        initial_matrix = [[E, E, E], [E, E, E], [E, E, E]]
        self.assertListEqual(self.tic_tac_toe._matrix, initial_matrix,
                             'Invalid intial matrix.')


if __name__ == '__main__':
    unittest.main()
