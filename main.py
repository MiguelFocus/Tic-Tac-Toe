board = {
    1: '  ', 2: '  ', 3: '  ',
    4: '  ', 5: '  ', 6: '  ',
    7: '  ', 8: '  ', 9: '  '
}

print(f"{board[1]}|{board[2]}|{board[3]}")
print('--+--+--')
print(f"{board[4]}|{board[5]}|{board[6]}")
print('--+--+--')
print(f"{board[7]}|{board[8]}|{board[9]}")


def create_board(choice, player):
    """Draws the player on the board"""
    global board
    try:
        if type(choice) == int:
            board[choice] = f"{player}"

            print(f"{board[1]}|{board[2]}|{board[3]}")
            print('--+--+--')
            print(f"{board[4]}|{board[5]}|{board[6]}")
            print('--+--+--')
            print(f"{board[7]}|{board[8]}|{board[9]}")

    except ValueError:
        print("Introduce un numero del 1 al 9")


def play(turn):
    """Checks which player is playing"""
    choice = ""
    if turn % 2 == 0:
        player = ' X'

    else:
        player = ' 0'
    try:
        choice = input(f"Turno de {player}. Elige en que casilla pintar. Casillas enumeradas de 1-9, en orden -->")
        return int(choice), player

    except ValueError:
        print(f"{choice} no es valido. Introduce un numero del 1 al 9.")

    return choice, player


game_on = True
game_turn = 0

while game_on:

    game_choice, game_player = play(game_turn)
    create_board(game_choice, game_player)

    if board[1] == board[2] == board[3] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[4] == board[5] == board[6] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[7] == board[8] == board[9] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[1] == board[4] == board[7] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[2] == board[5] == board[8] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[3] == board[6] == board[9] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[1] == board[5] == board[9] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    elif board[3] == board[5] == board[7] == game_player:
        game_on = False
        print(f"{game_player} Ganador!")

    if type(game_choice) == int:
        game_turn += 1