Here's a concise breakdown of its functionality:

1. Game Setup
Imports: Tkinter for GUI elements, random for selecting the starting player.
Initialization: The main Tkinter window is created, and two players (X and O) are defined.

2. GUI Elements
Label: Displays whose turn it is.
Reset Button: Allows starting a new game.
Grid of Buttons: A 3x3 grid for the Tic Tac Toe board, where each button corresponds to a cell on the board.

3. Game Functions
next_turn(row, column): Handles a player's move. It updates the button's text, checks for a winner or tie, and switches turns.
check_winner(): Checks rows, columns, and diagonals for a winning combination. Highlights the winning line in green or all cells in yellow if it's a tie.
empty_space(): Determines if there are any empty cells left on the board.
new_game(): Resets the board, chooses a random starting player, and updates the turn label.

4. Gameplay Flow
Players take turns clicking on the grid to place their symbols.
After each move, the game checks for a winner or a tie and updates the game state accordingly.
The game can be reset at any time to start a new round.
This setup creates an interactive Tic Tac Toe game with clear win/tie detection and a user-friendly interface.

Some Image of this game : 

![image](https://github.com/shahrierjaman/Tic-Tac-Toe/assets/157677455/b9784575-4656-4248-ae86-14422cd58c27)


![image](https://github.com/shahrierjaman/Tic-Tac-Toe/assets/157677455/1d7cf4de-cbc2-4cb0-8c7c-3f744cb513fe)


![image](https://github.com/shahrierjaman/Tic-Tac-Toe/assets/157677455/4f5a34f1-724b-4c39-bc7b-b47e7ecb9dec)


![image](https://github.com/shahrierjaman/Tic-Tac-Toe/assets/157677455/43d09c25-7f79-4909-8dde-6104054668b2)


