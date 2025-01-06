# Tic Tac Toe with Minimax Algorithm

This project is a Python implementation of the classic Tic Tac Toe game. The AI uses the Minimax algorithm to ensure optimal gameplay. Players can choose to play as 'X' or 'O' against the computer.

## Features
- **Interactive Gameplay**: The game lets the player pick their symbol ('X' or 'O') and takes turns against the AI.
- **Unbeatable AI**: The AI uses the Minimax algorithm to make decisions, ensuring it never loses.
- **Simple Interface**: The game board is displayed in the console, and the player makes moves using numerical inputs.

## How to Run
1. Make sure you have Python installed on your system.
2. Copy the code into a file named `tic_tac_toe.py`.
3. Run the script in a terminal or command prompt:

```bash
python tic_tac_toe.py
```

4. Follow the on-screen instructions to play the game.

## Game Rules
1. The player and the AI take turns to place their symbols ('X' or 'O') on the board.
2. The first to align three of their symbols horizontally, vertically, or diagonally wins.
3. If all positions are filled and no one wins, the game ends in a tie.

## Code Structure
### Functions
- **`print_board(board)`**: Displays the game board.
- **`player_turn(board, symbol)`**: Handles the player's move.
- **`valid_move(board, move)`**: Validates the player's move.
- **`place_the_move(board, move, symbol)`**: Places the move on the board.
- **`is_game_finish(board)`**: Checks if the game has ended in a tie.
- **`who_won(board, symbol)`**: Checks if a specific symbol has won.
- **`game_score(board)`**: Evaluates the board state and assigns a score.
- **`ai_turn(board, symbol)`**: Handles the AI's move.
- **`best_move(board, symbol)`**: Finds the optimal move for the AI.
- **`minimax(board, symbol)`**: Implements the Minimax algorithm to evaluate game states.

### Minimax Algorithm
- **Optimal Decision Making**: The algorithm simulates all possible moves and outcomes to choose the best move for the AI.
- **Scoring System**:
  - +1 for a win by 'X'
  - -1 for a win by 'O'
  - 0 for a tie

## Example Gameplay
```
Which symbol do you want to be?
1. X
2. O
1

 X| | 
 -+-+-
  | | 
 -+-+-
  | | 

Please pick your move between 1-9? 5

 X| | 
 -+-+-
  |X| 
 -+-+-
  | | 

AI's Turn:

 X| | 
 -+-+-
  |X|O
 -+-+-
  | | 
```

## Improvements and Extensions
- Add a GUI for a more user-friendly experience.
- Allow multiplayer mode.
- Implement additional difficulty levels for the AI.

## License
This project is open-source and free to use under the MIT License.