import os
import random

board = {
    '7' : ' ', '8' : ' ', '9' : ' ',
    '4' : ' ', '5' : ' ', '6' : ' ',
    '1' : ' ', '2' : ' ', '3' : ' '}

def print_board():              #Function to print the board
    print(
         '\t\t' + board['7'] + '|' + board['8'] + '|' + board['9'] + '\n'
        +'\t\t' + '-+-+-' + '\n'
        +'\t\t' + board['4'] + '|' + board['5'] + '|' + board['6'] + '\n'
        +'\t\t' + '-+-+-' + '\n'
        +'\t\t' + board['1'] + '|' + board['2'] + '|' + board['3'])

def clrscr():                   #Function to clear terminal viewport
    os.system('cls||clear')

def ai_play():                  #Function to allow user to choose move
    while(True):
        move = random.randint(1,9)
        if board[str(move)] == ' ':
            return move
        else: continue

def user_play():                #Function to allow user to choose move
    while(True):
        move = input("Make a move (1-9)")
        if board[str(move)] == ' ':
            return move
        else: 
            print('Move already made')
            continue


clrscr()
print_board()
x = ai_play()
print(x)
