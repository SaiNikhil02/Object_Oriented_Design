Design Connect Four
Background
Connect Four is a popular game played on a 7x6 grid. Two players take turns dropping colored discs into the grid. The first player to get four discs in a row (vertically, horizontally or diagonally) wins.

Requirements
Some possible questions to ask:

What are the rules of the game?
What size is the grid?
How many players are there? Player vs Computer? Player vs Player?
Are we keeping track of the score?
Basics
The game will be played by only two players, player vs player
The game board should be of variable dimensions
The target is to connect N discs in a row (vertically, horizontally or diagonally)
N is a variable (e.g. connect 4, 5, 6, etc)
There should be a score tracking system
After a player reaches the target score, they are the winner

Design
High-level
We will need a Grid class to maintain the state of the 2-D board
The board cell can be empty, yellow (occupied by Player 1) or red (occupied by Player 2)
The grid will also be responsible for checking for a win condition
We can have a Player class to represent the player's piece color
This isn't super important, but encapsulating information is generally a good practice
The Game class will be composed of the Grid and Players
The Game class will be responsible for the game loop and keeping track of the score

Code
We will use an enum to represent the GridPosition.

The Grid will maintain the state of the board and all of the pieces. It will also check for a win condition. Perhaps it would be more appropriate to name the checkWin method to checkNConnected, since the Grid itself shouldn't need to know what the rules of the game are.

A Player is only meant to encapsulate the player's information, more importantly the player's piece color.

The Game class will be used to play the game. It will keep track of the players, the score, and the grid. It will also be responsible for the game loop. The game parameters passed in via the constructor give us flexibility to play the game with slightly different rules and dimensions.
While we could instantiate the board within the Game class, it's preferred to pass it in via the constructor. This means the Game class does not need to know how to instantiate the board.
Even though we are only playing with two players, we can still use a list to store the players. This is not necessary, but it's easy enough and gives us flexibility to add more players in the future.

Finally, we can create the grid, set the game parameters, and play the game.

# Connect 4

## Description
This is an implementation of Connect 4 using Object-Oriented Design in Python.

## Features
- Player vs Player Mode
- Board representation using a 2D list
- Turn-based gameplay logic

## Classes
- `Game`: Manages the game flow.
- `Board`: Handles board setup and checking for wins.
- `Player`: Represents a player.

## How to Run
```bash
python Game.py


