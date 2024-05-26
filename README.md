# 2048 Game

Welcome to the 2048 game! This README will guide you through the basics of the game, how to play it, and provide an overview of the AI algorithms implemented, including Expectiminimax and Monte Carlo Tree Search (MCTS).
This work was done for a AI class.

## Game Explanation

2048 is a single-player sliding tile puzzle game. The objective is to combine tiles with the same number to create a tile with the number 2048. The game is played on a 4x4 grid, with numbered tiles that can be slid up, down, left, or right. When two tiles with the same number touch, they merge into one.

The game starts with two tiles in random locations on the grid, each with a value of either 2 or 4. Players make moves by sliding tiles in one of the four directions. After each move, a new tile (either 2 or 4) is added to a random empty spot on the board. The game continues until no more moves are possible, either by reaching the 2048 tile or filling the grid without any possible merges.

## Game

To play the game, simply run the following command in your terminal: `python3 main.py`

## AI

The game also includes AI algorithms to solve and play the game for you. There are two main AI algorithms implemented:

1. **Expectiminimax Algorithm**
2. **Monte Carlo Tree Search (MCTS)**

You can run the AI using the Expectiminimax algorithm with the following command: `python3 minimax.py`

### Expectiminimax Algorithm

The Expectiminimax algorithm is a decision-making algorithm that extends the Minimax algorithm. It is used in game theory and decision-making under uncertainty. This algorithm is particularly useful for games like 2048, where there is an element of chance (the random appearance of new tiles) along with adversarial moves.

Expectiminimax considers both the maximizing player's moves and the expected values of random events. It evaluates the possible moves, generates the potential game states, and calculates the expected values for each state to make the optimal move.

### Monte Carlo Tree Search (MCTS)

Monte Carlo Tree Search is another algorithm used for decision-making in games. MCTS uses random sampling of the state space to simulate many possible game sequences and evaluate their outcomes. It builds a search tree incrementally and uses the results of these simulations to make decisions.

However, the current implementation of MCTS in this project is not fully optimized and may not perform as well as Expectiminimax. MCTS can still provide interesting insights and is worth exploring for further development and improvements.



