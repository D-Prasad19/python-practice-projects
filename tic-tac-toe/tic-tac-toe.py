# Tic-Tac-Toe (CLI) – Two-player console game using Python basics

def print_board(board):
    """Display the current board."""
    cells = [c if c is not None else str(i+1) for i, c in enumerate(board)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} \n")

def check_winner(board, mark):
    """Return True if 'mark' has any winning combination."""
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False

def is_draw(board):
    """Return True if the board is full and no winner."""
    return all(cell is not None for cell in board)

def get_move(board, player):
    """Ask the current player for a valid move (1–9)."""
    while True:
        raw = input(f"Player {player}, choose a cell (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue
        pos = int(raw)
        if not 1 <= pos <= 9:
            print("Number must be between 1 and 9.")
            continue
        idx = pos - 1
        if board[idx] is not None:
            print("That cell is already taken. Try another.")
            continue
        return idx

def play_once():
    """Play a single game of Tic-Tac-Toe."""
    board = [None] * 9
    current = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Player X goes first.\n")
    print_board(board)

    while True:
        idx = get_move(board, current)
        board[idx] = current
        print_board(board)

        if check_winner(board, current):
            print(f"🎉 Player {current} wins!")
            break
        if is_draw(board):a
            print("It's a draw! 🤝")
            break

        current = "O" if current == "X" else "X"

def main():
    while True:
        play_once()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
