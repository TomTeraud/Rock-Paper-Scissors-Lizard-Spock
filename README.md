## Rock Paper Scissors Lizard Spock Game

This game is an implementation of the popular game "Rock Paper Scissors Lizard Spock" with additional computer players. The game allows you to play against computer players and compete for the highest number of wins.

### Files:

1. **main.py**: The main file that runs the game. It handles user input, creates player objects, plays rounds, and determines the winner at the end.
2. **custom_functions.py**: Contains custom functions used in the game, such as getting the number of computer players, the number of rounds, the player's name, and user input validation.
3. **custom_classes.py**: Defines the `Player` class that represents a player in the game. It has attributes for the player's name, points, and the selected move (rock, paper, scissors, lizard, or spock).

### How to Play:

1. Run the `main.py` file to start the game.
2. Enter the number of computer players (1-9), the number of rounds (1-5), and your player name when prompted.
3. The game will generate computer player names based on the number of computer players entered.
4. Each round, you will be asked to select your move (rock, paper, scissors, lizard, or spock).
5. The game will simulate each player's moves and determine the winner of each round based on the game rules.
6. The points for each player will be updated according to the results of each round.
7. At the end of all rounds, the game will display the final scores and declare the overall winner.

### Customization:

- You can customize the options available for moves by modifying the `options` tuple in `main.py`.
- The names for computer players can be customized by adding or modifying names in the `computer_names` tuple in `main.py`.
- The game rules can be adjusted by modifying the `rules` dictionary in `custom_functions.py`.