"""
Multiplayer Game Engine Module:

This module runs a game where there are two players: one user and one AI player.
They take turns trying to be the first to sink each others ships.

	Modules:
		- random: Helps generate random numbers.
		- components: Creates the ships and board, placing the ships on the board.
		- game_engine: Has functions that take coordinates for a move and process an attack.
		- logging: Allows us to log any errors.
		
    Functions:
    	- initialise_player():
    	- initialise_ascii_board():
    	- turn():
    	- generate_attack():
    	- ascii_move_board():
    
    It also uses functions from the components module and the game_engine module.
"""

import random
import components as comp
import game_engine as gm
import logging as log

# Format the logging messages
FORMAT = '%(levelname)s: %(asctime)s %(message)s'
log.basicConfig(format = FORMAT)

players = {}
ai_generated_moves = [[]]

def generate_attack(board) -> tuple:
    """
    Generates random coordinates to attack on the board. 
    It also makes sure it is not a move that has been used before.

    Parameters:
    	- board (2D array): A board of a given size.

    Returns:
    	- (tuple): The column value as the x_coord and the row value as y_coord.
    """
    new_move = False
    board_size = len(board)
    while not new_move:
        x_coord = random.randrange(board_size)
        y_coord = random.randrange(board_size)
        coords = [x_coord, y_coord]
        if coords not in ai_generated_moves:
            new_move = True
        ai_generated_moves.append(coords)
    return (x_coord, y_coord)
def initialise_player(name, settings) -> tuple:
    """
    Initialise a player for the game.

    Parameters:
    	- name (str): The name of the player.
    	- settings (str): The name of the strategy for placing battleships. 
          
    Returns:
    	- (tuple): A tuple containing the player's board and ships.
    """
    players[name] = (comp.initialise_board(), comp.create_battleships())
    player_board, player_ships = players[name]
    comp.place_battleships(player_board, player_ships, settings)
    return player_board, player_ships
def initialise_ascii_board(board) -> list[list[str]]:
    """
    Initialises an ASCII art board based on the battleships board.

    Parameters:
    	- board (2D array): The board the battleships are on.

    Returns:
    	- ascii_art_board (2D array): An ASCII art representation of the board.
    	 			  				  None values are represented by '~'.
    	 			  				  Battleships are represented by 'B'.
    """
    ascii_art_board = []
    row_number = 0
    for board_row in board:
        # Creates an empty row to add characters into
        ascii_art_board.append([])
        for item in board_row:
            if item is None:
                ascii_art_board[row_number].append('~')
            else:
                ascii_art_board[row_number].append('B')
        row_number += 1
    return ascii_art_board
def ascii_move_board(ascii_board, move) -> list[list[str]]:
    """
    Changes the ASCII art board based on the move.

    Parameters:
    	- ascii_board (2D array): The ascii art board of the battleships board.
    	- move (tuple): The column and the row of the selected move.

    Returns:
    	- ascii_board (2D array): The ascii art board of the battleships board.
    							  If the move was a Hit that move element changes to 'X'.
    							  If the move was a Miss that move element changes to 'X'.
    """
    column, row = move
    if ascii_board[row][column] == 'B':
        ascii_board[row][column] = 'X'
    else:
        ascii_board[row][column] = 'O'
    return ascii_board
def turn(coords, board, ships) -> None:
    """
    Performs a turn in the game and depending on the outcome prints hit or miss.

    Parameters:
    	- coords (tuple): The coordinates for the attack.
    	- board (list): The board with the current state of the game.
    	- ships (dict): The battleship names are keys and current sizes are values.
    """
    if gm.attack(coords, board, ships):
        print("\nHit\n")
    else:
        print("\nMiss\n")
def ai_opponent_game_loop() -> None:
    """
    Run a game loop for a multiplayer game against an AI opponent.
    A player and an AI player are created.
    The player gets an ascii art board to graphical represent their board.
    The players take turn at using coordinates to attack.
    Once all the ships have been sunk Game Over is printed.
    
    Functions:
    	- initialise_player(): Initialises the players.
    	- initialise_ascii_board(): Initialises the ascii board.
    	- gm.cli_coordinates_input(): Takes user input for attack coordinates.
    	- turn(): Allows each player to take a turn.
    	- generate_attack(): Creates random coordinates for an attack.
    	- ascii_move_board(): Updates the ascii board with the move.
    """
    print("\nWelcome to the Multiplayer Game")
    # Create User
    user_board, user_ships = initialise_player('User', 'custom')
    user_ascii_board = initialise_ascii_board(user_board)
    # Create AI
    ai_board, ai_ships = initialise_player('AI', 'random')
    # Runs the while loop until either players ships all have a size value of 0
    while (
        not all(value == 0 for value in user_ships.values()) and
        not all(value == 0 for value in ai_ships.values())
    ):
        print("\nUser Move\n")
        user_coords = gm.cli_coordinates_input()
        turn(user_coords, ai_board, ai_ships)
        print("AI Move")
        ai_coords = generate_attack(user_board)
        turn(ai_coords, user_board, user_ships)
        # Display the ASCII art board row by row
        for row in ascii_move_board(user_ascii_board, ai_coords):
            print(row)
    if all(value == 0 for value in user_ships.values()):
        print("Game Over, AI wins")
    else:
        print("Game Over, Player wins")

if __name__ == "__main__":
    ai_opponent_game_loop()
