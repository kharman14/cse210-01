"""
Tic Tac Toe
Author: Katie Harman
"""

def main():
    # create game board
    game = create_board()

    num = 1
    while not (winner(game)):
        display_game(game)
        num = take_turn(num, game)
    display_game(game)
    print("Good game. Thanks for playing!")


def create_board():
    board = []
    for square in range(9):
        board.append(square+1)
    return board

def display_game(board):
    # Display the game board
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("- + - + -")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("- + - + -")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def take_turn(current, board):
    if (current % 2) != 0:
        player = "x"
    else:
        player = "o"
    answer = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[answer - 1] = player
    current += 1
    return current

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[4] == board[8] or 
            board[0] == board[3] == board[6] or
            board[2] == board[4] == board[6] or
            board[2] == board[5] == board[8] or
            board[1] == board[4] == board[7])

if __name__ == "__main__":
    main()