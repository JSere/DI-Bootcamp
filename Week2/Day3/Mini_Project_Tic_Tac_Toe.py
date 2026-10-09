# Mini-Project - Tic Tac Toe

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '] 
]

def display_board(board):
    for row in board:
        print(" | ".join(row))     

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))

        
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == ' ':
                    return row, col
                else:
                    print(" Invalid move! Spot already taken. try again!")
            else:
                print(" Invalid move! Numbers must be 0, 1, or 2. try again!")
        except ValueError:
            print(" Invalid input! Please enter numbers only.")

def check_win(board, player):
    
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play():
    current_player = 'X'

    while True:
        display_board(board)
        
        row, col = player_input(board, current_player)
        board[row][col] = current_player
        

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

    
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play()