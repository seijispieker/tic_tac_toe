"""Tests functionality of the tic_tac_toe.tic_tac_toe module."""
import itertools
import random
from typing import List
import unittest

from tic_tac_toe import tic_tac_toe


class TicTacToeInitTestCase(unittest.TestCase):
    """Tests __init__ method of TicTacToe."""

    def test_tic_tac_toe_init_initial_matrix(self) -> None:
        """Tests __init__ method of TicTacToe without arguments.

        Asserts if _matrix attribute is a deep copy of INITIAL_MATRIX, the
        default value of the paramater matrix.
        """
        tic_tac_toe_object = tic_tac_toe.TicTacToe()
        self.assert_matrix_deep_copy(copy=tic_tac_toe_object._matrix,
                                     original=tic_tac_toe.INITIAL_MATRIX)

    def test_tic_tac_toe_init_random_sample(self, k: int = 10**10) -> None:
        """Tests __init__ method of TicTacToe with random sample of arguments.

        Asserts if _matrix attribute is a deep copy of random sample of size
        k of all the possible 3 by 3 matrices.
        """
        # Generates all possible 3 by 3 matrices with all possible Player Enums.
        rows = itertools.product((player for player in tic_tac_toe.Player),
                                 repeat=tic_tac_toe.SIZE)
        matrices = itertools.product(rows, repeat=tic_tac_toe.SIZE)

        # Makes sure that k is not bigger than number of possibilities.
        if k > (n := len(tic_tac_toe.Player)**(tic_tac_toe.SIZE**2)):
            k = n

        sample = random.sample(list(matrices), k=k)

        # Assert for each matrix in the random sample.
        for matrix in sample:
            with self.subTest(matrix=matrix):
                matrix_list = [list(row) for row in matrix]
                tic_tac_toe_object = tic_tac_toe.TicTacToe(matrix_list)
                self.assert_matrix_deep_copy(copy=tic_tac_toe_object._matrix,
                                             original=matrix_list)

    def assert_matrix_deep_copy(self, copy: List[List[tic_tac_toe.Player]],
                                original: List[List[tic_tac_toe.Player]]) -> None:
        """Asserts if copy matrix is an deep copy of original matrix."""
        self.assertListEqual(copy, original, '_matrix is not a copy')
        self.assertIsNot(copy, original, '_matrix is not a deep copy')

        # Assert for lower depth.
        for _matrix_row, original_row in zip(copy, original):
            self.assertIsNot(_matrix_row, original_row,
                             'row of _matrix is not a deep copy')


if __name__ == '__main__':
    unittest.main()
