import os
import random

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

def clrscr():                   #Function to clear terminal viewport
    os.system('cls||clear')

def ai_play(board,avatar):                  #Function to allow user to choose move
    if (board['7'] == board['8'] == avatar or board['3'] == board['6'] == avatar or board['1'] == board['5'] == avatar) and board['9'] == ' ':
        return 9
    elif (board['1'] == board['4'] == avatar or board['9'] == board['8'] == avatar or board['3'] == board['5'] == avatar) and board['7'] == ' ':
        return 7
    elif (board['3'] == board['2'] == avatar or board['7'] == board['4'] == avatar or board['9'] == board['5'] == avatar) and board['1'] == ' ':
        return 1
    elif (board['9'] == board['6'] == avatar or board['1'] == board['2'] == avatar or board['7'] == board['5'] == avatar) and board['3'] == ' ':
        return 3
    else:
        while True :
            move = random.randint(1,9)
            if board[str(move)] == ' ':
                return move
            else: continue

def user_play():                #Function to allow user to choose move
    while True:
        move = input("Make a move (1-9): ")
        try:
            if board[str(move)] == ' ':
                return move
            else: 
                print('Invalid move')
                continue
        except:
            print('Invalid move')
            continue

def win_check(board,avatar):
    if board['7'] == board['8'] == board['9'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['7'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['4'] == board['5'] == board['6'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['4'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag

    elif board['1'] == board['2'] == board['3'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['1'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['1'] == board['4'] == board['7'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['1'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['2'] == board['5'] == board['8'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['2'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['3'] == board['6'] == board['9'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['3'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['7'] == board['5'] == board['3'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['7'] == avatar:
            print(" **** You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    
    elif board['1'] == board['5'] == board['9'] != ' ':
        flag = 0
        clrscr()
        print_board()
        print("\nGame Over.\n")
        if board['1'] == avatar:
            print(" **** Congratz! You won! ****")
        else:
            print(" **** You lost! ****")                
        return flag
    return 1
        
def game_engine():
    count = 0
    flag = 1
    while True:
        avatar = input('Which avatar(X,O) would you like? ')
        if avatar == 'x' or 'X':
            avatar = 'X'
            ai_avatar = 'O'
            break
        elif avatar == 'o' or 'O':
            avatar = 'O'
            ai_avatar = 'X'
            break
        else:
            print('Invalid avatar!')
            continue
    clrscr()
    print_board()
    while flag == 1:
        if seed == 1:
            move = user_play()
            board[str(move)] = avatar
            count += 1
            if count >= 5:
                flag = win_check(board,avatar)
                if flag == 0:
                    break
            move = ai_play(board,avatar)
            board[str(move)] = ai_avatar
            count += 1
        elif seed == -1:
            move = ai_play(board,avatar)
            board[str(move)] = ai_avatar
            count += 1
            clrscr()
            print_board()
            if count >= 5:
                flag = win_check(board,avatar)
                if flag == 0:
                    break
            move = user_play()
            board[str(move)] = avatar
            count += 1
        clrscr()
        print_board()

def main():
    global seed
    play = True
    while play:
        clrscr()
        print('Welcome to Tic-Tac-Toe\n')
        print_board()
        game_engine()
        again=str(input("Do you want to play again(y,n): "))
        if again == 'n' or 'N':
            play = False

if __name__ == '__main__':
    main()