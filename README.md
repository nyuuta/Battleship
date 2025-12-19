Battleship Game (Simplified)
This is a simplified version of the classic Battleship game.

How to Run


Install dependencies:


pip install -r requirements.txt



Run the game:


python main.py

How It Works


Player input: enter coordinates x y (1–10) for each move.


Bot moves: chooses cells randomly.


Ships configuration:


1 ship of size 4


2 ships of size 3


3 ships of size 2


4 ships of size 1




Ships cannot touch each other, even diagonally.


Display


X — hit


o — miss


. — unknown/empty cell


When a ship is destroyed, the game prints its size. The game ends when all ships of one side are destroyed.

Files


main.py — entry point


data/player_ships.csv — player ship positions


data/bot_ships.csv — bot ship positions


data/game_state.csv — log of moves


src/ — contains the game logic modules
