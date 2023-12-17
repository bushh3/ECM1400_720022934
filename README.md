# ECM1400-720022934

## Introduction
This package allows a user to play battleships through modular implementation. It has four main modules that do the following:
### Components
This module sets up the fundamental elements of the game, including functions for creating the game board, creating the battleships, and placing them on the board. 
### Game Engine
This module runs a single-player game where the player attempts to sink battleships on a pre-set board. 
It includes functions for processing attacks, taking user input for coordinates, and playing the game until all ships are sunk.
### Multiplayer Game Engine
This module creates multiplayer functionality against an AI opponent. 
The functions allow the AI to generate random attacks, and players take turns to try to sink each other's ships. 
### Main
The main module provides a web interface using Flask, allowing users to play against the AI. 

## Prerequisites
Before you get started, ensure you have the following prerequisites installed:
- [Python](https://www.python.org/downloads/release/python-3918/) (version 3 or more but no higher than 3.9)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) (version 1.0 or higher)

## Installation
To install the `ECM1400_720022934` package on your device, follow these steps:
1. **Download the Zip File:**
   
   Download the `ECM1400_720022934` file to your local machine.
2. **Open your Terminal or Command Line:**
   
   Open a terminal or command line on your device.
3. **Navigate to the Directory:**
   
   Change your current directory to the location where the `ECM1400_720022934` file is located. Use the `cd` command to navigate.
   
   ```bash
   cd /ECM1400_720022934/src
   ```
4. **Install the Package:**
   
   Use the `pip` command to install.
   ```bash
   pip install battleships_game
   ```

## Getting Started Tutorial
There are three possible game modes you could play. They are the `The Single Player Game`, `The Multiplayer Command Line Game`, or `The Multiplayer Web Game`.
### The Single Player Game
1. **Open your Terminal or Command Line:**
   
   Open a terminal or command line on your device.
2. **Navigate to the Directory:**
   
   Change your current directory to the location where the battleships can be run from. Use the `cd` command to navigate.
   
   ```bash
   cd /ECM1400_720022934/src/battleships_game
   ```
3. **Run the Game_Engine Module:**

   Use this command to run the code in the terminal.
   ```bash
   python game_engine.py
   ```
4. **Take Your Turn:**

   To play the game input one coordinate at a time with a range of 0-9 inclusive.
   
   You will either hit or miss the ship. 

   `Example`

   ```bash
      Welcome to the Simple Game Loop

      Enter the column number: 1
      Enter the row number: 2

      Hit      
   ```
5. **End of Game:** 

   The game will end when all the ships have been sunk.
### The Multiplayer Command Line Game
1. **Open your Terminal or Command Line:**
   
   Open a terminal or command line on your device.
2. **Navigate to the Directory:**
   
   Change your current directory to the location where the battleships can be run from. Use the `cd` command to navigate.
   
   ```bash
   cd /ECM1400_720022934/src/battleships_game
   ```
3. **Run the Game_Engine Module:**

   Use this command to run the code in the terminal.
   ```bash
   python mp_game_engine.py
   ```
4. **Take Your Turn:**

   To play the game input one coordinate at a time with a range of 0-9 inclusive. 
   
   You will either hit or miss the ship. 
   
   `Example`

   ```bash
      Welcome to the Multiplayer Game

      User Move

      Enter the column number: 1
      Enter the row number: 2

      Miss
   ```
5. **AI Turn:**

   The AI then has a turn. It will output the result of the turn and an ascii art board of your board.

   These are the following symbols that will be used:

   - 'B' is a battleship
   - '~' is an empty square
   - 'X' is a hit
   - '0' is a miss
   
   `Example`

   ```bash
      AI Move

      Miss

      ['B', 'B', 'B', 'B', 'B', '~', '~', '~', '~', '~']
      ['B', 'B', 'B', 'B', '~', '~', '~', '~', '~', '~']
      ['B', 'B', 'B', '~', '~', '~', '~', '~', '~', '~']
      ['B', 'B', 'B', '~', '~', '~', '~', '~', '~', '~']
      ['B', 'B', '~', '~', '~', '~', '~', 'O', '~', '~']
      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
      ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
   ```
5. **End of Game:** 

   The game will end when all the ships have been sunk and a message will be displayed to tell you who the winner was.

### The Multiplayer Web Game

1. **Open your Terminal or Command Line:**
   
   Open a terminal or command line on your device.
2. **Navigate to the Directory:**
   
   Change your current directory to the location where the battleships can be run from. Use the `cd` command to navigate.
   
   ```bash
   cd /ECM1400_720022934/src/battleships_game
   ```
3. **Run the Game_Engine Module:**

   Use this command to run the code in the terminal.
   ```bash
   python main.py
   ```
   You will get the following result:
   ```bash
   * Serving Flask app 'main'
   * Debug mode: on
   INFO: 2023-12-17 20:08:27,680 WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on http://127.0.0.1:5000
   INFO: 2023-12-17 20:08:27,680 Press CTRL+C to quit
   INFO: 2023-12-17 20:08:27,696  * Restarting with watchdog (fsevents)
   WARNING: 2023-12-17 20:08:27,781  * Debugger is active!
   INFO: 2023-12-17 20:08:27,788  * Debugger PIN: 987-161-162
   ```
4. **Go to the Web Page:**
   
   To run go to http://127.0.0.1:5000/placement

   **YOU MUST KEEP THE TERMINAL OPEN**

5. **Place Your Ships:**

   Once you have navigated to the webpage, hover your mouse over the board. You should see some of the squares highlighted green like this:

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.35.48.png>)
   
   Move your mouse around until you are happy with the placement of your ship. When you are click your mouse.

   Then begin to move your mouse again to place the next ship.

   You will notice that the ship you have placed is now grey and if the new ship is hovering over an existing ship or out of bounds of the board it will be red like this:

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.39.29.png>)

   If you would like to rotate a ship press r like this:

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.40.45.png>)

   Do this until all the ships are placed i.e. there are no more green squares appearing when you hover over the board.

   Then press Send Game. 
   
   Click OK on the message that appear at the top of your screen.

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 21.08.17.png>)

6. **Make Moves:**

   Once you have pressed game you will see the following webpage:

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.43.31.png>)

   To make a move press on any square on the white board. Red means you have hit a battleship and blue is a miss.

   The AI will then take its turn and you will see this on the Players Grid (your battleships). This move is noted in the Game Log.

   `Example`

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.45.05.png>)

   Now keep making moves until one player has sunk all the battleships.

   A message will be shown when the game is over showing who wins.

   `Example`

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.47.56.png>)

   Once you click OK the final game state will be shown.

   ![Alt text](<README_photos/Screenshot 2023-12-17 at 20.48.15.png>)

## Testing
Explain how users can run tests for your project. Include any testing frameworks or tools used.

## Developer Documentation
For developers contributing to your project, provide information about the code structure, guidelines, and any additional tools they might need.

## Details

- **Author:** Henry James Hardy Bush
- **License:** MIT
- **Source:** [Project Repository](https://github.com/your-username/your-project)