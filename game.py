def print_board(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2] + '\n' +
          '-+-+-\n' + 
          board[1][0] + '|' + board[1][1] + '|' + board[1][2] + '\n' +
          '-+-+-\n' +
          board[2][0] + '|' + board[2][1] + '|' + board[2][2] + '\n' )


def player_turn(board, symbol):
    while(True):
        player_move = input("pleas pick your move between 1-9 ?")

        if valid_move(board, player_move):
            place_the_move(board, player_move, symbol)
            break
        

def valid_move(board, move):
    if move == '1' and board[0][0] == ' ':
        return True
    elif move == '2' and board[0][1] == ' ':
        return True
    elif move == '3' and board[0][2] == ' ':
        return True
    elif move == '4' and board[1][0] == ' ':
        return True
    elif move == '5' and board[1][1] == ' ':
        return True
    elif move == '6' and board[1][2] == ' ':
        return True
    elif move == '7' and board[2][0] == ' ':
        return True
    elif move == '8' and board[2][1] == ' ':
        return True
    elif move == '9' and board[2][2] == ' ':
        return True
    else:
        print("Invalid move\nTry again\n")
        return False


def place_the_move(board, move, symbol):
    if move == '1':
        board[0][0] = symbol
        return
    elif move == '2':
        board[0][1] = symbol
        return
    elif move == '3':
        board[0][2] = symbol
        return
    elif move == '4':
        board[1][0] = symbol
        return
    elif move == '5':
        board[1][1] = symbol
        return
    elif move == '6':
        board[1][2] = symbol
        return
    elif move == '7':
        board[2][0] = symbol
        return
    elif move == '8':
        board[2][1] = symbol
        return
    elif move == '9':
        board[2][2] = symbol
        return


def is_game_finish(board):
    if (board[0][0] != ' ' and board[0][1] != ' ' and board[0][2] != ' ' and 
        board[1][0] != ' ' and board[1][1] != ' ' and board[1][2] != ' ' and 
        board[2][0] != ' ' and board[2][1] != ' ' and board[2][2] != ' '):
        return True
    else:
        return False
        

def who_won(board, symbol):
    if ( (board[0][0] == symbol and board [0][1] == symbol and board [0][2] == symbol) or 
         (board[0][0] == symbol and board [1][1] == symbol and board [2][2] == symbol ) or 
         (board[0][0] == symbol and board [1][0] == symbol and board [2][0] == symbol ) or 
         (board[1][0] == symbol and board [1][1] == symbol and board [1][2] == symbol ) or 
         (board[2][0] == symbol and board [2][1] == symbol and board [2][2] == symbol ) or 
         (board[2][0] == symbol and board [1][1] == symbol and board [0][2] == symbol ) or 
         (board[0][1] == symbol and board [1][1] == symbol and board [2][1] == symbol ) or 
         (board[0][2] == symbol and board [1][2] == symbol and board [2][2] == symbol ) ):
        return True
    else:
        return False


def game_score(board):
    if who_won(board, 'X'):
        return 1
    elif who_won(board, 'O'):
        return -1
    elif is_game_finish(board):
        return 0
    else:
        return None


def ai_turn(board, symbol):
    move = best_move(board, symbol)
    board[move[0]][move[1]] = symbol


def best_move(board, symbol):
    best_score = -float('inf') if symbol == 'X' else float('inf')
    move = None
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == ' ':
                board[i][j] = symbol
                score = minimax(board, 'O') if symbol == 'X' else minimax(board, 'X')
                board[i][j] = ' '

                if symbol == 'X' and score > best_score:
                    best_score = score
                    move = [i, j]
                elif symbol == 'O' and score < best_score:
                    best_score = score
                    move = [i, j]
    return move


def minimax(board, symbol):
    score = game_score(board)

    if score != None:
        return score

    if(symbol == 'X'):
        best_score = -float('inf')
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board,'O')
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board,'X')
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score






board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]

player_x = 'X'
player_o = 'O'

option = input("which you want to be ?\n1. X\n2. O\n")

while(True):

    if option == '1':
        print_board(board)
        player_turn(board, player_x)

        score = game_score(board)
        print_board(board)
        if score == 1:
            print("Player Won")
            break
        elif score == -1:
            print("AI Won")
            break
        elif score == 0:
            print("Tie")
            break

        ai_turn(board, player_o)

        score = game_score(board)
        print_board(board)
        if score == 1:
            print("AI Won")
            break
        elif score == -1:
            print("Player Won")
            break
        elif score == 0:
            print("Tie")
            break
        


    elif option == '2':
        ai_turn(board, player_x)

        score = game_score(board)
        print_board(board)
        if score == 1:
            print("Player Won")
            break
        elif score == -1:
            print("AI Won")
            break
        elif score == 0:
            print("Tie")
            break

        player_turn(board, player_o)

        score = game_score(board)
        print_board(board)
        if score == 1:
            print("Player Won")
            break
        elif score == -1:
            print("AI Won")
            break
        elif score == 0:
            print("Tie")
            break
    
    else:
        print("\nInvalid input\nTry again\n")
        option = input("which you want to be ?\n1.X\n2.O\n")