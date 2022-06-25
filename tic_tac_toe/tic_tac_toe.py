"""A three by three tic-tac-toe game.

Attributes:
    PLAYERS: List of the two possible players: 'X' or 'O'.
    POSSIBLE_INDICES: List of possible row and column indices.
"""

PLAYERS = ['X', 'O']
POSSIBLE_INDICES = [0, 1, 2]


class TicTacToe:
    """A three by three tic-tac-toe game.

    Attributes:
        _matrix: A list containing three lists of length three representing
            the tic-tac-toe game. A entry contains 'X', 'O' or None.
    """

    def __init__(self) -> None:
        """Constructs by initializing a 3 by 3 matrix with None."""
        self._matrix = []

        for _ in range(3):
            self._matrix.append([None for _ in range(3)])

    def __str__(self) -> str:
        """Returns a string representation of the current game."""
        string = '  0 1 2 \n'  # Column indices.
        line = f' {7*"-"}\n'
        string += line

        for i, row in enumerate(self._matrix):
            string += str(i)  # Row indices.

            for entry in row:
                if not entry:  # Entry is None thus empty.
                    entry = ' '

                string += f'|{entry}'

            string += f'|\n{line}'

        return string[:-1]

    def move(self, player: str, i: int, j: int) -> bool:
        """Makes a move with given player and returns if move is valid.

        Arguments:
            player: 'X' or 'O'.
            i: Row index 0, 1 or 2.
            j: Column index 0, 1 or 2.

        Returns:
            True if the move is valid or False if the move is invalid.
        """
        if i >= 3 or j >= 3:
            return False
        elif self._matrix[i][j]:
            return False
        else:
            self._matrix[i][j] = player
            return True

    def winner(self) -> str | bool:
        """Returns the winner or True if game is a tie or False if not ended."""
        return (self._check_rows() or self._check_columns()
                or self._check_diagonals() or self._full_matrix())

    def _check_rows(self) -> str | None:
        """Returns the player that has a full row or None."""
        for row in self._matrix:
            if row[0] and all(entry == row[0] for entry in row):
                return row[0]

    def _check_columns(self) -> str | None:
        """Returns the player that has a full column or None."""
        for j in range(3):
            if self._matrix[0][j] and all(self._matrix[i][j]
                                           == self._matrix[0][j]
                                           for i in range(3)):
                return self._matrix[0][j]

    def _check_diagonals(self) -> str | None:
        """Returns the player that has a full diagonal or None."""
        if self._matrix[0][0] and all(self._matrix[i][i]
                                       == self._matrix[0][0]
                                       for i in range(3)):
            return self._matrix[0]

        if self._matrix[0][2] and all(self._matrix[i][3 - i]
                                       == self._matrix[2][2]
                                       for i in range(3)):
            return self._matrix[2][2]

    def _full_matrix(self) -> bool:
        """Returns if matrix is full."""
        return (all(self._matrix[0]) and all(self._matrix[1])
                and all(self._matrix[2]))
