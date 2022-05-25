class Board:
    players = {'X', 'O'}

    def __init__(self):
        self.matrix = [[None for _ in range(3)] for _ in range(3)]

    def move(self, player, x, y):
        if player not in self.players:
            raise Exception('Invalid Player')

        if self.matrix[x][y]:
            raise Exception('Invalid Move.')

        self.matrix[x][y] = player
