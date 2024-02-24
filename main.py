from board import Board

# Get Player's Names
playerX = input("Player X, what is your name?\n")
playerO = input("Player O, what is your name?\n")

# initialize the game board
board = Board(player_x=playerX, player_o=playerO)

# Play the game
while board.game_on:

    player_choice = None

    # continue once the player has input a valid square
    while player_choice is None:
        board.draw()
        player_choice = board.prompt_player()

    board.update(player_choice)
    board.switch_player()
    board.check_for_win()

# end of game message
board.end()
