#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueens_util(board, col, N, solutions):
    if col == N:
        temp = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    temp.append([i, j])
        solutions.append(temp)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = nqueens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        return 1

    if N < 4:
        print("N must be at least 4")
        return 1

    board = [[0 for x in range(N)] for y in range(N)]
    solutions = []

    nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
