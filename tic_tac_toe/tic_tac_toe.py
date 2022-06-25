"""A three by three tic-tac-toe game.

Attributes:
    PLAYERS: List of the two possible players: 'X' or 'O'.
"""

PLAYERS = ['X', 'O']


class TicTacToe:
    """A three by three tic-tac-toe game.

    Attributes:
        __matrix: A list containing three lists of length three representing
            the tic-tac-toe game. A entry contains 'X', 'O' or None.
    """

    def __init__(self) -> None:
        """Constructs by initializing a 3 by 3 matrix with None."""
        self.__matrix = []

        for _ in range(3):
            self.__matrix.append([None for _ in range(3)])

    def __str__(self) -> str:
        """Returns a string representation of the current game."""
        line = f'{7*"-"}\n'
        string = line

        for row in self.__matrix:
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
        elif self.__matrix[i][j]:
            return False
        else:
            self.__matrix[i][j] = player
            return True

    def winnner(self) -> str | bool:
        """Returns the winner or True if game is a tie or False if not ended."""
        return (self.__check_rows() or self.__check_columns()
                or self.__check_diagonals() or self.__full_matrix())

    def __check_rows(self) -> str | None:
        """Returns the player that has a full row or None."""
        for row in self.__matrix:
            if row[0] and all(entry == row[0] for entry in row):
                return row[0]

    def __check_columns(self) -> str | None:
        """Returns the player that has a full column or None."""
        for j in range(3):
            if self.__matrix[0][j] and all(self.__matrix[i][j]
                                           == self.__matrix[0][j]
                                           for i in range(3)):
                return self.__matrix[0][j]

    def __check_diagonals(self) -> str | None:
        """Returns the player that has a full diagonal or None."""
        if self.__matrix[0][0] and all(self.__matrix[i][i]
                                       == self.__matrix[0][0]
                                       for i in range(3)):
            return self.__matrix[0]

        if self.__matrix[0][2] and all(self.__matrix[i][3 - i]
                                       == self.__matrix[2][2]
                                       for i in range(3)):
            return self.__matrix[2][2]

    def __full_matrix(self) -> bool:
        """Returns if matrix is full."""
        return (all(self.__matrix[0]) and all(self.__matrix[1])
                and all(self.__matrix[2]))
