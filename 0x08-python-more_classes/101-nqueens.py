#!/usr/bin/python3
import sys


def print_board(board):
    """
    Prints the board in the format specified in the prompt.
    """
    for row in board:
        print(row)


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col].
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens(board, col, solutions):
    """
    Recursive function to solve the N-Queens problem.
    """
    if col == len(board):
        # Base case: all queens are placed
        solutions.append(board[:])
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens(board, col+1, solutions)

            # Backtrack: remove the queen and try the next row
            board[row][col] = 0


def main():
    # Check the command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the board to all 0s
    board = [[0 for j in range(n)] for i in range(n)]

    # Find all solutions to the N-Queens problem
    solutions = []
    solve_n_queens(board, 0, solutions)

    # Print the solutions
    for solution in solutions:
        print_board(solution)
        print()


if __name__ == '__main__':
    main()
