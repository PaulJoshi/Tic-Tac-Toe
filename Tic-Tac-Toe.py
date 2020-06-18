import os
import ai

board = {
    '7' : ' ', '8' : ' ', '9' : ' ',
    '4' : ' ', '5' : ' ', '6' : ' ',
    '1' : ' ', '2' : ' ', '3' : ' '}
seed = 1

def print_board():              #Function to print the board
    print(
         '\t\t' + board['7'] + '|' + board['8'] + '|' + board['9'] + '\n'
        +'\t\t' + '-+-+-' + '\n'
        +'\t\t' + board['4'] + '|' + board['5'] + '|' + board['6'] + '\n'
        +'\t\t' + '-+-+-' + '\n'
        +'\t\t' + board['1'] + '|' + board['2'] + '|' + board['3'] + '\n')

def clrscr():                   #Function to clear terminal viewport(Windows, Linux, MacOS compatible)
    os.system('cls||clear')

def user_play():                #Function to allow user to choose move
    while True:
        move = input("\tMake a move (1-9): ")
        try:
            if board[str(move)] == ' ':
                return move
            else: 
                print('\tInvalid move')
                continue
        except:
            print('\tInvalid move')
            continue

def tie_check(board):                   #Function to check if game is tied
    tie = False
    count = 0
    for key in board.keys():
        if board[key] == ' ':
            return False
        else:
            count += 1
    if count == 9:
        return True

def print_result(str,avatar):
    clrscr()
    print_board()
    print("\t      Game Over")
    if board[str] == avatar:
        print("    **** Congratz! You won! ****")
    else:
        print("\t **** You lost! ****")

def win_check(board,avatar):                #Function to check status of the game(win/lose/tie)
    if board['7'] == board['8'] == board['9'] != ' ':
        flag = 0
        print_result('7',avatar)              
        return flag
    
    elif board['4'] == board['5'] == board['6'] != ' ':
        flag = 0
        print_result('4',avatar)              
        return flag

    elif board['1'] == board['2'] == board['3'] != ' ':
        flag = 0
        print_result('1',avatar)                
        return flag
    
    elif board['1'] == board['4'] == board['7'] != ' ':
        flag = 0
        print_result('1',avatar)                
        return flag
    
    elif board['2'] == board['5'] == board['8'] != ' ':
        flag = 0
        print_result('2',avatar)              
        return flag
    
    elif board['3'] == board['6'] == board['9'] != ' ':
        flag = 0
        print_result('3',avatar)              
        return flag
    
    elif board['7'] == board['5'] == board['3'] != ' ':
        flag = 0
        print_result('7',avatar)                
        return flag
    
    elif board['1'] == board['5'] == board['9'] != ' ':
        flag = 0
        print_result('1',avatar)               
        return flag

    elif tie_check(board):
        flag = 0
        clrscr()
        print_board()
        print("\t      Game Over")
        print("\t**** It's a Tie! ****")
        return flag
    return 1
        
def game_engine():
    count = 0
    flag = 1
    while True:
        avatar = str(input('    Which avatar(X,O) would you like?\n\n\t\t  '))
        if avatar in ('x','X'):
            avatar = 'X'
            ai_avatar = 'O'
            break
        elif avatar in ('o','O','0'):
            avatar = 'O'
            ai_avatar = 'X'
            break
        else:
            print('Invalid avatar!')
            continue
    clrscr()
    print_board()
    while flag == 1:
        if seed == 1:           #(2*n)th game, n = 0,1,2,...  User gets first turn
            move = user_play()
            board[str(move)] = avatar
            count += 1
            if count >= 5 and win_check(board,avatar) == 0:
                break
            move = ai.ai_play(board,avatar)
            board[str(move)] = ai_avatar
            count += 1
            if count >= 5 and win_check(board,avatar) == 0:
                break
        elif seed == -1:            #((2*n) + 1)th game, n = 0,1,2,...  Program gets first turn
            move = ai.ai_play(board,avatar)
            board[str(move)] = ai_avatar
            count += 1
            clrscr()
            print_board()
            if count >= 5 and win_check(board,avatar) == 0:
                break
            move = user_play()
            board[str(move)] = avatar
            count += 1
            if count >= 5 and win_check(board,avatar) == 0:
                break
        clrscr()
        print_board()

def main():
    global seed
    play = True
    while play:
        clrscr()
        print('\tWelcome to Tic-Tac-Toe\n')
        print_board()
        game_engine()
        again=str(input("\n  Do you want to play again(y,n): "))
        if again in ('Y','y'):
            for key in board.keys():
                board[key] = ' '
            seed *= -1                  #So that user and program gets first turn alternatively in each game
            continue
        else:
            play = False

if __name__ == '__main__':
    main()