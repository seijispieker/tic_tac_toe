class Game:
    players = {'X', 'O'}
    SIZE = 3

    def __init__(self) -> None:
        """Initialize by filling a matrix with None."""
        self.matrix = [[None for _ in range(Game.SIZE)]
                       for _ in range(Game.SIZE)]

    def __str__(self) -> str:
        """Return a string representation of the current game."""
        line = Game.SIZE * 2 * '-' + '-\n'
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
        if i >= Game.SIZE or j >= Game.SIZE:
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
        for j in range(Game.SIZE):
            if self.matrix[0][j] and all(self.matrix[i][j] == self.matrix[0][j]
                                         for i in range(Game.SIZE)):
                return self.matrix[0][j]

    def check_diagonals(self) -> str | None:
        """Returns the player that has a full diagonal or None."""
        if self.matrix[0][0] and all(self.matrix[i][i] == self.matrix[0][0]
                                     for i in range(Game.SIZE)):
            return self.matrix[0]

        max_index = Game.SIZE - 1

        if (self.matrix[0][max_index] and
            all(self.matrix[i][Game.SIZE - i]
                == self.matrix[max_index][max_index]
                for i in range(Game.SIZE))):
            return self.matrix[max_index][max_index]

    def full_matrix(self) -> bool:
        """Return if matrix is full."""
        return (all(self.matrix[0]) and all(self.matrix[1])
                and all(self.matrix[2]))
