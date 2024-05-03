'''
    Beini Wang
    CS5001, Spring 2023
    Project Game 2048
    This is a program of a Game class that represents game 2048 design.
'''

import turtle as t
from random import randint, choice

class Game:

    '''
    Class: Game
    This class creates a 2048 game in Python turtle. It initializes the size
    of the grid and the starting matrix with 0s. It also has methods to add a 
    new tile with 2 or 4 in a random position, start the game with at least
    two random elements in list are 2 or 4, compress the matrix by moving all
    numbers to the left of the grid, sum up the numbers in the left row if two
    of them are the same, change the list by moving numbers horizontally,
    and by flipping number over its diagonal, and check if the player wins or
    the game is over. The left, right, up, and down methods move the tiles 
    in their respective direction and check for win and game over. A new tile
    (2 or 4)will be added to the list after each action(if movable), and so 
    the elements in list are 0s or power to 2 from 2 to 2048. Drawing methods
    are using turtle to present the list in a square as it visually helps 
    users to see the moves and the game.
    Parameters:
    - size (int): The size of the grid. It should at least be 4, if less than
    4 or not an int, error will raise
    Attributes:
    - size (int): The size of the grid
    - matrix (list): The matrix of the list representing the game board,
    a nested list of size number elements and each number contain size number
    of 0, power to 2 from 2 to 2048
    - win (bool): A flag indicating whether the player wins or not.
    - over (bool): A flag indicating whether the player losses or not.
    - score (int): The current score of the player(calculating by adding all
      combined numbers)
    - canmove(bool): A flag indication whether the left, right, up, down
    action is possible when updating the matrix(is created and updated in
    add_tile method)
    '''

    def __init__(self, size):
        
        '''
        It initializes a new instance of the Game class.
        Parameters:
        - size (int): The size of the grid, should be at least 4
        Preconditions:
        size is a positive integer more than 3, if less than four or not
        an int, ValueError is raised
        Postconditions:
        A new instance of the Game class is created with the specified size
        matrix is a list of size number of element and each element includes 
        size number of 0s, representing the 2D version list for game 2048
        - The win flag is set to False.
        - The over flag is set to False.
        - The score is set to 0
        - The canmove flag indication whether the left, right, up, down
        action is possible when updating the matrix is set to False
        '''

        # if size number is not int or less than 4, raise error
        if not isinstance(size, int) or size < 4:
            raise ValueError('game grid size should be at least 4 int')

        # initialize value of attributes      
        self.size = size

        # initial lize a list representing the 2D version list for game 2048
        # the first element representing all number tiles of bottom row of 
        # game board, second is the second bottom row and so on
        # index of each element of elements are the column position of tile
        self.matrix = [[0] * self.size for row in range(self.size)]
        self.win = False
        self.over = False
        self.score = 0
        self.canmove = False

      
    def add_tile(self):

        '''
        Method:
        it adds one new tile to the list(the attribute matrix), with int
        2 or 4 in a random position that is not 0 in the list and updates
        the matrix list
        Return(list):
            matrix(list), the nested list have one 2 or 4 replaced one 0
            in the list of lists
        Preconditions:
        attribute matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Postconditions:
            canmove(bool) is updated to default False, will update later
            in following moving tile methods
            the matrix(list) will be updated with the new tile(2 or 4)
        '''

        # after each move, set the default can move value to False
        self.canmove = False

        # randomly select a position in the list
        row, col = randint(0, (self.size - 1)), randint(0, (self.size - 1))

        # if the number i n that postion of matrix is not 0, select again
        while self.matrix[row][col] != 0:
            (row, col) = (randint(0, (self.size - 1)), 
                          randint(0, (self.size - 1)))

        # update the matrix(list) with new tile with number 2 or 4
        self.matrix[row][col] = choice([2, 4])
        return self.matrix
    
    def start_game(self):

        '''
        Method:
        it starts the game by adding two or more tiles with 2 or 4 in random
        positions of the matrix(list) and matrix is updated and draw_score
        executed and draw score in Turtle (score is 0)
        function
        Return(list):
            matrix(list), the nested list have two 2 or 4 replaced one 0
            in the list of lists
        Pre-condition:
            matrix(list) is the nested list created in constructor, list of 0s
        Post condition:
            matrix(list) will be updated with at least 2 at most 4 elements
            at random positions replaced by number 2 or 4(random)
        '''

        # randomly select the row and col for position for two numbers
        for start in range(2):
            self.matrix = self.add_tile()
        
        # call draw function to print score when starting game 
        # (self.score is 0 as set in constructor)
        return self.matrix

    def compress(self):
        
        '''
        method to compress all the non-zero numbers in nested list: 
        self.matrix, all non-zero number are moved to least index position
        as possible in the elements (lists) of the nested list (matrix)
        and update the attribute matrix
        Precondition:
        The current grid must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Postcondition:
        The grid is compressed so that all non-zero values are shifted to
        the leftmost column of each row, with any empty spaces to the right
        of the non-zero values filled with zeros. The canmove flag is set
        to True if any numbers were moved during the compression.
        '''

        # create a new list to store compressed numbers
        new_matrix = [[0] * self.size for row in range(self.size)]

        # loop thru all elements(row in game)
        for row in range(self.size):

            # set first position to 0
            pos = 0
            for col in range(self.size):

                # if element in row(row, col position in game) is not zero
                if self.matrix[row][col] != 0:

                    # update the number to new matrix
                    new_matrix[row][pos] = self.matrix[row][col]

                    # if any position of number in attribute matrix changed
                    # meaning matrix can be moved, the left move is possible
                    # change canmove attribute to True
                    if col != pos:
                        self.canmove = True
                    
                    # current position filled, move to next one
                    pos += 1
        self.matrix = new_matrix
    
    def sum_left(self):

        '''
        to sum up adjacent equal and not 0 numbers of the elements of 
        matrix(lists) on the left possible index position of the element and 
        the next index position number will be changed to zero. if there's 
        non-zero two adjacent equal numbers, attribute canmove will be 
        changed to True, and score will update its value by adding the sumed 
        up number
        Precondition:
        The current grid must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Postcondition:
        score will be updated by adding the sumed up number values, canmove
        will be updated if there's sumed up number, matrix will be updated 
        with all non-zero equal adjacent number, the next index position will
        be changed to 0
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        '''

        # if the numbers sum up after add all same numbers
        for row in range(self.size):
            for col in range((self.size - 1)):

                # see if numbers next to each other on one row is same 
                # and not 0
                if ((self.matrix[row][col + 1] == self.matrix[row][col]) and 
                    self.matrix[row][col]):

                    # then the left number is the sum of two same number
                    # (times 2)
                    self.matrix[row][col] *= 2

                    # updata the score with the value that is created
                    self.score += self.matrix[row][col]

                    # right number changes to 0
                    self.matrix[row][col + 1] = 0

                    # update the status that the matrix has numbers sum up
                    self.canmove = True
    
    def horizontal_change(self):
        
        '''
        Method:
        to reverse numbers horizontally of the elements of the list(matrix)
        (reverse the sequence)
        Precondition:
        The current grid must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        matrix will be updated with all numbers in the elements to a 
        horizontally reversing order
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        '''

        # create a new list
        new_matrix = []

        # loop thru size number times
        for row in range(self.size):

            # add []
            new_matrix.append([])

            # append of the numbers in attribute matrix list 
            # index position to a reverse sequence to the new list
            for col in range(self.size):
                new_col = (self.size - 1) - col
                new_matrix[row].append(self.matrix[row][new_col])
        
        # update matrix attribute
        self.matrix = new_matrix
    
    def diagonal_change(self):

        '''
        Method:
        to transpose numbers diagonally of the lists of the list(matrix)
        (interchanging positions of rows and column in the matrix)
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        matrix will be updated with all numbers in the elements to 
        a transposing order(interchanging positions of rows and column)
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        '''

        # create a new matrix as the matrix in constructor
        new_matrix = [[0] * self.size for row in range(self.size)]

        # append the elements of attribute matrix with 
        # interchanging the rows and columns index of the element
        for row in range(self.size):
            for col in range(self.size):
                new_matrix[col][row] = self.matrix[row][col]
        
        # update the attribute matrix
        self.matrix = new_matrix
    
    def move_left(self):

        '''
        Method:
        moves all tiles to the left and merges adjacent tiles of the same 
        value. score attribute is updated/added with each merged value 
        canmove attribute change to True if compress or 
        horizontally same adjacent values exists
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        current matrix (game board) is modified by moving all the tiles to 
        left, with any adjacent tiles of the same value being merged and 
        their sum added value to the player's score, canmove is updated to
        True if matrix has any changes
        '''

        # first compress all non-zero number to left
        self.compress()

        # sum same value adjacent number, 
        # the next index position will change to 0, and score updated
        self.sum_left()

        # then compress to left again
        self.compress()

    def move_right(self):

        '''
        Method:
        moves all tiles to the right and merges adjacent tiles of the same 
        value. Score attribute is updated/added with each merged value 
        canmove attribute change to True if compress or 
        horizontally same adjacent values exists
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        current matrix (game board) is modified by moving all the tiles to 
        right, with any adjacent tiles of the same value being merged and 
        their sum added value to the player's score, canmove is updated to
        True if matrix has any changes
        '''

        # first reverse the elements in matrix
        self.horizontal_change()

        # execute same steps as in move_left
        self.compress()
        self.sum_left()
        self.compress()

        # reverse the elments in matrix again
        self.horizontal_change()

    def move_down(self):

        '''
        Method:
        moves all tiles down and merges adjacent tiles of the same value. 
        score attribute is updated/added with each merged value, canmove 
        attribute change to True if compress or vertically same adjacent
        values exists
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        current matrix (game board) is modified by moving all the tiles down
        with any vertically adjacent tiles of the same value being merged and 
        their sum added value to the player's score, canmove is updated to
        True if matrix has any changes
        '''

        # first transpose the elements in matrix
        self.diagonal_change()

        # execute same steps as in move_left
        self.compress()
        self.sum_left()
        self.compress()

        # transpose the elements in matrix again
        self.diagonal_change()

    def move_up(self):

        '''
        Method:
        moves all tiles up and merges adjacent tiles of the same value. Score
        attribute is updated/added with each merged value, canmove attribute 
        change to True if compress or vertically same adjacent values exists
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        current matrix (game board) is modified by moving all the tiles up 
        with any vertically adjacent tiles of the same value being merged and 
        their sum added value to the player's score, canmove is updated to
        True if matrix has any changes
        '''

        # first transpose elements in matrix
        self.diagonal_change()

        # execute same steps as in move_right
        self.horizontal_change()
        self.compress()
        self.sum_left()
        self.compress()
        self.horizontal_change()

        # again to transpose elements in matrix
        self.diagonal_change()

    def check_curmove(self):
        
        '''
        Method:
        Check if there is a possible matrix change when tiles shift(either 
        compress or sum_left method changed matrix attribute), by checking
        canmove is True. If so, add a new tile to game board (replace a 0 in 
        matrix with either 2 or 4)
        Preconditions:
        The current grid must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power of 2 numbers from 2 to 2048   
        Postconditions:
        If there is a possible move left on the board, replace a 0 in matrix 
        with either 2 or 4, otherwise do nothing
        '''

        # to check in the current shift, if canmove is True 
        # either compress or sum numbers to left is possible 
        if self.canmove:

            # execute add_tile
            self.add_tile()
     
    def game_win(self):
        
        '''
        Method:checks if player won game by searching for the number 2048 
        in the matrix attribute. If the number is found, the win attribute of
        the object is set to True, if not will leave it unchanged
        (default False)
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        win attribute will change to True if 2048 found
        '''

        # loop thru each element of matrix
        for row in self.matrix:

            # if 2048 found, change win attribute to True and return True
            if 2048 in row:
                self.win = True

    def can_move_final(self):

        '''
        A helper method for the final move check (if game is over)
        Checks if there is any valid equal numbers(including 0s here) in 
        matrix/game by looping through and checking if there are any adjacent 
        cells that have the same value, either horizontally or vertically
        Return(bool):
            return True if there are equal numbers, False otherwise
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        '''

        # loop thru the list and see if any horizontally adjacent numbers
        # are equal (element in elements of nested list, matrix)
        for row in range(self.size):
            for col in range((self.size - 1)):
                if self.matrix[row][col] == self.matrix[row][col + 1]:

                    # if so, return True
                    return True
        
        # loop thru the list and see if any vertically adjacent numbers
        # are equal (element with same index number of elements in matrix)
        for row in range((self.size - 1)):
            for col in range(self.size):
                if self.matrix[row][col] == self.matrix[row + 1][col]:

                    # if so, return True
                    return True
        
        # else False
        return False
    
    def game_over(self):
   
        '''
        Method:checks if player loss the game by searching if there's any 0
        in the matrix attribute. If no, then use the helper method to check
        if there's possible move to left (equal adjacent numbers), if no,
        then it means current game is over
        Return:
        return when there's 0 in matrix, to end this method(because if 
        there's 0, game is not over)
        Precondition:
        The current matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        with win attribute False (to avoid 2048 in grid and one more tile 
        added to grid, and fake a game over here), over attribute will be 
        updated to True if no 0 in matrix and no adjacent equal elements
        '''

        # first make sure win attribute is not True
        if not self.win:

            # loop thru matrix, see if there's zero in it
            for row in self.matrix:

                # if there's 0, then return and end method
                if 0 in row:
                    return
                
            # if no 0 in the matrix, execute can_move_final method
            # see if there's possible move to left, if no
            if not self.can_move_final():

                # over attribute changed to True
                self.over = True

    def check_status(self):
        
        '''
        method executes game_win(), check_curmove(), game_over(), 
        (three methods created above) to check win/loss status and should a 
        new tile add to the board (used before drawing the current game 
        board in later drawing methods)
        '''
        
        self.game_win()
        self.check_curmove()
        self.game_over()

    # down below are drawing methods for turtle to draw on canvas
    def draw_msg(self, msg, x, y):

        '''
        Method:
        to write the msg(str) at (x,y) on turtle canvas
        Parameters:
            msg(str): the msg str for turtle to write
            x(int or float): the x coordinate of the writting position
            y(int or float): the y coordinate of the writting position
        Post condition:
        the message will be written on canvas align to left at (x,y)
        '''

        t.pu()

        # set to position (x,y)
        t.goto(x, y)

        # write the message align to left
        t.write(msg, align='left', font=('Helvetica', 16, 'normal'))
        t.setpos(0, 0)
    
    def draw_default(self):

        '''
        Method:
        to write the instruction, score at certain position on turtle canvas
        Post condition:
        the instruction/score(int) attribute will be written on canvas align 
        to left at (x,y)
        '''

        # set pen color for messages
        t.pencolor('#695c57')

        # write the attribute number, score at (-20,-130)
        self.draw_msg(f'score: {self.score}', -20, -130)

        # and the instruction of of recognizable keys
        self.draw_msg(("Game 2048: \n" +
                       "Try to combine numbers and reach 2048!\n" + 
                       "Press key 's' to restart a new game\n" + 
                       "Press key 'Esc' to quit\n" + 
                       "Press arrow keys \u2191, \u2193, \u2190, \u2192\n" +
                       "to shift all numbers accordingly\n" + 
                       "Any other keys are not recognizable"), -500, -40)
        
    def win_lose_msg(self):

        '''
        Method:
        to write the win/loss message when player wins/losses the game using
        attribute win/over
        Post condition:
        if player wins(win attribute is True), write winning message
        if player losses(over attribute is True), write gameover message
        '''

        # using win/over attribute and write the message accordingly
        if self.win:
            self.draw_msg("You win! Press 's' to restart game.", -20, -160)
        elif self.over:
            self.draw_msg("Game Over! Press 's' to restart game.", -20, -160)
    
    def press(self):

        '''
        Method:
        method for all unrecognizable keys, to write a message saying
        key is not recognizable
        '''
        
        # write the message key not recogized if executed
        self.draw_msg('Key not recognized', -20, -190)
        
    def draw_square(self, num):

        '''
        Method:
        method to draw a square with certain filling color with a side of 50
        and write a non-zero number in the square 
        Parameter(int):
        num: it's a non-negative int, to be written in the square drawn, 
        0 will not be written
        Precondition:
        num must be 0 or power to 2 from 2 to 2048
        Post condition:
        a square filled with color and non-zero number will be drawn
        '''

        # set the side length of square to 40
        side = 50
        
        # create the lists of possible numbers/filling colors for numbers
        number = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        color = ['white', 'beige', 'bisque', 'light gray', 'orange', 'coral', 
                'thistle', 'plum', 'light blue', 'pale green', 
                'green yellow', 'gold']
        
        # create a dict of keys of numbers with values of its filling color
        fill = {number[i]: color[i] for i in range(len(number))}

        # fill with the color as specified        
        t.color('black', fill[num])
        t.begin_fill()

        # draw each square with pen color
        t.pencolor('#b8afa9')
        for s in range(4):
            t.pd()
            t.forward(side)
            t.left(90)

        t.end_fill()

        # change pen color back to black
        t.pencolor('black')

        # write the non-zero number
        if num != 0:
            t.pu()
            t.setheading(0)

            # at the bottom middle of the square
            t.forward(side/2)
            t.write(num, align='center', font=('Helvetica', 16, 'bold'))

    def draw_board(self, matrix):

        '''
        Method:
        method to draw game board with bottom left corner at (-100, -100)
        and using matrix(list) to draw each element in it as a square, number
        tile of the game, using draw_square method, after drawing each element
        of one row, move up distance 55 to draw the next row, till the end
        of the list
        Parameter(list):
            matrix, not attribute(list), a nested list of int numbers: 0s and
            power to 2 from 2 to 2048
        Precondition:
        matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        a game board will be drawn with bottom left corner at (-100, -100)
        '''

        # set the bottom left corn of the board to (-100, -100)
        start_x = -100
        start_y = -100

        # after drawing each square, move distance is 55
        side = 55
        t.pu()
        t.setpos(start_x, start_y)
        t.setheading(0)

        # draw rows of squares with the number of size
        for row in range(self.size):

            # draw each row of squares with number of size
            for col in range(self.size):

                # write number, draw square with color
                self.draw_square(matrix[row][col])
                t.pu()

                # after drawing each square move to next right square in row
                start_x += side
                t.setpos(start_x, start_y)
                t.setheading(0)
            
            # after drawing each row, move to the next row on top of
            start_y += side
            start_x = -100   
            t.setpos(start_x, start_y)

    def start(self):
        
        '''
        method to start the game by drawing the game board(matrix) after
        executing start_game method(having two 2 or 4 tiles in Game object)
        and draw the instruction and score
        '''

        self.draw_board(self.start_game())
        self.draw_default()
    
    def left(self):
        
        '''
        method: if game not won yet, clear canvas execute move_left and 
        check_status methods to check if a tile needs to add and win/lose 
        condition and draw game board and display instruction score and 
        win/loss accordingly, if game won, do nothing
        Post condition:
        if game not won, clear canvas, draw current matrix of object and write
        message accordingly
        '''

        # if game not won by player yet
        if not self.win:
            t.clear()
            
            # execute move_left()
            self.move_left()
            
            # check if game is won by player
            self.check_status()
            
            # draw the gameboard and display msg
            self.draw_board(self.matrix)
            self.win_lose_msg()
            self.draw_default()
            
    def right(self):
        
        '''
        method: if game not won yet, clear canvas execute move_right and 
        check_status methods to check if a tile needs to add and win/lose 
        condition and draw game board and display instruction score and 
        win/loss accordingly, if game won, do nothing
        Post condition:
        if game not won, clear canvas, draw current matrix of object and write
        message accordingly
        '''
        
        # if game not won by player yet
        if not self.win:
            t.clear()
            
            # execute move_right()
            self.move_right()
            
            # check if player wins or lossed the game 
            # and if cur move is possible (add tile or not)
            self.check_status()
            
            # draw the gameboard and display msg
            self.draw_board(self.matrix)
            self.win_lose_msg()
            self.draw_default()
    
    def up(self):
        
        '''
        method: if game not won yet, clear canvas execute move_up and 
        check_status methods to check if a tile needs to add and win/lose 
        condition and draw game board and display instruction score and 
        win/loss accordingly, if game won, do nothing
        Post condition:
        if game not won, clear canvas, draw current matrix of object and write
        message accordingly
        '''
        
        # if game not won by player yet
        if not self.win:
            t.clear()
            
            # execute move_up()
            self.move_up()
            
            # check if player wins or lossed the game 
            # and if cur move is possible (add tile or not)
            self.check_status()
            
            # draw the gameboard and display msg
            self.draw_board(self.matrix)
            self.win_lose_msg()
            self.draw_default()
    
    def down(self):
        
        '''
        method: if game not won yet, clear canvas execute move_down and 
        check_status methods to check if a tile needs to add and win/lose 
        condition and draw game board and display instruction score and 
        win/loss accordingly, if game won, do nothing
        Post condition:
        if game not won, clear canvas, draw current matrix of object and write
        message accordingly
        '''
        
        # if game not won by player yet
        if not self.win:
            t.clear()
      
            # execute move_down()
            self.move_down()
            
            # check if player wins or lossed the game 
            # and if cur move is possible (add tile or not)
            self.check_status()
            
            # draw the gameboard and display msg
            self.draw_board(self.matrix)
            self.win_lose_msg()
            self.draw_default()

    # setter methods
    def set_matrix(self, lst):
        
        '''
        method: to set the matrix attribute of object
        Post condition:
        if lst passed in is not a list, or list length and number of elements 
        of list is not the size of the object, all numbers in lst is not 0 or 
        power to 2 from 2 to 2048(eligible numbers in 2048 game), raise error
        '''
        
        # set matrix is not a list raise error
        if not isinstance(lst, list):
            raise ValueError('Cannot set this type of Value')
        
        # create a list of eligible number tiles in game board
        eligible = [0]
        for number in range(1, 12):
            eligible.append(2 ** number)
        
        # if number tile in the set matrix is not eligible raise error
        # set row numbers to zero
        r = 0
        
        # set a list of col numbers
        col = []
        for row in lst:
            r += 1
            
            # set and reset col number to 0 for each row
            c = 0
            for tile in row:
                if tile not in eligible:
                    raise ValueError('number tile in set matrix not eligible')
                c += 1
                
            # append the col numbers of each row in the list
            col.append(c)
            
        # if row number is not the object size, raise error
        if r != self.size:
            raise ValueError('set matrix has wrong row number')
        
        # if any col number is not the object size, raise error
        for c in col:
            if c != self.size:
                raise ValueError('set matrix has wrong col number')
        
        # if no error raised, can set object matrix to the parameter list
        self.matrix = lst

    def set_canmove(self, b):
        
        '''
        method: to set the canmove attribute of object, canmove is a bool type
        flag indicating if the current move direction is possible(after move,
        matrix changes)
        Post condition:
        if b passed in is not a bool type value, raise error
        '''
        
        if not isinstance(b, bool):
            raise ValueError('Cannot set this type of Value')
        self.canmove = b
        
    # methods created for testing purposes
    def not_zero_count(self):
        
        '''
        method to count the number of all non-zero tiles of matrix of object
        Return(int):
        an int of the number of all non-zero tiles of current matrix
        '''

        count = 0
        
        # loop thru all tiles of current matrix
        for row in range(self.size):
            for col in range(self.size):
                
                # if it's not 0, count + 1
                if self.matrix[row][col] != 0:
                    count += 1
        return count
    
    def total(self):
        
        '''
        method to sum up all number tiles of current matrix of object
        Return(int):
        an int of total number of all number tiles of current matrix
        '''
        
        sum = 0
        
        # loop thru each number of current matrix
        for row in self.matrix:
            for number in row:
                
                # add each number
                sum += number
        return sum
