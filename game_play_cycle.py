# Pokemon Trading Card Game Play Cycle

# Import necessary modules
import random

# Define the game_play function

def game_play():
    # Initialize the game
    print('Welcome to the Pokemon Trading Card Game!')
    while True:
        try:
            player1 = input('Player 1, please enter your name: ')
            player2 = input('Player 2, please enter your name: ')
            break
        except EOFError:
            print('Please enter a name.')
    coin_flip = random.randint(1, 2)
    if coin_flip == 1:
        active_player = player1
        print(player1 + ' goes first!')
    else:
        active_player = player2
        print(player2 + ' goes first!')
    # Start the game
    while True:
        # Draw a card
        print(active_player + ', draw a card.')
        # Check for win condition
        if win_condition():
            print(active_player + ' wins!')
            break
        # Switch active player
        if active_player == player1:
            active_player = player2
        else:
            active_player = player1

# Define the win_condition function

def win_condition():
    # Check for win condition
    return False

# Call the game_play function

game_play()
