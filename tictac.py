def display_board(board):
    print('\n'*100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[7] + '|' + board[8] + '|' + board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


def player_input():
    marker: ''
    #Keep asking player 1 to be x or o
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ")
    #assign player 2 opposite marker
    if player1 == 'X':
        player2 =='O'
    else:
        player2 == "X"
    
    return (player1,player2)

player1_marker,player2_marker = player_input()