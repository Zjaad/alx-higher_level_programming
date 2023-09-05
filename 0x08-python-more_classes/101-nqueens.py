#!/usr/bin/python3

import sys

def initialize_chessboard(size):
    """Initialize an `size`x`size` chessboard with empty squares."""
    board = [[' ' for _ in range(size)] for _ in range(size)]
    return (board)

def deep_copy_board(board):
    """Returns  deep copy of a chessboard."""
    return ([row[:] for row in board])

def find_solutions(board, row, queens, all_solutions):
    """Recurs  find solutions to the N-Queens puzzle."""
    if queens == len(board):
        all_solutions.append(board_to_positions(board))
        return (all_solutions)

    for col in range(len(board)):
        if board[row][col] == ' ':
            temp_board = deep_copy_board(board)
            temp_board[row][col] = 'Q'
            mark_attacked_squares(temp_board, row, col)
            all_solutions = find_solutions(temp_board, row + 1, queens + 1, all_solutions)

    return (all_solutions)

def board_to_positions(board):
    """Convert the chessboard to a list of queens positions."""
    positions = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                positions.append([row, col])
    return (positions)

def mark_attacked_squares(board, row, col):
    """Mark squares attacked by a queen on the board."""
    size = len(board)
    for i in range(size):
        board[row][i] = 'x' 
        board[i][col] = 'x' 

        
        if row - i >= 0 and col + i < size:
            board[row - i][col + i] = 'x'

        
        if row - i >= 0 and col - i >= 0:
            board[row - i][col - i] = 'x'

       
        if row + i < size and col + i < size:
            board[row + i][col + i] = 'x'

      
        if row + i < size and col - i >= 0:
            board[row + i][col - i] = 'x'

def print_solutions(solutions):
    """Print the solutions."""
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    chessboard = initialize_chessboard(N)
    solutions = find_solutions(chessboard, 0, 0, [])
    print_solutions(solutions)
