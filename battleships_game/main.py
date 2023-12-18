"""
Main Module

This module provides the web interface for a user to play against the computer.

	Modules:
		- json: Handles JSON data.
		- Flask: Web framework that is written in Python.
		- components: Creates the ships and board, placing the ships on the board.
		- game_engine: Has functions that take coordinates for a move and process an attack.
		- mp_game_engine: Has the function to generate a random attack coordinate.
		- logging: Allows us to log any errors.
	
	Routes:
		- /placement: Handles ship placement.
		- /: Handles the main interface with the players two boards.
		- /attack: Handles the attacka on the opponent.

	Functions:
		- placement()
		- main()
		- process_attack()
"""

import json
import logging as log
from flask import Flask, render_template, request, jsonify
import components as comp
import game_engine as gm
import mp_game_engine as mp_gm

# Format the logging messages
FORMAT = '%(levelname)s: %(asctime)s %(message)s'
log.basicConfig(format = FORMAT)

app = Flask(__name__, template_folder='templates')
empty_board = comp.initialise_board()
player_ships = comp.create_battleships()
player_board = [[]]
ai_empty = comp.initialise_board()
ai_ships = comp.create_battleships()
ai_board = comp.place_battleships(ai_empty, ai_ships, "random")

@app.route('/placement', methods=['GET', 'POST'])
def placement():
    """
    Handles the ship placement on the player's board.

    GET Method:
    Renders the 'placement.html' template with the player board size and ship information.

    POST Method:
    Places the battleships on the board from the information in 'placement.html'.

    Returns:
    	- For GET request (html): 'placement.html'.
		- For POST request: A JSON response with a 'message' as 'Received' and 200.
    """
    global player_board
    if request.method == 'GET':
        return render_template('placement.html', ships=player_ships, board_size=len(empty_board))
    data = request.get_json()
    location_data = "placement.json"
    with open(location_data, "w", encoding = 'utf-8') as place_file:
        json.dump(data, place_file)
    player_board = comp.place_battleships(empty_board, player_ships, "custom", location_data)
    return jsonify({'message': 'Received'}), 200
@app.route('/')
def main():
    """
    Creates the main interface, so long as the player's board has been created.

    Returns:
    	IF placement has happened then
    	- (str): "Player board not placed. Please go to /placement first."
    	ELSE 
    	- template (html): 'main.html' is returned.
    """
    if player_board == [[]]:
        return "Player board not placed. Please go to /placement first."
    return render_template('main.html', player_board=player_board)
@app.route('/attack', methods=['GET'])
def process_attack():
    """
    Handles attacks and returns the game information.

    Returns:
    	- response (json): The attack and the AI's turn.
    					   If the game is over, the response has a game over message.
    """
    # Get the players selected coordinates and do an attack
    x_coord = request.args.get('x')
    y_coord = request.args.get('y')
    player_move = (x_coord, y_coord)
    player_turn = gm.attack(player_move, ai_board, ai_ships)
    # Generate an AI attack
    ai_move = mp_gm.generate_attack(player_board)
    gm.attack(ai_move, player_board, player_ships)
    # Sees if the game is over or not by checking if either players ships all have a size value of 0
    game_over = False
    winner = ""
    if all(value == 0 for value in player_ships.values()):
        winner = "AI"
        game_over = True
    elif all(value == 0 for value in ai_ships.values()):
        winner = "Player"
        game_over = True
    if not game_over:
        return jsonify({'hit': player_turn, 'AI_Turn': ai_move})
    return jsonify({'hit': player_turn, 'AI_Turn': ai_move, 'finished': f'{winner} Wins!'})

if __name__ == '__main__':
    app.run(debug=True)
