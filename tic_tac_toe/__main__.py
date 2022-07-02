"""Main script that starts the tic-tac-toe game."""
from typing import Tuple

from tic_tac_toe import tic_tac_toe


def main() -> None:
    """Start a while loop and ask user input."""
    game = tic_tac_toe.TicTacToe()
    print(game)

    while True:
        print(f"{game.current_player.value}'s turn")

        try:
            game.move(*ask_indices())
        except (IndexError, tic_tac_toe.InvalidMoveError) as error:
            print(error)
            continue

        print(game)

        if winner := game.winner():
            if winner is True:
                print('It is a tie!')
            elif (winner is tic_tac_toe.Player.X or
                  winner is tic_tac_toe.Player.O):
                print(f'{winner} has won!')
            else:
                continue

            break


def ask_indices() -> Tuple[int, int]:
    """Ask the user for row and column indices and return as tuple."""
    while True:
        i_string = input('Row index: ')

        if i_string.isnumeric():
            i = int(i_string)

            if i in tic_tac_toe.POSSIBLE_INDICES:
                break

        print('Invalid row index.')

    while True:
        j_string = input('Column index: ')

        if j_string.isnumeric():
            j = int(j_string)

            if j in tic_tac_toe.POSSIBLE_INDICES:
                break

        print('Invalid column index.')

    return i, j


if __name__ == '__main__':
    main()
