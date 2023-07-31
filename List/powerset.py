"""
Blind 75 

Link: https://www.algoexpert.io/questions/Powerset

Time: O(N * 2 ^ N)
Space: O(N * 2 ^ N)
"""

def powerset(array: list) -> list:
    result = [[]]
    
    for num in array:
        len_ = len(result)
        for i in range(len_):
            subset = result[i]
            result.append([num] + subset)
            
    return result

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [1, 2]
        
        result = [[], [1], [2], [2, 1]]
        
        self.assertEqual(powerset(array), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4]
        
        result = [[], [1], [2], 
                  [2, 1], [3], 
                  [3, 1], [3, 2],
                  [3, 2, 1],
                  [4], [4, 1],
                  [4, 2], [4, 2, 1],
                  [4, 3], [4, 3, 1],
                  [4, 3, 2], 
                  [4, 3, 2, 1]]
        
        self.assertEqual(powerset(array), result)
        
        
if __name__ == '__main__':
    unittest.main()