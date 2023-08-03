"""
Blind 75

Link: https://www.algoexpert.io/questions/Spiral%20Traverse
https://leetcode.com/problems/spiral-matrix/

Time: O(n)
Space: O(n)

Hint:
    - Use 4 loops (move right, go down, move left, go up)
    - Be careful with indexing
"""

def spiral_traverse(array: list) -> list:
    if len(array) == 1:
        return 1
    
    result = []
    
    start_row, end_row = 0, len(array) - 1
    start_col, end_col = 0, len(array[0]) - 1
    
    while start_row <= end_row and start_col <= end_col:
        #move right
        for col in range(start_col, end_col + 1):
            result.append(array[start_row][col])
            
        #go down
        for row in range(start_row + 1, end_row + 1):
            result.append(array[row][end_col])
            
        #move left 
        for col in reversed(range(start_col, end_col)):
            #prevent visited
            if start_row == end_row:
                break
            result.append(array[end_row][col])
        
        #go up
        for row in reversed(range(start_row + 1, end_row)):
            #prevent visited
            if start_col == end_col:
                break
            result.append(array[row][start_col])
        
        #iterate until we reach centre
        start_row, end_row = start_row + 1, end_row - 1
        start_col, end_col = start_col + 1, end_col - 1
        
    return result

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]
        
        result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        
        self.assertEqual(spiral_traverse(array), result)
        
    def test_program2(self):
        array = [
    [19, 32, 33, 34, 25, 8],
    [16, 15, 14, 13, 12, 11],
    [18, 31, 36, 35, 26, 9],
    [1, 2, 3, 4, 5, 6],
    [20, 21, 22, 23, 24, 7],
    [17, 30, 29, 28, 27, 10]
  ]
        result = [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24, 23, 22, 21, 2, 31, 36, 35, 4, 3]
        
        self.assertEqual(spiral_traverse(array), result)
        
    def test_program3(self):
        array = [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
  ]
        result = [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]
        
        self.assertEqual(spiral_traverse(array), result)
        
if __name__ == '__main__':
    unittest.main()
            