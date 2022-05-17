#Link: https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph

#Time: O(m * n)
#Space: O(m * n)

#Hint: Using padded matrix, the total ways to padded_matrix[row][col] = padded_matrix[row - 1][col] + padded_matrix[row][col - 1]

def num_of_ways_to_traverse_graph(width: list, height: list) -> int:
    #initialize padded matrix
    padded_matrix = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    padded_matrix[1][1] = 1
    
    for row in range(1, len(padded_matrix)):
        for col in range(1, len(padded_matrix[0])):
            if row == 1 and col == 1:
                pass
            else:
                padded_matrix[row][col] = padded_matrix[row - 1][col] + padded_matrix[row][col - 1]
    
    return padded_matrix[-1][-1]

import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        width = 4
        height = 3
        
        result = 10
        
        self.assertEqual(num_of_ways_to_traverse_graph(width, height), result)
        
    def test_program2(self):
        width = 7
        height = 5
        
        result = 210
        
        self.assertEqual(num_of_ways_to_traverse_graph(width, height), result)
        
    def test_program3(self):
        width = 1
        height = 2
        
        result = 1
        
        self.assertEqual(num_of_ways_to_traverse_graph(width, height), result)
        
if __name__ == '__main__':
    unittest.main()