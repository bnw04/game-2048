Beini Wang, Spring 2023
Game 2048 Program

An explanation of the high-level design:
In File Game.py: 
The game 2048 is implemented in a class named "Game," which is designed to create and manage the traditional game 2048 in Python 
using the turtle graphics library for visual representation. The class includes methods for initializing the game board, 
adding new tiles, compressing and moving tiles, checking for win or game over, and updating the score. The class attributes 
include the size of the game board, the matrix representing the game board, flags indicating whether the player has won 
or loss, and the current score and if the current move is possible. For the description of each method, please see the bottom of
this file.
In File main.py:
There's a import of class "Game" and a defined start function that re-runs the main function in file. The main function starts 
the game by asking player what size of the board is and display the size x size grid on Python Turtle with two tiles of 2 or 4 
added on the game board, set the Turtle canvas to a size that all content will be visible, bind the specifically designed methods 
of class Game to the key-press event of eligible keys.
In File TestGame.py:
There's a import of class "Game" and unittest to test all logic methods in "Game" class. Using the setter and counting total 
non-zero tiles/totaling all number tiles in the game board methods, and AssertEqual/True/False/In methods of unittest class to see
if all logic methoes are working as expected as designed. The running result of the test should be OK.

Instructions on how to run the program:
To run the program, simply run main.py. When the program starts, first the grid size will be asked, the default size is 4 and 
any number greater than 4 will generate the size of game board accordingly (considering the original game only support size 4 grid,
any number greater than 100 is not recommended because that will take ultimately long time to run). If it's not a number or 
not at least 4, program will ask you again to enter the number. Any float number will be round down and that integer of grid will
be created and to start the game.
The game board will be displayed on the screen with two 2 or 4 number tile at random positions, and the score and instruction 
on which keys are eligible will be displayed at all time.
The player can use arrow keys to shift the number tiles on the game board in one of the four directions, left, right, up and down 
each time accordingly, use key 's' to restart the game by re-entering the game size, and use 'Esc' to quit the game by closing Turtle 
window. Any other keys are not recognizable. Player may re-start or quit the game at any time using the keys as explained above.

Features that work in this program include:
- The game board is initialized with asking the player to enter the size of the board, (default size number is 4 and 
  any least 4 number will be accepted, greater then 100 number is not recommended). Each number tile will be drawn as a square with
  number in it, 0 number will be shown as an empty square.
- The board features each number of tiles has a unique color, making it easier to identify and has a highlight when cells merge.
- The game has defined keys can be used by the player, if any other keys are pressed, a 'key not recgonized' message will be displayed.
- The player's score will be drawn on the board and updates with every move. The player earns points by combining two tiles with 
  the same number. The value of the combined tiles is added to the player's score.
- The player can use arrow keys on keyboard to shift the tiles and when two tiles with the same number are slide into each other, they 
  merge into a new tile with double the value on game board. And if any shifts, merge happends, a new tile with value 2 or 4 will 
  replace an empty in a random place. If no change on the game board with current move, no tile will be added like traditional 2048 game.
  The process is not shown and the resulting grid, game board will be displayed after the key-press event.
- The player can restart or quit the game at any time by pressing key 's' to restart or key 'Esc' to close Turtle window. 
- The game ends when there are no more moves left, and the player cannot merge any more tiles. A game over message will be displayed and
  player can no longer move the current board and has the option to restart or quit game.
- The player wins when there is a value of 2048 on game board even if the game over condition is met after the last move(win and loss
  message will never show up at the same time, win determination has higher priority). A you-win message will be displayed and player 
  can no longer move the current board and has the option to restart or quit game.
- The turtle canvas will be set large enough to show all content of game of any size, and will self expand after player entering the 
  game board size.
- The game board, player's score, game instruction will be displayed at all time when player's playing, key not recognized/win/loss
  messages will show up as conditions are met.

Game class methods list:
add_tile(): Adds a new tile with a value of 2 or 4 to a random zero tile position on the game board.
start_game(): Initializes the game by adding two tiles with a value of 2 or 4 to random positions on the empty game board.
compress(): Compresses the game board by moving all tiles to the left, leaving empty spaces on the right.
sum_left(): Merges tiles to left on the game board by adding their values together if they are adjacent and have the same value.
horizontal_change(): Reverses the order of the tiles in each row of the game board.
diagonal_change(): Transposes the game board by swapping rows and columns.
move_left(): Moves all tiles on the game board to the left and merges them if possible.
move_right(): Moves all tiles on the game board to the right and merges them if possible.
move_up(): Moves all tiles up on the game board and merges them if possible.
move_down(): Moves all tiles down on the game board and merges them if possible.
check_curmove(): Check if the move changes the game board, if so add a new tile, else do nothing.
game_win(): Check if player wins the game by checking if value of 2048 is on the game board.
can_move_final(): A helper method for game over check, to check if any adjacent same number tiles(includes 0).
game_over(): Check if game is over by checking if no 0 tiles on board and no adjacent same number by calling helper method.
check_status(): executes check_curmove/game_win/game_over to check the win/loss status and if a new tile needs to be added.
draw_msg(msg, x, y): To draw a str msg on Turtle canvas position (x, y).
draw_default(): To draw default instruction and score to display on game board.
win_lose_msg(): To draw win/loss message on game board if game_win/game_over condition is met.
press(): To draw 'Key not recognized' message on game board.
draw_square(num): A helper method for drawing the game board, draw a square of the tile of game board with specified color and number
draw_board(matrix): To draw the current game board with all numbered tiles.
start(): To draw the start game board with two 2 or 4 random position tiles on game board.
left(): To draw the game board after left move and with default instruction, score, possible message
right(): To draw the game board after righ move and with default instruction, score, possible message
up(): To draw the game board after up move and with default instruction, score, possible message
down(): To draw the game board after down move and with default instruction, score, possible message
set_matrix(lst): A setter method that could set the object's matrix to an eligible game board(if not eligible, error will raise)
set_canmove(b): A setter method that could set the object's canmove flag(indicating if current move changes the board)
not_zero_count(): To count the not zero tiles of the current game board.
total(): To total all number tiles of the current game board.