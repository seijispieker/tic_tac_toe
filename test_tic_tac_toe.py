"""Tests functionality of the tic_tac_toe.tic_tac_toe module."""
import unittest

from tic_tac_toe import tic_tac_toe


class InitTicTacToeTestCase(unittest.TestCase):
    """Tests __init__ method of TicTacToe."""

    def test_tic_tac_toe_init_without_argument(self) -> None:
        """Tests if _matrix attribute is a deep copy of INITIAL_MATRIX."""
        tic_tac_toe_object = tic_tac_toe.TicTacToe()
        self.assertListEqual(tic_tac_toe_object._matrix,
                             tic_tac_toe.INITIAL_MATRIX,
                             '_matrix is not equal to INITIAL_MATRIX')
        self.assertIsNot(tic_tac_toe_object._matrix,
                         tic_tac_toe.INITIAL_MATRIX,
                         '_matrix is not a deep copy of INITIAL_MATRIX')


if __name__ == '__main__':
    unittest.main()
