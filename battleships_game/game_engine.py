"""
Game Engine Module:

This module runs a game where the player tries to sink battleships on a pre-set board.

	Modules:
		- components: Creates the ships and board, placing the ships on the board.
		- logging: Allows us to log any errors.
		
    Functions:
    	- attack()
    	- cli_coordinates_input()
    	- simple_game_loop()
    
    It also uses functions from the components module.
"""

import logging as log
import components as comp

# Format the logging messages
FORMAT = '%(levelname)s: %(asctime)s %(message)s'
log.basicConfig(format = FORMAT)

def attack(coordinates: tuple, board, ships) -> bool:
    """
    Processes an attack on the board at the coordinates to see if it hit the ship.

    Parameters:
    	- coordinates (tuple): A tuple representing the (column, row) coordinates on the board.
    	- board (2D array): The board with the ships on it.
    	- ships (dict): The battleship names are keys and sizes are values.

    Returns:
    	- (bool): True if a ship was hit.
              	  False otherwise.
              	  
    It also sets that element to None and decreases the size value of the ship.
    """
    column = int(coordinates[0])
    row = int(coordinates[1])
    try:
        for ship_name in ships.keys():
            if board[row][column] == ship_name:
                board[row][column] = None
                # Decrements the ship's size value
                ships[ship_name] -= 1
                return True
    except IndexError:
        log.warning('Row and/or column is out of the bounds of the board')
    return False
def cli_coordinates_input() -> tuple:
    """
    Take a user input for the column and row until they enter two integer values.
    
    Returns:
    	- (tuple): The column value as the x_coord and the row value as y_coord.
    """
    while True:
        try:
            x_coord = int(input("Enter the column number: "))
            y_coord = int(input("Enter the row number: "))
            if 0 <= x_coord <= 9 and 0 <= y_coord <= 9:
                return (x_coord, y_coord)
            log.warning("Please enter two integer values from 0 to 9 inclusive.\n")
        except ValueError:
            log.warning("Please enter two integer values.\n")
def simple_game_loop() -> None:
    """
    Simulates a game where the player tries to sink battleships on a pre-set board.
    If they hit a ship then a Hit message is printed. 
    If they miss a ship then a Miss message is printed.
    Once all the ships have been sunk Game Over is printed.

    Functions:
    	- comp.initialise_board(): Initialises the game board.
    	- comp.create_battleships(): Creates battleships for the game.
    	- comp.place_battleships(board, ships): Places battleships on the board.
    	- cli_coordinates_input(): Takes user input for attack coordinates.
    	- attack(coords, board, ships): Executes an attack on the specified coordinates.
    """
    print("\nWelcome to the Simple Game Loop\n")
    board = comp.initialise_board()
    ships = comp.create_battleships()
    comp.place_battleships(board, ships)
    # Runs the while loop until all ships have a size value of 0
    while not all(value == 0 for value in ships.values()):
        coords = cli_coordinates_input()
        if attack(coords, board, ships):
            print("\nHit\n")
        else:
            print("\nMiss\n")
    print("Game Over\n")

if __name__ == "__main__":
    simple_game_loop()
