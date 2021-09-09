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

    while not (marker== "X" or marker=="O"):
        marker = input('Player 1: Do you want to be X or O?  ')
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