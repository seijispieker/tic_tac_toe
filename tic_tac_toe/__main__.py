"""Main script that starts the tic-tac-toe game."""
from typing import List, Tuple

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
                print(f'{winner.value} has won!')
            else:
                continue

            break


def ask_indices() -> Tuple[int, int]:
    """Ask the user for row and column indices and return as tuple."""
    while True:
        user_input = input("Indices '<row index>, <column index>': ")
        # Split user input by comma and strip leading and trailing characters.
        indices_string: List[str] = list(map(str.strip, user_input.split(',')))

        if (len(indices_string) is 2 and indices_string[0].isnumeric()
                and indices_string[1].isnumeric()):
            return int(indices_string[0]), int(indices_string[1])
        else:
            print('Invalid indices.')


if __name__ == '__main__':
    main()
