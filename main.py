# Build game board and valid character list
class Board:
    def __init__(self, player_x, player_o, curr_player="X"):
        self.board = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        self.valid_positions = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.curr_player = curr_player
        self.player_x_name = player_x
        self.player_o_name = player_o
        self.game_on = True
        self.winner = ''

    # Display board
    def show(self):
        for row in self.board:
            print(f"|{row[0]}|{row[1]}|{row[2]}|")

    # Update board with user input
    def update(self, selection):
        # remove selection from valid positions
        self.valid_positions.remove(selection)

        # place x or o on the board
        for row in self.board:
            if selection in row:
                i = row.index(selection)
                row[i] = self.curr_player

    # get user input
    def prompt_player(self):
        # get player name for prompt
        if self.curr_player == "X":
            player_name = self.player_x_name
        else:
            player_name = self.player_o_name

        # get user input
        data = input(f"{player_name}, select the box to place your mark. ").upper()

        # validate user input
        if data not in self.valid_positions or data == '':
            print("\n\nInvalid Input. Please select a valid location.\n")
            return None
        else:
            return data

    # flip players between turns
    def switch_player(self):
        if self.curr_player == "X":
            self.curr_player = "O"
        else:
            self.curr_player = "X"

    def check_for_win(self):
        # if all spaces are used end game
        if not self.valid_positions:
            self.game_on = False

        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                self.game_on = False
                self.winner = row[0]

        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                self.game_on = False
                self.winner = self.board[0][col]

        # check diag
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                self.board[0][2] == self.board[1][1] == self.board[2][0]):
            self.game_on = False
            self.winner = self.board[1][1]


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
        board.show()
        player_choice = board.prompt_player()

    board.update(player_choice)
    board.switch_player()
    board.check_for_win()

# end of game message
board.show()
if board.winner == "X":
    name = board.player_x_name
else:
    name = board.player_o_name

if board.winner:
    print(f"{board.winner}'s won!")
    print(f"Great job {name}!")
else:
    print("CATS! Try Again.")
