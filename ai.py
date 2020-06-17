import random

def ai_play(board,avatar):                  #Function to choose move
    if (board['5'] == ' '):
        return 5
    elif (board['7'] == board['8'] == avatar or board['3'] == board['6'] == avatar or board['1'] == board['5'] == avatar) and board['9'] == ' ':
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