"""Tests functionality of the tic_tac_toe.tic_tac_toe module."""
import itertools
import random
from typing import List
import unittest

from tic_tac_toe import tic_tac_toe


class TicTacToeTestCase(unittest.TestCase):
    """Base class for each of the Tic-Tac-Toe test cases."""

    def assert_matrix_deep_copy(self, copy: List[List[tic_tac_toe.Player]],
                                original: List[List[tic_tac_toe.Player]]) -> None:
        """Asserts if copy matrix is an deep copy of original matrix."""
        self.assertListEqual(copy, original, '_matrix is not a copy')
        self.assertIsNot(copy, original, '_matrix is not a deep copy')

        # Assert for lower depth.
        for _matrix_row, original_row in zip(copy, original):
            self.assertIsNot(_matrix_row, original_row,
                             'row of _matrix is not a deep copy')


class TicTacToeInitialMatrixTestCase(TicTacToeTestCase):
    """Tests TicTacToe instance initialized without argument.

    Attributes:
        tic_tac_toe: TicTacToe instance.
    """

    def setUp(self) -> None:
        """Creates a TicTacToe instance without argument."""
        self.tic_tac_toe = tic_tac_toe.TicTacToe()

    def test_tic_tac_toe_init(self) -> None:
        """Tests __init__ method of TicTacToe without arguments.

        Asserts if _matrix attribute is a deep copy of INITIAL_MATRIX, the
        default value of the paramater matrix.
        """
        self.assert_matrix_deep_copy(copy=self.tic_tac_toe._matrix,
                                     original=tic_tac_toe.INITIAL_MATRIX)


class TicTacToeRandomSampleTestCase(TicTacToeTestCase):
    """Tests TicTacToe instances initialized with a random sample.

    Attributes:
        sample: Random sample of all possible matrices.
    """

    def setUp(self, k: int = 10**10) -> None:
        """Generates a random sample of possible matrices.

        Arguments:
            k: Size of the random sample.
        """
        # Generates all possible 3 by 3 matrices with all possible Player Enums.
        rows = itertools.product((player for player in tic_tac_toe.Player),
                                 repeat=tic_tac_toe.SIZE)
        matrices = itertools.product(rows, repeat=tic_tac_toe.SIZE)

        # Makes sure that k is not bigger than number of possibilities.
        if k > (n := len(tic_tac_toe.Player)**(tic_tac_toe.SIZE**2)):
            k = n

        self.sample = random.sample(list(matrices), k=k)

    def test_tic_tac_toe_init(self) -> None:
        """Tests __init__ method of TicTacToe with random sample of arguments.

        Asserts if _matrix attributes are a deep copies of random sample of size
        k of all the possible 3 by 3 matrices.
        """
        # Asserts for each possible matrix in the random sample.
        for matrix in self.sample:
            with self.subTest(matrix=matrix):
                matrix_list = [list(row) for row in matrix]
                tic_tac_toe_object = tic_tac_toe.TicTacToe(matrix_list)
                self.assert_matrix_deep_copy(copy=tic_tac_toe_object._matrix,
                                             original=matrix_list)


if __name__ == '__main__':
    unittest.main()
