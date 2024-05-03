'''
    Beini Wang
    CS5001, Spring 2023
    Project Game 2048
    This is main function of running Game 2048 on Turtle.
'''

from Game import Game
import turtle as t
from random import randint, choice

def start_new():
    
    '''
    Function:
        a function to clear the turtle screen and run main function,
        designed for the re-start game 2048 feature
    '''
    
    t.clear()
    main()

def main():
    
    '''
    main function starts Game 2048 and link key press events to designed 
    methods
    '''

    # ask user to input the size of the game board
    # set default size to 4, and size should not be at least 4
    # any larger board would take ultimately long to run
    size = int(t.numinput('Game size:', 'size number(at least 4)', 
                          default=4, minval=4))
    
    # set the canvas large enough to show all content, and expand the window
    t.screensize((55 * size) * 2, (55 * size) * 2)
    screen = t.Screen()
    screen.setup(width=1.00, height=1.00, startx=None, starty=None)
    game = Game(size)
    
    # hide turtle and accelerate the process
    t.ht()
    t.tracer(0)
    t.title('Game 2048')
    
    # start game and link keys
    game.start()
    t.listen()
      
    # link all keys to print a unrecognized msg method, use onkeypress to 
    # avoid showing message when user finished enter size and hit 'Enter'
    t.onkeypress(game.press, '')
    
    # re-link eligible keys to designed methods
    # including re-start/quit game, shift numbers in four directions
    t.onkeypress(t.bye, 'Escape')
    t.onkeypress(start_new, 's')
    t.onkeypress(game.left, 'Left')
    t.onkeypress(game.right, 'Right')
    t.onkeypress(game.up, 'Up')
    t.onkeypress(game.down, 'Down')
    t.mainloop()

if __name__ == "__main__": 
    main()