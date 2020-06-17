import random

def ai_play(board):                  #Function to choose move
    if (board['5'] == ' '):
        return 5
    elif (board['7'] == board['8'] != ' ' or board['3'] == board['6'] != ' ' or board['1'] == board['5'] != ' ') and board['9'] == ' ':
        return 9
    elif (board['1'] == board['4'] != ' ' or board['9'] == board['8'] != ' ' or board['3'] == board['5'] != ' ') and board['7'] == ' ':
        return 7
    elif (board['3'] == board['2'] != ' ' or board['7'] == board['4'] != ' ' or board['9'] == board['5'] != ' ') and board['1'] == ' ':
        return 1
    elif (board['9'] == board['6'] != ' ' or board['1'] == board['2'] != ' ' or board['7'] == board['5'] != ' ') and board['3'] == ' ':
        return 3
    elif (board['1'] == board['3'] != ' ' or board['8'] == board['5'] != ' ') and board['2'] == ' ':
        return 2
    elif (board['3'] == board['9'] != ' ' or board['4'] == board['5'] != ' ') and board['6'] == ' ':
        return 6
    elif (board['9'] == board['7'] != ' ' or board['2'] == board['5'] != ' ') and board['8'] == ' ':
        return 8
    elif (board['7'] == board['1'] != ' ' or board['6'] == board['5'] != ' ') and board['4'] == ' ':
        return 4
    else:
        while True :
            move = random.randint(1,9)
            if board[str(move)] == ' ':
                return move
            else: continue