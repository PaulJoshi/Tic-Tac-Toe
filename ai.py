
def ai_play(board,avatar):                  #Function to choose move
    if avatar == 'X':
        ai_avatar = 'O'
    else:
        ai_avatar = 'X'
    #if (board['5'] == ' '):
    #    return 5
    if (board['7'] == board['8'] == ai_avatar or board['3'] == board['6'] == ai_avatar or board['1'] == board['5'] == ai_avatar) and board['9'] == ' ':
        return 9
    elif (board['1'] == board['4'] == ai_avatar or board['9'] == board['8'] == ai_avatar or board['3'] == board['5'] == ai_avatar) and board['7'] == ' ':
        return 7
    elif (board['3'] == board['2'] == ai_avatar or board['7'] == board['4'] == ai_avatar or board['9'] == board['5'] == ai_avatar) and board['1'] == ' ':
        return 1
    elif (board['9'] == board['6'] == ai_avatar or board['1'] == board['2'] == ai_avatar or board['7'] == board['5'] == ai_avatar) and board['3'] == ' ':
        return 3
    elif (board['1'] == board['3'] == ai_avatar or board['8'] == board['5'] == ai_avatar) and board['2'] == ' ':
        return 2
    elif (board['3'] == board['9'] == ai_avatar or board['4'] == board['5'] == ai_avatar) and board['6'] == ' ':
        return 6
    elif (board['9'] == board['7'] == ai_avatar or board['2'] == board['5'] == ai_avatar) and board['8'] == ' ':
        return 8
    elif (board['7'] == board['1'] == ai_avatar or board['6'] == board['5'] == ai_avatar) and board['4'] == ' ':
        return 4
    elif (board['7'] == board['8'] == avatar or board['3'] == board['6'] == avatar or board['1'] == board['5'] == avatar) and board['9'] == ' ':
        return 9
    elif (board['1'] == board['4'] == avatar or board['9'] == board['8'] == avatar or board['3'] == board['5'] == avatar) and board['7'] == ' ':
        return 7
    elif (board['3'] == board['2'] == avatar or board['7'] == board['4'] == avatar or board['9'] == board['5'] == avatar) and board['1'] == ' ':
        return 1
    elif (board['9'] == board['6'] == avatar or board['1'] == board['2'] == avatar or board['7'] == board['5'] == avatar) and board['3'] == ' ':
        return 3
    elif (board['1'] == board['3'] == avatar or board['8'] == board['5'] == avatar) and board['2'] == ' ':
        return 2
    elif (board['3'] == board['9'] == avatar or board['4'] == board['5'] == avatar) and board['6'] == ' ':
        return 6
    elif (board['9'] == board['7'] == avatar or board['2'] == board['5'] == avatar) and board['8'] == ' ':
        return 8
    elif (board['7'] == board['1'] == avatar or board['6'] == board['5'] == avatar) and board['4'] == ' ':
        return 4
    else:
        import random
        while True :
            move = random.randint(1,9)
            if board[str(move)] == ' ':
                return move
            else: continue