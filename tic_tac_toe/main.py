import numpy as np

game_board = np.array([
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
])

def call_game_board(player):
    for i in game_board:
        print((i[0] + str(' | '))+(i[1] + str(' | '))+(i[2]))
    print('----------')


def call_sample_board(player):
    sample_board = np.array([
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
        ])
    for i in sample_board:
        print((i[0] + str(' | '))+(i[1] + str(' | '))+(i[2]))
    print(f"Player {player}, Choose your position according to the positions displayed above: ")

def display_board():
    for i in game_board:
        print((i[0] + str(' | '))+(i[1] + str(' | '))+(i[2]))


def get_player_input(player):
    call_sample_board(player)
    move = int(input())
    if move == 1:
        if game_board[0,0] == ' ':
            game_board[0,0] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 2:
        if game_board[0,1] == ' ':
            game_board[0,1] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 3:
        if game_board[0,2] == ' ':
            game_board[0,2] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 4:
        if game_board[1,0] == ' ':
            game_board[1,0] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 5:
        if game_board[1,1] == ' ':
            game_board[1,1] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 6:
        if game_board[1,2] == ' ':
            game_board[1,2] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 7:
        if game_board[2,0] == ' ':
            game_board[2,0] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 8:
        if game_board[2,1] == ' ':
            game_board[2,1] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)
    elif move == 9:
        if game_board[2,2] == ' ':
            game_board[2,2] = f'{player}'            
        else:
            print('Place already taken')
        call_game_board(player)


def main(player):
    player = 'X'
    while True:
        if player == 'X':
            get_player_input('X')
            player = 'O'
        elif player == 'O':
            get_player_input('O')
            player = 'X'
main('X')

