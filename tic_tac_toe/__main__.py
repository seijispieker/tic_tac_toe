"""Main script that starts the tic-tac-toe game."""
from typing import Tuple

from tic_tac_toe import tic_tac_toe


def main() -> None:
    """Start a while loop and ask user input."""
    game = tic_tac_toe.TicTacToe()
    i = 0  # Even numbers is X's turn, odd numbers is O's turn.

    while True:
        current_player = tic_tac_toe.PLAYERS[i % 2]

        print(game)
        print(f"{current_player}'s turn ***")

        if not game.move(current_player, *ask_indices()):
            print('Invalid move.')
            continue

        if winner := game.winner():
            if winner is True:
                print('It is a tie!')
            else:
                print(f'{winner} has won!')

        i += 1


def ask_indices() -> Tuple[int, int]:
    """Ask the user for row and column indices and return as tuple."""
    i, j = None, None  # i = row index, j = column index

    while True:
        i = input('Row index: ')

        if i.isnumeric():
            i = int(i)

            if i in tic_tac_toe.POSSIBLE_INDICES:
                break

        print('Invalid row index.')

    while True:
        j = input('Column index: ')

        if j.isnumeric():
            j = int(j)

            if j in tic_tac_toe.POSSIBLE_INDICES:
                break

        print('Invalid column index.')

    return i, j


if __name__ == '__main__':
    main()
