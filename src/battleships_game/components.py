"""
Components Module:

This module provides functions setting up the elements of the game Battleships.

    Modules:
        - random: Helps generate random numbers.
		- json: Handles JSON data.
		- logging: Allows us to log any errors.
		
    Functions:
        - initialise_board()
        - create_battleships()
        - place_battleships()
        - place()
        - can_place()
"""
import random
import json
import logging as log

# Format the logging messages
FORMAT = '%(levelname)s: %(asctime)s %(message)s'
log.basicConfig(format = FORMAT)

def initialise_board(size=10) -> list[list[str]]:
    """
    Initialises a square board with the specified size.
    
    Parameters:
        - size (int, default = 10): The size of the square game board.
        
    Returns:
        - board (2D array): The initialised board with None as the value for each element.
    """
    try:
        board = [[None] * size for row in range(size)]
        return board
    except ValueError:
        log.warning('Incorrect size value type')
        log.info('Using default value')
        return 10
def create_battleships(filename="battleships.txt") -> dict:
    """
    Creates a dictionary of battleships from a file.
    
    Parameters:
        - filename (str, default = "battleships.txt"): A file name.
          The file contains the name and size of the battleships.
          
    Returns:
        - battleships (dict): The battleship names are keys and sizes are values.
    """
    battleships = {}
    try:
        with open(filename, 'r', encoding='utf-8') as ship_file:
            for line in ship_file:
                ship_name, ship_size = line.strip().split(':')
                battleships[ship_name] = int(ship_size)
        return battleships
    except ValueError:
        log.warning('Invalid data in the file')
        log.info('Returning empty dictionary')
        return {}
    except FileNotFound:
        log.warning('This file cannot be found')
        log.info('Returning empty dictionary')
        return {}
def place_battleships(board, ships, strat="simple", filename="placement.json") -> list[list[str]]:
    """
    Places the battleships on the board depending on the placement strategy.
    
    Parameters:
    	
        - board (2D array): The board to place the battleships on.
        - ships (dict): The battleship names are keys and sizes are values.
        - strategy (str, default = "simple"): The strategy for placing battleships. 
          Options are "simple", "random", or "custom".
        - filename (str, default = "placement.json"): A file name.
          It is used for custom placements when placement_type is "custom".
          
    Returns:
        - board (2D array): The updated board with the battleships placed.
    """
    # The simple strategy places each battleship horizontal on a new row starting from (0,0)
    if strat == "simple":
        row_index = 0
        for ship_name, ship_size in ships.items():
            place(board, ship_name, ship_size, [0, row_index], 'h')
            row_index +=1
    # The random strategy places the battleships in random positions and orientations
    elif strat == "random":
        for ship_name, ship_size in ships.items():
            placed = False
            ship_range = len(board) - ship_size
            while not placed:
                direction = random.choice(['h', 'v'])
                column = random.randint(0, ship_range)
                row = random.randint(0, ship_range)
                placed = can_place(board, ship_size, column, row, direction)
            place(board, ship_name, ship_size, [column, row], direction)
    # The custom strategy allows the battleships to be placed according to a placement file
    elif strat == "custom":
        with open(filename, 'r', encoding='utf-8') as custom_file:
            location_data = json.load(custom_file)
            for ship_name, ship_info in location_data.items():
                column = int(ship_info[0])
                row = int(ship_info[1])
                direction = ship_info[2]
                if can_place(board, ships[ship_name], column, row, direction):
                    place(board, ship_name, ships[ship_name], [column, row], direction)
                else:
                    print("The custom placements overlap and therefore cannot be placed!")
    else:
        log.warning('No strategy was used to place ships')
    return board
    
def place(board, ship_name, ship_size, location, direction) -> None:
    """
    Places of a ship with a specified name, size, and orientation (horizontal
    or vertical) at a given position on the board.
    
    Parameters:
        - board (2D array): The board to place the battleships on.
        - ship_name (str): The name of the ship to be placed.
        - ship_size (int): The size of the ship.
        - column (int): The starting column index for the placement.
        - row (int): The starting row index for the placement.
        - direction (str): The orientation of the ship ('h' for horizontal, 'v' for vertical).
    """
    column, row = location
    for i in range(ship_size):
        if direction == 'h':
            board[row][i+column] = ship_name
        else:
            board[i+row][column] = ship_name
def can_place(board, ship_size, column, row, direction) -> bool:
    """
    Check if a ship of given size can be placed on a game board at the specified location.
    
    Parameters:
        - board (2D array): The board the battleships are on.
        - ship_size (int): The size of the ship to be placed.
        - column (int): The starting column index for the placement.
        - row (int): The starting row index for the placement.
        - direction (str): The orientation of the ship ('h' for horizontal, 'v' for vertical).
        
    Returns:
        - (bool): True if the ship can be placed without overlapping with existing ships.
                  False otherwise.
    """
    if direction == 'h':
        for i in range(column, column + ship_size):
            if board[row][i] is not None:
                return False
    else:
        for i in range(row, row + ship_size):
            if board[i][column] is not None:
                return False
    return True
