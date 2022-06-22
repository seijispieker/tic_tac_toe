class Game:
    PLAYERS = {'X', 'O'}

    def __init__(self) -> None:
        """Initialize by filling a 3 by 3 matrix with None."""
        self.matrix = [[None for _ in range(3)] for _ in range(3)]

    def __str__(self) -> str:
        """Return a string representation of the current game."""
        line = f'{7*"-"}\n'
        string = line

        for row in self.matrix:
            for entry in row:
                if not entry:  # Entry is None thus empty.
                    entry = ' '

                string += f'|{entry}'

            string += f'|\n{line}'

        return string[:-1]

    def move(self, player: str, i: int, j: int) -> bool:
        """Make a move with given player and return if move is valid.

        Arguments:
        player -- 'X' or 'O'
        i -- row index
        j -- column index

        Returns true if the move is valid or returns false if the move is
        invalid.
        """
        if i >= 3 or j >= 3:
            return False
        elif self.matrix[i][j]:
            return False
        else:
            self.matrix[i][j] = player
            return True

    def winnner(self) -> str | bool:
        """Returns the winner or True if game is a tie or False if not ended."""
        return (self.check_rows() or self.check_columns()
                or self.check_diagonals() or self.full_matrix())

    def check_rows(self) -> str | None:
        """Returns the player that has a full row or return None."""
        for row in self.matrix:
            if row[0] and all(entry == row[0] for entry in row):
                return row[0]

    def check_columns(self) -> str | None:
        """Returns the player that has a full column or None."""
        for j in range(3):
            if self.matrix[0][j] and all(self.matrix[i][j] == self.matrix[0][j]
                                         for i in range(3)):
                return self.matrix[0][j]

    def check_diagonals(self) -> str | None:
        """Returns the player that has a full diagonal or None."""
        if self.matrix[0][0] and all(self.matrix[i][i] == self.matrix[0][0]
                                     for i in range(3)):
            return self.matrix[0]

        if self.matrix[0][2] and all(self.matrix[i][3 - i] == self.matrix[2][2]
                                     for i in range(3)):
            return self.matrix[2][2]

    def full_matrix(self) -> bool:
        """Return if matrix is full."""
        return (all(self.matrix[0]) and all(self.matrix[1])
                and all(self.matrix[2]))
