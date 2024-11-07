#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    It checks the column and the diagonals.
    """
    # Check the column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    """
    Solve the N Queens puzzle using backtracking.
    """

    def backtrack(row, board):
        # If we have placed all queens, print the solution
        if row == N:
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Reset for backtracking

    # Initialize the board with -1 (no queens placed yet)
    board = [-1] * N
    backtrack(0, board)


def main():
    """
    Main function to handle input and call the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
