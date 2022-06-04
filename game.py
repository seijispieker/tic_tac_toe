class Game:
    players = {'X', 'O'}
    SIZE = 3

    def __init__(self):
        self.matrix = [[None for _ in range(3)] for _ in range(3)]

    def move(self, player, x, y):
        if self.matrix[x][y]:
            return False
        else:
            self.matrix[x][y] = player
            return True

    def winnner(self):
        return (self.check_rows() or self.check_columns()
                or self.check_diagonals() or self.check_tie())

    def check_rows(self):
        for row in self.matrix:
            if row[0] and all(entry == row[0] for entry in row):
                return row[0]

    def check_columns(self):
        for j in range(3):
            if self.matrix[0][j] and all(self.matrix[i][j] == self.matrix[0][j]
                                         for i in range(3)):
                return self.matrix[0][j]

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
