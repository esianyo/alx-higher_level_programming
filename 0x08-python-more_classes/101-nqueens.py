#!/usr/bin/python3
"""
A chess board
Esianyo Dzisenu
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Solve the N queens problem using backtracking
    """
    n = len(board)

    # Base case: All queens are placed
    if col >= n:
        solution = []
        for row in range(n):
            queen_pos = [row, board[row].index(1)]
            solution.append(queen_pos)
        solutions.append(solution)
        return

    # Recursive case: Try placing a queen in each row of the current column
    for row in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1, solutions)

            # Backtrack and remove the queen
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print the solutions to the N queens problem
    """
    for solution in solutions:
        print(solution)


def nqueens(N):
    """
    Solve the N queens problem for a given board size N
    """
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
