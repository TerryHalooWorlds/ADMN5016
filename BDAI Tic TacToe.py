# Game set up
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Print board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])

player = "X"

# Game mechanics
# Place an X (or an O) in one of the 9 slots
while True:
    position = input("Please choose a position from 1-9: ")

    # Exit game
    if position == "exit":
        exit()

    position = int(position)

    # Check if position is already taken
    if board[position - 1] == "-":
        board[position - 1] = player
    else:
        print("Player " + player + ", " + "position " + str(position) + " already taken!")
        continue

    # Print board
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    # Check if PLayer Wins
    # Row
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # Column
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # Diagonal
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    winner = row_1 + row_2 + row_3 + column_1 + column_2 + column_3 + diagonal_1 + diagonal_2

    if winner >= 1:
        print("PLayer " + player + "won!")
        exit()
    elif "-" not in board:
        print("It's a tie!")
        exit()

    # Switch players
    if player == "X":
        player = "O"
    else:
        player = "X"

    print("Player " + player + "'s turn.")

    # Game ends - row, col, diagonal; tie
