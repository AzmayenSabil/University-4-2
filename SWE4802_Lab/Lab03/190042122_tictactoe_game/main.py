from loguru_config import logger
from pysnooper import snoop


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


# Decorate the play_game function with pysnooper
@snoop()
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter row (0-2): "))
            col = int(input(f"Player {current_player}, enter column (0-2): "))

            if not (0 <= row < 3 and 0 <= col < 3):
                raise ValueError("Invalid move. Cell selection is out of bounds. Try again.")

            if not is_valid_move(board, row, col):
                raise ValueError("Invalid move. Cell already occupied. Try again.")
        except ValueError as e:
            logger.error(e)
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            logger.info(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            logger.info("It's a draw!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()

