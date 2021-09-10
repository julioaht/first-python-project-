# crear terminal def... not working
# def clear():
#    os.system( 'cls' )


#creating board for display

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# small test to check if board is working 


test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

# clear()

# getting the players marker Preference

def player_input():
    marker=""

# the output = (player1 marker, Player2 marker)
    while not (marker== "X" or marker=="O"):
        marker = input('Player 1: Do you want to be X or O?  ').upper()
    if marker == "X":
        return ('X','O')
    else:
        return('O','X')  


# checking players input
# player_input()              



#get board, marker, position. and assign to board

def place_marker(board, marker, position):
    board[position] = marker


    # test to check if place_marker() is working. test passed
    # place_marker(test_board,'$',8)

    #display_board(test_board)

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


win_check(test_board,'X')

