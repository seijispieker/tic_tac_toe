class Game:
    players = {'X', 'O'}
    SIZE = 3

    def __init__(self) -> None:
        """Initialize by filling a matrix with None."""
        self.matrix = [[None for _ in range(Game.SIZE)]
                       for _ in range(Game.SIZE)]

    def move(self, player: str, x: int, y: int) -> bool:
        """Make a move with given player and return if move is valid.

        Arguments:
        player -- 'X' or 'O'
        x -- x coordinate
        y -- y coordinate

        Returns true if the move is valid or returns false if the move is
        invalid.
        """
        if x > Game.MATRIX_SIZE or y > Game.MATRIX_SIZE:
            return False
        elif self.matrix[x][y]:
            return False
        else:
            self.matrix[x][y] = player
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
        for y in range(Game.SIZE):
            if self.matrix[0][y] and all(self.matrix[x][y] == self.matrix[0][y]
                                         for x in range(Game.SIZE)):
                return self.matrix[0][y]

    def check_diagonals(self):
        if self.matrix[0][0] and all(self.matrix[i][i] == self.matrix[0][0]
                                     for i in range(3)):
            return self.matrix[0]

        if self.matrix[0][2] and all(self.matrix[i][3 - i] == self.matrix[2][2]
                                     for i in range(3)):
            return self.matrix[2][2]

    def check_tie(self):
        return (all(self.matrix[0]) and all(self.matrix[1])
                and all(self.matrix[2]))
