'''
    Project Game 2048
    This is a program of a GameTest class that tests all not helper/turtle 
    methods in Game class.
'''

from Game import Game
import unittest

class GameTest(unittest.TestCase):

    '''
    GameTest class using unittest to test if all logic non-helper methods in 
    Game class are working as expected
    '''

    def setUp(self):
        
        '''
        this method will be executed before each test, Games are, matrix lists
        are defined in this method
        '''
        
        # Game object created
        self.g1 = Game(4)
        self.g2 = Game(8)
        self.g3 = Game(5)
        
        # the list of possible number tiles of a new tile
        self.tile = [2, 4]

        # matrix values
        self.m1 = [[0, 2, 0, 2],
                   [8, 0, 2, 0],
                   [4, 4, 4, 64],
                   [0, 0, 256, 0]]        
        self.m2 = [[8, 4, 4, 4],
                   [8, 4, 0, 0],
                   [8, 2, 0, 0],
                   [0, 0, 0, 0]]   
        self.m3 = [[8, 16, 4, 64],
                   [0, 16, 8, 0],
                   [8, 0, 0, 512],
                   [2, 16, 8, 256]]      
        self.m4 = [[8, 16, 4, 64],
                   [8, 16, 8, 2],
                   [8, 16, 4, 512],
                   [2, 16, 8, 256]]      
        self.m51 = [[8, 4, 4, 4, 0],
                    [8, 4, 0, 0, 0],
                    [8, 2, 2, 0, 0],
                    [0, 0, 0, 16, 0],
                    [0, 0, 32, 0, 0]]

    def test_constructor(self):
        
        '''
        test the constructor of class Game to see if attributes of object
        equal to the expected value
        error will raised if size passed in is not an int or value less than
        three
        '''

        # the expected matrix created for different game size
        g1_m = [[0] * 4 for row in range(4)]
        g2_m = [[0] * 8 for row in range(8)]
        g3_m = [[0] * 5 for row in range(5)]

        # to test size 4 all setup attributes in constructor
        self.assertEqual(self.g1.size, 4)
        self.assertEqual(self.g1.matrix, g1_m)
        self.assertEqual(self.g1.score, 0)
        self.assertFalse(self.g1.win)
        self.assertFalse(self.g1.over)
        self.assertFalse(self.g1.canmove)

        # to test size 8 all setup attributes in constructor
        self.assertEqual(self.g2.size, 8)
        self.assertEqual(self.g2.matrix, g2_m)
        self.assertEqual(self.g2.score, 0)
        self.assertFalse(self.g2.win)
        self.assertFalse(self.g2.over)
        self.assertFalse(self.g2.canmove)
        
        # to test size 5 all setup attributes in constructor
        self.assertEqual(self.g3.size, 5)
        self.assertEqual(self.g3.matrix, g3_m)
        self.assertEqual(self.g3.score, 0)
        self.assertFalse(self.g3.win)
        self.assertFalse(self.g3.over)
        self.assertFalse(self.g3.canmove)
        
        with self.assertRaises(ValueError):
            game = Game(3)
            
        with self.assertRaises(ValueError):
            game = Game('not an int')
    
    def test_set_matrix(self):
        
        '''
        test the set_matrix of class Game, if the matrix value passed in is
        not a list or doesn't have object size, not eligible number tile,
        error will be raise
        Post condition: the matrix attribute of the object will be changed
        to the parameter value, if no error raised
        '''
        
        # test1, with eligible matrix passed in 
        self.g1.set_matrix(self.m1)
        self.assertEqual(self.g1.matrix, self.m1)
        
        # test2, with eligible matrix passed in 
        self.g3.set_matrix(self.m51)
        self.assertEqual(self.g3.matrix, self.m51)
        
        # test 3, if set matrix is not a list, error raise
        with self.assertRaises(ValueError):
            self.g1.set_matrix('not a matrix')
        
        # test 4, if set matrix size is not the same with the object size
        with self.assertRaises(ValueError):
            self.g1.set_matrix(self.m51)
        
        # test 5, if set matrix has not eligible number tile
        with self.assertRaises(ValueError):
            self.g1.set_matrix([[6, 3000, 4, 4],
                                [16, 4, 0, 0],
                                [8, 2, 0, 0],
                                [0, 0, 0, 0]])
    
    def test_set_canmove(self):
        
        '''
        test the set_canmove of class Game, if the parameter value passed in 
        is not a bool type, error will be raise
        Post condition: the canmove attribute of the object will be changed
        to the parameter value, if no error raised
        '''
        
        self.g1.set_canmove(True)
        self.assertTrue(self.g1.canmove)
        
        self.g1.set_canmove(False)
        self.assertFalse(self.g1.canmove)
        
        with self.assertRaises(ValueError):
            self.g1.set_canmove('not a bool')
    
    def test_total(self):
        
        '''
        test the total method of class Game, should return the total of number
        of tiles of the matrix attribute
        '''
        
        # test1, matrix have all 0s tiles, total is 0
        self.assertEqual(self.g1.total(), 0)
        
        # test2, test with object matrix set, total is all numbers total
        self.g1.set_matrix(self.m1)
        self.assertEqual(self.g1.total(), 346)
        
        # test3, another size object with matrix set
        # total is all numbers total
        self.g3.set_matrix(self.m51)
        self.assertEqual(self.g3.total(), 92)
        
    def test_not_zero_count(self):
        
        '''
        test the not_zero_count method of class Game, should return the count
        of not zero tiles of the matrix attribute
        '''
        
        # test1, matrix have all 0s tiles, not zero tile is 0
        self.assertEqual(self.g1.not_zero_count(), 0)
        
        # test2, test with object matrix set, check not zero tiles count
        self.g1.set_matrix(self.m1)
        self.assertEqual(self.g1.not_zero_count(), 9)
        
        # test3, another size object with matrix set
        # check not zero tiles count
        self.g3.set_matrix(self.m51)
        self.assertEqual(self.g3.not_zero_count(), 11)
    
    def test_add_tile(self):
        
        '''
        test the add_tile method of class Game, should update and return the 
        matrix attribute with one random position of a 0 tile replaced by a
        2 or 4 tile. Used total and not_zero_count methods to test the result
        '''

        # test1, after adding a tile, the non_zero count is 1 
        # and total is 2 or 4
        self.g1.add_tile()
        self.assertEqual(self.g1.not_zero_count(), 1)
        self.assertIn(self.g1.total(), self.tile)
        
        # if canmove attribute set to False
        self.assertFalse(self.g1.canmove)

        # test2, after adding a tile, the non_zero count is 1 
        # and total is 2 or 4
        self.g2.add_tile()
        self.assertEqual(self.g2.not_zero_count(), 1)
        self.assertIn(self.g2.total(), self.tile)
        
        # if canmove attribute set to False
        self.assertFalse(self.g1.canmove)

        # test3, set the game matrix to one with more tiles and test again
        self.g1.set_matrix(self.m1)
        
        # store the before count of non-zero and total of number tiles
        before_total = self.g1.total()
        before_count = self.g1.not_zero_count()
        self.g1.add_tile()
        after_total = self.g1.total()
        after_count = self.g1.not_zero_count()

        # if the difference of count is 1 and total sum is 2 or 4 more
        self.assertEqual(after_count - before_count, 1)
        self.assertIn(after_total - before_total, self.tile)
        
        # if canmove attribute set to False
        self.assertFalse(self.g1.canmove)

    def test_start(self):

        '''
        test the start_game method of class Game, should update and return the 
        matrix attribute with two random position of a 0 tile replaced by two
        2 or 4 tile. Used total and not_zero_count methods to test updated
        matrix
        '''

        # set the possible outcome of adding two 2 or 4 tiles as a list 
        tile_sum = [4, 6, 8]
        self.g1.start_game()
        self.g2.start_game()

        # start g1, check if the count is 2 and 
        # total of is in possible outcome list
        self.assertEqual(self.g1.not_zero_count(), 2)
        self.assertIn(self.g1.total(), tile_sum)

        # start g2, check if the count is 2 and 
        # total of is in possible outcome list
        self.assertEqual(self.g2.not_zero_count(), 2)
        self.assertIn(self.g2.total(), tile_sum)
    
    def test_compress(self):
        
        '''
        test the compress method of class Game, should update matrix attribute
        with all number tiles other than 0 shift to the possible left most
        position, if matrix has any changes, canmove attribute will change
        to True, test if matrix and canmove has expected value
        '''

        # test1
        # if matrix have all 0s tiles, after compress nothing changes
        # the canmove attribute will be False
        before = self.g1.matrix
        self.g1.compress()
        self.assertEqual(self.g1.matrix, before)
        self.assertFalse(self.g1.canmove)

        # test2, use self.m2
        # set the game matrix with no possible compress move
        self.g1.set_matrix(self.m2)
        
        # execute compress method, the matrix should not change
        self.g1.compress()

        # the expected matrix outcome after compress executed should be same
        # the canmove attribute will be changed to True
        self.assertEqual(self.g1.matrix, self.m2)
        self.assertFalse(self.g1.canmove)

        # test3, use self.m1
        # set the game matrix with possible compress move
        self.g1.set_matrix(self.m1)
        
        # execute compress method
        self.g1.compress()

        # the expected matrix outcome after compress executed
        # the canmove attribute will be changed to True
        after = ([[2, 2, 0, 0],
                  [8, 2, 0, 0],
                  [4, 4, 4, 64],
                  [256, 0, 0, 0]])
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # test4, set g3 matrix to m51
        # set the game matrix with possible compress move
        self.g3.set_matrix(self.m51)
        
        # execute compress method
        self.g3.compress()

        # the expected matrix outcome after compress executed
        # the canmove attribute will be changed to True
        after = [[8, 4, 4, 4, 0],
                 [8, 4, 0, 0, 0],
                 [8, 2, 2, 0, 0],
                 [16, 0, 0, 0, 0],
                 [32, 0, 0, 0, 0]]
        self.assertEqual(self.g3.matrix, after)
        self.assertTrue(self.g3.canmove)

    def test_sum_left(self):

        '''
        test the sum_left method of class Game, should update matrix attribute
        with all horizontally same adjacent number tiles sum up to the left
        tile, and next tile changes to 0, if matrix has any changes, canmove
        will change to True, test if matrix and canmove has expected value
        '''

        # test1
        # if matrix have all 0s tiles, after sum nothing changes
        # the canmove attribute will be False
        # score attribute will still be 0
        before = self.g1.matrix
        self.g1.sum_left()
        self.assertEqual(self.g1.matrix, before)
        self.assertFalse(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)

        # test2, use self.m3
        # set the game matrix with no possible sum ups move
        self.g1.set_matrix(self.m3)

        # execute sum_left method, the matrix should not change
        self.g1.sum_left()

        # the expected matrix outcome after compress executed should be same
        # the canmove attribute will be changed to False
        # score attribute will still be 0
        self.assertEqual(self.g1.matrix, self.m3)
        self.assertFalse(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)

        # test3, use self.m1, with same row has three same number
        # set the game matrix with possible compress move
        self.g1.set_matrix(self.m1)
        
        # execute compress method
        self.g1.sum_left()

        # the expected matrix outcome after sum to left executed
        # the canmove attribute will be changed to True
        # score attribute should be equal to the total of added numbers
        after = [[0, 2, 0, 2],
                 [8, 0, 2, 0],
                 [8, 0, 4, 64],
                 [0, 0, 256, 0]]
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 8)
        
        # test4, test with another size game
        # set the g3 matrix with possible compress move
        self.g3.set_matrix(self.m51)
        
        # execute compress method
        self.g3.sum_left()

        # the expected matrix outcome after sum to left executed
        # the canmove attribute will be changed to True
        # score attribute should be equal to the total of added numbers
        after = [[8, 8, 0, 4, 0],
                 [8, 4, 0, 0, 0],
                 [8, 4, 0, 0, 0],
                 [0, 0, 0, 16, 0],
                 [0, 0, 32, 0, 0]]
        self.assertEqual(self.g3.matrix, after)
        self.assertTrue(self.g3.canmove)
        self.assertEqual(self.g3.score, 12)
 
    def test_horizontal_change(self):
        
        '''
        test the horizontal_change method of class Game, should update matrix
        with all number tiles horizontally reverse their position
        test if matrix has expected value
        '''       
                
        # test1
        # if matrix have all 0s tiles, 
        # after horizontal change, nothing changes
        before = self.g1.matrix
        self.g1.horizontal_change()
        self.assertEqual(self.g1.matrix, before)
        
        # test2, use self.m1, set the expected horizontal change result
        self.g1.set_matrix(self.m1)
        self.g1.horizontal_change()
        after = [[2, 0, 2, 0],
                 [0, 2, 0, 8],
                 [64, 4, 4, 4],
                 [0, 256, 0, 0]]
        self.assertEqual(self.g1.matrix, after)
        
        # test3, use self.m1, set the expected horizontal change result
        self.g1.set_matrix(self.m2)
        self.g1.horizontal_change()
        after = [[4, 4, 4, 8],
                 [0, 0, 4, 8],
                 [0, 0, 2, 8],
                 [0, 0, 0, 0]]
        self.assertEqual(self.g1.matrix, after)
        
        # test4, test with another size game
        # set the expected horizontal change result
        self.g3.set_matrix(self.m51)
        self.g3.horizontal_change()
        after = [[0, 4, 4, 4, 8],
                 [0, 0, 0, 4, 8],
                 [0, 0, 2, 2, 8],
                 [0, 16, 0, 0, 0],
                 [0, 0, 32, 0, 0]]
        self.assertEqual(self.g3.matrix, after)
        
    def test_diagonal_change(self):
        
        '''
        test the diagonal_change method of class Game, should update matrix
        with all number tiles transpose their position, 
        test if matrix has expected value
        '''
        
        # test1
        # if matrix have all 0s tiles, 
        # after horizontal change, nothing changes
        before = self.g1.matrix
        self.g1.diagonal_change()
        self.assertEqual(self.g1.matrix, before)
             
        # test2, use self.m1, set the expected diagonal change result
        self.g1.set_matrix(self.m1)
        self.g1.diagonal_change()
        after = [[0, 8, 4, 0], 
                 [2, 0, 4, 0], 
                 [0, 2, 4, 256], 
                 [2, 0, 64, 0]]
        self.assertEqual(self.g1.matrix, after)
        
        # test3, test with another size game
        # set the expected diagonal change result
        self.g3.set_matrix(self.m51)
        self.g3.diagonal_change()
        after = [[8, 8, 8, 0, 0],
                 [4, 4, 2, 0, 0],
                 [4, 0, 2, 0, 32],
                 [4, 0, 0, 16, 0],
                 [0, 0, 0, 0, 0]]
        self.assertEqual(self.g3.matrix, after)

    def test_move_left(self):
        
        '''
        merges all horizontally adjacent tiles of the same value and moves 
        all non-zero tiles to the left. score attribute is updated/added
        with each merged value, canmove attribute change to True if matrix
        has any change, test matrix, canmove, score attributes
        '''
        
        # test1, if all 0 tiles matrix, after executing move_left matrix
        # should not change and canmove stay False, score not change
        before = self.g1.matrix
        self.g1.move_left()
        self.assertEqual(self.g1.matrix, before)
        self.assertEqual(self.g1.score, 0)
        self.assertFalse(self.g1.canmove)
        
        # test2, for real game case, after executing move_left, tiles shift
        # left and sum up same numbers, canmove changes to True, score updates
        self.g1.set_matrix(self.m1)
        after = [[4, 0, 0, 0],
                 [8, 2, 0, 0],
                 [8, 4, 64, 0],
                 [256, 0, 0, 0]]
        self.g1.move_left()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # first score update to 12
        self.assertEqual(self.g1.score, 12)
        
        # test3, no compress at first but possible sum up, after executing
        # tiles sum up same numbers and shift to left, canmove changes to True
        # set canmove to False(in test2 it was changed to True), updates score
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m2)
        after = [[8, 8, 4, 0],
                 [8, 4, 0, 0],
                 [8, 2, 0, 0],
                 [0, 0, 0, 0]]
        self.g1.move_left()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # since we didn't reset score, score accumulates (12+8)
        self.assertEqual(self.g1.score, 20)
        
        # test4, no possible sum up but compress, after executing
        # tiles sum up same numbers and shift to left, canmove changes to True
        # set canmove to False(test3 it was changed to True), score no change
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m3)
        after = [[8, 16, 4, 64],
                 [16, 8, 0, 0],
                 [8, 512, 0, 0],
                 [2, 16, 8, 256]]
        self.g1.move_left()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # since we didn't reset score, score remain to be 20
        self.assertEqual(self.g1.score, 20)
        
    def test_move_right(self):
        
        '''
        merges all horizontally adjacent tiles of the same value and moves 
        all non-zero tiles to the right. score attribute is updated/added
        with each merged value, canmove attribute change to True if matrix
        has any change, test matrix, canmove, score attributes
        '''
        
        # test1, if all 0 tiles matrix, after executing move_left
        # matrix attribute should not change and canmove stay False
        before = self.g1.matrix
        self.g1.move_right()
        self.assertEqual(self.g1.matrix, before)
        self.assertFalse(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)
        
        # test2, for real game case, after executing move_right, tiles shift
        # left and sum up same numbers, canmove changes to True, score updates
        self.g1.set_matrix(self.m1)
        after = [[0, 0, 0, 4],
                 [0, 0, 8, 2],
                 [0, 4, 8, 64],
                 [0, 0, 0, 256]]
        self.g1.move_right()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 12)
        
        # test3, no compress at first but possible sum up, after executing
        # tiles sum up same numbers and shift to right, canmove changes 
        # set canmove to False (in test2 it was changed to True)
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m2)
        after = [[0, 8, 4, 8],
                 [0, 0, 8, 4],
                 [0, 0, 8, 2],
                 [0, 0, 0, 0]]
        self.g1.move_right()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # since we didn't reset score, score accumulates (12+8)
        self.assertEqual(self.g1.score, 20)
        
        # test4, no possible sum up but compress, after executing, tiles
        # sum up same numbers and shift to right, canmove changes to True
        # set canmove to False since in test3 it was changed to True
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m3)
        after = [[8, 16, 4, 64],
                 [0, 0, 16, 8],
                 [0, 0, 8, 512],
                 [2, 16, 8, 256]]
        self.g1.move_right()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # since we didn't reset score, score remain unchange
        self.assertEqual(self.g1.score, 20)
        
    def test_move_up(self):
        
        '''
        draw function in Game class draw the bottom row first, so moves up 
        all tiles is to move all non-zero tiles to the largest possible index
        element of matrix 
        merges all vertically adjacent tiles of the same value and moves up
        all tiles. score attribute is updated/added with each merged value, 
        canmove attribute change to True if matrix has any change, test 
        matrix, canmove, score attributes
        '''
        
        # test1, if all 0 tiles matrix, after executing move_up
        # matrix attribute should not change and canmove stay False
        before = self.g1.matrix
        self.g1.move_up()
        self.assertEqual(self.g1.matrix, before)
        self.assertFalse(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)
        
        # test2, for real game case, after executing move_up, tiles shift
        # up with no sum up same numbers, canmove changes to True
        # no score update
        self.g1.set_matrix(self.m1)
        after = [[0, 0, 0, 0],
                 [0, 0, 2, 0],
                 [8, 2, 4, 2],
                 [4, 4, 256, 64]]
        self.g1.move_up()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)
        
        # test3, no compress at first but possible sum up, after executing
        # tiles sum up same numbers and move up, canmove changes to True
        # set canmove to False (in test2 it was changed to True)
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m4)
        after = [[0, 0, 4, 64],
                 [8, 0, 8, 2],
                 [16, 32, 4, 512],
                 [2, 32, 8, 256]]
        self.g1.move_up()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 80)
        
        # test4, sum up and compress, after executing, tiles
        # sum up same numbers and move up, canmove changes to True
        # set canmove to False since in test3 it was changed to True
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m3)
        after = [[0, 0, 0, 0],
                 [0, 0, 0, 64],
                 [16, 16, 4, 512],
                 [2, 32, 16, 256]]
        self.g1.move_up()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # score accumulates = 80+64 = 144
        self.assertEqual(self.g1.score, 144)
        
    def test_move_down(self):
        
        '''
        draw function in Game class draw the bottom row first, so moves down
        all tiles is to move all non-zero tiles to the least possible index
        element of matrix 
        merges all vertically adjacent tiles of the same value and moves down
        all tiles. score attribute is updated/added with each merged value, 
        canmove attribute change to True if matrix has any change, 
        test matrix, canmove, score attributes
        '''
        
        # test1, if all 0 tiles matrix, after executing move_down
        # matrix attribute should not change and canmove stay False
        before = self.g1.matrix
        self.g1.move_down()
        self.assertEqual(self.g1.matrix, before)
        self.assertFalse(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)
        
        # test2, for real game case, after executing move_down, tiles shift
        # down with no sum up same numbers, canmove changes to True
        # no score update
        self.g1.set_matrix(self.m1)
        after = [[8, 2, 2, 2],
                 [4, 4, 4, 64],
                 [0, 0, 256, 0],
                 [0, 0, 0, 0]]
        self.g1.move_down()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 0)
        
        # test3, no compress at first but possible sum up, after executing
        # tiles sum up same numbers and move down, canmove changes to True
        # set canmove to False (in test2 it was changed to True)
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m4)
        after = [[16, 32, 4, 64],
                 [8, 32, 8, 2],
                 [2, 0, 4, 512],
                 [0, 0, 8, 256]]
        self.g1.move_down()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        self.assertEqual(self.g1.score, 80)
        
        # test4, sum up and compress, after executing, tiles
        # sum up same numbers and move down, canmove changes to True
        # set canmove to False since in test3 it was changed to True
        self.g1.set_canmove(False)
        self.g1.set_matrix(self.m3)
        after = [[16, 32, 4, 64],
                 [2, 16, 16, 512],
                 [0, 0, 0, 256],
                 [0, 0, 0, 0]]
        self.g1.move_down()
        self.assertEqual(self.g1.matrix, after)
        self.assertTrue(self.g1.canmove)
        
        # score accumulates = 80+64 = 144
        self.assertEqual(self.g1.score, 144)
    
    def test_cur_move(self):
        
        '''
        method to test the check_curmove method in class Game. The method
        execute add_tile(), if self.canmove attribute is True. This test
        use the setter for canmove and test if add_tile() will executed using
        total() and not_zero_count() methods to see if one new non-zero 2 or 4
        tile is added to replace one 0 tile
        Pre-condition:
        canmove attribute is a bool
        matrix must be a nested list where the number of elements
        and elements in the element are equal with dimensions size x size, 
        all numbers in list should be 0 or power to 2 numbers from 2 to 2048
        Post condition:
        if canmove is True, a new tile 2 or 4 will replace 0, 
        if False, no change
        '''
        
        # set canmove attribute to True
        self.g1.set_canmove(True)
        before_total = self.g1.total()
        before_count = self.g1.not_zero_count()
        self.g1.check_curmove()
        after_total = self.g1.total()
        after_count = self.g1.not_zero_count()
                
        # test 1, if the difference of count is 1 and total sum 2 or 4 more
        self.assertEqual(after_count - before_count, 1)
        self.assertIn(after_total - before_total, self.tile)
        
        # set canmove attribute to False
        self.g1.set_canmove(False)
        before_total = self.g1.total()
        before_count = self.g1.not_zero_count()
        self.g1.check_curmove()
        after_total = self.g1.total()
        after_count = self.g1.not_zero_count()
                
        # test 2, if no difference on counts and total sums
        self.assertEqual(after_count, before_count)
        self.assertEqual(after_total, before_total)
        
    def test_game_win(self):
        
        '''
        test the game_win method of class Game, should update the win 
        attribute to True if number 2048 found in attribute matrix
        test by checking win if 2048 found
        '''
        
        # test1, if all 0 tiles matrix, after executing game_win method
        # win attribute should not change and stay False
        self.g1.game_win()
        self.assertFalse(self.g1.win)
        
        # test2, for the real game case, set a matrix, if no 2048 in game
        # board, after executing game_win method, win attribute stay False
        self.g1.set_matrix(self.m1)
        self.g1.game_win()
        self.assertFalse(self.g1.win)
        
        # test3, set a win case matrix, 2048 in game board
        # after executing game_win method, win attribute will change to True
        win = [[2048, 2, 0, 2],
               [8, 0, 2, 0],
               [4, 4, 4, 64],
               [0, 0, 256, 0]]
        self.g1.set_matrix(win)
        self.g1.game_win()
        self.assertTrue(self.g1.win)
        
        # test4, set another win case matrix(all non-zero tiles), 2048 in game
        # board, after executing game_win, win attribute will change to True
        win = [[2048, 2, 8, 2, 4],
               [8, 16, 2, 256, 128],
               [4, 4, 4, 64, 128],
               [128, 512, 256, 4, 64],
               [128, 512, 256, 4, 8]]
        self.g3.set_matrix(win)
        self.g3.game_win()
        self.assertTrue(self.g3.win)
    
    def test_game_over(self):
        
        '''
        test the game_over method of class Game, should update the over
        attribute to True if win attribute is not True and no 0 found in 
        and no possible move of matrix
        test by checking over if above condition is met
        '''
        
        # test1, if all 0 tiles matrix, after executing game_win method
        # win attribute should not change and stay False
        self.g1.game_over()
        self.assertFalse(self.g1.over)
        
        # test2, for real game case, set a matrix, if not all tiles filled,
        # after executing game_over method, over attribute stay False
        self.g1.set_matrix(self.m1)
        self.g1.game_over()
        self.assertFalse(self.g1.over)
        
        # test3, for real game case, set a matrix, if all tiles filled,
        # but possible horizonal move left, over attribute stay False
        mat = [[2, 2, 64, 2],
               [8, 4, 2, 128],
               [4, 32, 4, 64],
               [8, 16, 256, 512]]
        self.g1.set_matrix(mat)
        self.g1.game_over()
        self.assertFalse(self.g1.over)
        
        # test4, for real game case, set a matrix, if all tiles filled,
        # but possible vertical move left, over attribute stay False
        mat = [[2, 8, 64, 2],
               [2, 4, 2, 128],
               [4, 32, 4, 64],
               [8, 16, 256, 512]]
        self.g1.set_matrix(mat)
        self.g1.game_over()
        self.assertFalse(self.g1.over)
        
        # test5, for real game case, set a matrix, if all tiles filled,
        # no any possible move left, over attribute will change to True
        mat = [[2, 8, 64, 2],
               [16, 4, 2, 128],
               [4, 32, 4, 64],
               [8, 16, 256, 512]]
        self.g1.set_matrix(mat)
        self.g1.game_over()
        self.assertTrue(self.g1.over)
        
        # test6, set a win case matrix(all non-zero tiles and no more possible
        # move) after executing game_win/game_over, over attribute stay False
        # (game_over method doesn't change over attribute if already win)
        win = [[2048, 2, 8, 2, 4],
               [8, 16, 32, 256, 512],
               [4, 32, 4, 64, 128],
               [256, 512, 256, 4, 64],
               [128, 32, 2, 16 , 8]]
        self.g3.set_matrix(win)
        self.g3.game_win()
        self.g3.game_over()
        self.assertFalse(self.g3.over)
        
    def test_check_status(self):
        
        '''
        test check_status method of class Game that execute game_win,
        check_curmove, game_over method that checks the status of current game
        board. Test by executing move methods(tested above) and execute 
        check_status to see if result is as expected.
        '''
        
        # test1, with right move, no change on matrix, win/over will be False
        # canmove is False after move methods, no tile added, score is 0
        mat = [[0, 16, 64, 8],
               [0, 8, 2, 128],
               [0, 0, 4, 64],
               [8, 16, 256, 16]] 
        self.g1.set_matrix(mat)
        self.g1.move_right()
        self.assertFalse(self.g1.canmove)
        before_count = self.g1.not_zero_count()
        before_total = self.g1.total()
        self.g1.check_status()
        self.assertFalse(self.g1.win)
        self.assertFalse(self.g1.over)
        self.assertEqual(self.g1.total(), before_total)
        self.assertEqual(self.g1.not_zero_count(), before_count)
        self.assertEqual(self.g1.score, 0)
        
        # test2, with up move, all tiles position change, canmove is True, 
        # win/over False, tile added, score no change(no sum)
        self.g1.move_up()
        self.assertTrue(self.g1.canmove)
        self.g1.check_status()
        self.assertFalse(self.g1.win)
        self.assertFalse(self.g1.over)
        self.assertIn(self.g1.total() - before_total, self.tile)
        self.assertEqual(self.g1.not_zero_count() - before_count, 1)
        self.assertEqual(self.g1.score, 0)
        
        # test3, after the down move, possible sum up, canmove to True
        # then player losses game, check over attribute is True, 
        # win False, if matrix has one tile added, score increased by 64
        mat = [[1024, 16, 64, 8],
               [16, 8, 2, 128],
               [4, 32, 4, 32],
               [8, 16, 256, 32]]
        self.g1.set_matrix(mat)
        self.g1.move_down()
        self.assertTrue(self.g1.canmove)
        before_count = self.g1.not_zero_count()
        before_total = self.g1.total()
        self.g1.check_status()
        self.assertFalse(self.g1.win)
        self.assertTrue(self.g1.over)
        self.assertIn(self.g1.total() - before_total, self.tile)
        self.assertEqual(self.g1.not_zero_count() - before_count, 1)
        self.assertEqual(self.g1.score, 64)
        
        # test4, after the left move, sum up two 1024, canmove to True, 
        # player wins, check win attribute, if matrix has one tile added
        # and over attribute is False, score increased by 2048
        mat = [[1024, 1024, 64, 8, 0],
               [16, 8, 2, 128, 0],
               [4, 32, 4, 64, 0],
               [0, 16, 2, 4, 16],
               [0, 0, 0, 0, 0]]
        self.g3.set_matrix(mat)
        self.g3.move_left()
        self.assertTrue(self.g3.canmove)
        before_count = self.g3.not_zero_count()
        before_total = self.g3.total()
        self.g3.check_status()
        self.assertTrue(self.g3.win)
        self.assertFalse(self.g3.over)
        self.assertIn(self.g3.total() - before_total, self.tile)
        self.assertEqual(self.g3.not_zero_count() - before_count, 1)
        self.assertEqual(self.g3.score, 2048)

# execute the tests
def main():
    unittest.main()

if __name__ == "__main__":
    main()
