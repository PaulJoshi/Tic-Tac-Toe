def print_board() { #Function to print the board
    board = {
        '7' : ' ', '8' : ' ', '9' : ' ',
        '4' : ' ', '5' : ' ', '6' : ' ',
        '1' : ' ', '2' : ' ', '3' : ' '}
    print(
        board['7']+'|'+board['8']+'|'+board['9']+'\n'
        +'-+-+-'+'\n'+
        board['4']+'|'+board['5']+'|'+board['6']+'\n'
        +'-+-+-'+'\n'+
        board['1']+'|'+board['2']+'|'+board['3'])
}