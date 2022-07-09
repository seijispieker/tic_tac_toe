"""A three by three tic-tac-toe game.

Attributes:
    POSSIBLE_INDICES: List of possible row and column indices.
"""

from enum import Enum
from typing import Iterable, List


POSSIBLE_INDICES = {0, 1, 2}


class Player(Enum):
    """Possible players."""
    X = 'X'
    O = 'O'
    EMPTY = ' '


INITIAL_MATRIX = [
    [Player.EMPTY, Player.EMPTY, Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY],
    [Player.EMPTY, Player.EMPTY, Player.EMPTY],
]


class TicTacToe:
    """A three by three tic-tac-toe game.

    Attributes:
        current_player: The player whoes turn it is.
        _matrix: A list containing three lists of length three representing the
            tic-tac-toe game. A entry contains a Player Enum.
    """

    def __init__(self,
                 matrix: Iterable[Iterable[Player]] = INITIAL_MATRIX) -> None:
        """Constructs TicTacToe object by deep copying matrix.

        Args:
            matrix: An iterable that has three iterables that has three Player
                Enums.

        Raises:
            ValueError: If matrix has wrong dimensions.
        """
        self.current_player = Player.X  # Player whoes turn it is.
        self._matrix: List[List[Player]] = []

        for row in matrix:
            self._matrix.append([entry for entry in row])

        if (len(self._matrix) != 3 or len(self._matrix[0]) != 3
                or len(self._matrix[1]) != 3 or len(self._matrix[2]) != 3):
            raise ValueError('Matrix has wrong dimensions.')

    def __str__(self) -> str:
        """Returns a string representation of the current game."""
        lines: List[str] = []  # List of lines.
        LINE_OF_LINES = f' {7*"-"}'

        lines.append('  0 1 2 ')  # Column indices.
        lines.append(LINE_OF_LINES)

        for i, row in enumerate(self._matrix):
            line: List[str] = []  # List of strings that form the line.
            line.append(str(i))  # Row indices.

            for entry in row:
                line.append(entry.value)

            line.append('')  # To make sure line ends with '|'.
            lines.append('|'.join(line))
            lines.append(LINE_OF_LINES)

        return '\n'.join(lines)

    def move(self, i: int, j: int) -> None:
        """Makes a move with the player whoes turn it is with the given indices.

        Arguments:
            i: Row index 0, 1 or 2.
            j: Column index 0, 1 or 2.

        Raises:
            IndexError: If i or j is not equal to 0, 1 or 2.
            InvalidMoveError: If the move is not possible.
        """
        if i not in POSSIBLE_INDICES:
            raise IndexError('Row index i can only be 0, 1 or 2.')
        elif j not in POSSIBLE_INDICES:
            raise IndexError('Column index j can only be 0, 1 or 2.')
        elif self._matrix[i][j] is not Player.EMPTY:
            raise ValueError('Move is not possible.')
        else:  # Move can be made.
            self._matrix[i][j] = self.current_player

            # Update the player whoes turn is next.
            if self.current_player is Player.X:
                self.current_player = Player.O
            else:
                self.current_player = Player.X

    def winner(self) -> Player | bool:
        """Returns the winner or True if tie.

        Returns:
            Player: Player.X or Player.O if X or O won respectively. Returns
                Player.EMPTY if there is no winner and no tie.
            bool: Returns True if tie.
        """
        return (self._check_rows() or self._check_columns()
                or self._check_diagonals() or self._full_matrix())

    def _check_rows(self) -> Player | bool:
        """Returns player that has full row or False."""
        for row in self._matrix:
            if all(entry is row[0] for entry in row):
                return row[0]
        else:
            return False

    def _check_columns(self) -> Player | bool:
        """Returns player that has full row or False."""
        for j in range(3):
            if all(self._matrix[i][j] is self._matrix[0][j] for i in range(3)):
                return self._matrix[0][j]
        else:
            return False

    def _check_diagonals(self) -> Player | bool:
        """Returns player that has a full diagonal or False."""
        if all(self._matrix[i][i] is self._matrix[0][0] for i in range(3)):
            return self._matrix[0][0]
        elif all(self._matrix[i][2 - i] is self._matrix[0][2]
                 for i in range(3)):
            return self._matrix[2][2]
        else:
            return False

    def _full_matrix(self) -> bool:
        """Returns True matrix is full or False if not full."""
        return all(self._matrix[i][j] is not Player.EMPTY
                   for i in range(3) for j in range(3))
