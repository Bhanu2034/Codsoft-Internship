import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {
        'X': 1,
        'O': -1,
        'tie': 0,
    }

    if check_winner(board, 'X'):
        return -1
    elif check_winner(board, 'O'):
        return 1
    elif is_board_full(board):
        return 0

    empty_cells = get_empty_cells(board)

    if is_maximizing:
        max_eval = float('-inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[cell[0]][cell[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for cell in empty_cells:
            board[cell[0]][cell[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[cell[0]][cell[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_val = float('-inf')
    best_move = None
    for cell in get_empty_cells(board):
        board[cell[0]][cell[1]] = 'O'
        move_val = minimax(board, 0, False, float('-inf'), float('inf'))
        board[cell[0]][cell[1]] = ' '

        if move_val > best_val:
            best_move = cell
            best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's move
        player_move = input("Enter your move (row and column, separated by space): ")
        player_row, player_col = map(int, player_move.split())
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue

        print_board(board)

        # Check if player wins
        if check_winner(board, 'X'):
            print("You win! Congratulations!")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

        # AI's move
        print("AI's move:")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = 'O'

        print_board(board)

        # Check if AI wins
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break

        # Check for a tie
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
