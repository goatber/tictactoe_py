"""
Tic-tac-toe
===========
Created to learn extremely basic and non-random AI in python.

Code influenced by Tech with Tim on youtube:
https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg
"""
import random

board = [" " for x in range(10)]


def insert_letter(letter, pos):
    board[pos] = letter


def space_is_free(pos) -> bool:
    return board[pos] == " "


def print_board():
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")


def clear_board(bo):
    for i in range(1, len(bo)):
        bo[i] = " "


def is_winner(bo, letter) -> bool:
    # Rows (cases 1-3)
    # Columns (cases 4-6)
    # Diagonals (cases 7 and 8)

    return  (bo[7] == letter and bo[8] == letter and bo[9] == letter) or\
            (bo[4] == letter and bo[5] == letter and bo[6] == letter) or\
            (bo[1] == letter and bo[2] == letter and bo[3] == letter) or\
            (bo[1] == letter and bo[4] == letter and bo[7] == letter) or\
            (bo[2] == letter and bo[5] == letter and bo[8] == letter) or\
            (bo[3] == letter and bo[6] == letter and bo[9] == letter) or\
            (bo[1] == letter and bo[5] == letter and bo[9] == letter) or\
            (bo[3] == letter and bo[5] == letter and bo[7] == letter)


def player_move():
    running = True  # While player is currently placing
    while running:
        move = input("Select a position to place an X (1-9) > ")
        try:
            move = int(move)  # Checks if input is numerical
            if 10 > move > 0:  # Checks if desired move is in between 1 and 9 exclusively
                if space_is_free(move):  # Checks if desired space is free
                    running = False  # Stops player move, no further input needed
                    insert_letter("X", move)  # Place X
                else:
                    print("This space is already occupied.")
            else:
                print("Type a valid numerical value within the range!")
        except:
            print("Type a valid numerical value!")


def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0  # After checking all possible moves, if none are possible returns 0

    for letter in ["O", "X"]:  # Checks for computer win condition then player win condition
        for i in possible_moves:
            board_copy = board[:]  # Stores board copy to memory
            board_copy[i] = letter
            if is_winner(board_copy, letter):
                move = i
                return move

    # If no win condition found:
    corners_open = []
    for i in possible_moves:  # Checks for all open corners then moves if available
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    # If center is open, move there
    if 5 in possible_moves:
        return 5

    # If no win condition, open corner, or open center:
    edges_open = []
    for i in possible_moves:  # Checks for all open edges then moves if available
        if i in [2, 4, 6, 8]:
            edges_open.append(i)
    if len(edges_open) > 0:
        move = select_random(edges_open)

    # Return edge move or 0 if no move found
    return move


def select_random(_list):
    list_length = len(_list)
    random_pos = random.randrange(0, list_length)
    return _list[random_pos]


def is_board_full() -> bool:
    if board.count(" ") >= 1:
        return False
    else:
        return True


def main():
    print("Tic-Tac-Toe | Player vs. Computer")
    print("Position 1 is top left, position 9 is bottom right.")
    print_board()

    while not(is_board_full()):  # As long as board is not full, run:
        if not(is_winner(board, "O")):  # player's move
            player_move()
            print_board()
        else:
            print("Computer wins!")
            break

        if not(is_winner(board, "X")):  # computer's move
            move = computer_move()
            if move == 0:  # Computer cannot find valid move therefore board is full
                print("Tie game!")
            else:
                insert_letter("O", move)
                print("Computer placed at", move)
                print_board()
        else:
            print("Player wins!")
            break

    if is_board_full():  # If the board is full, tie is declared
        print("Tie game!")


if __name__ == "__main__":
    clear_board(board)
    main()

while True:  # While game is running:
    play_again = input("Play again? (Y/N) > ")  # Does the player want to reset?
    if play_again.lower() == "y" or play_again.lower() == "yes":  # If yes, clear the board and rerun the game
        clear_board(board)
        main()
    else:  # Otherwise, quit the game
        raise SystemExit()




