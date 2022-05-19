#Link: https://www.algoexpert.io/questions/Kadane's%20Algorithm

#Time: O(n)
#Space: O(1)

def kadane_algorithm(array: list) -> int:
    max_so_far = array[0]
    max_overall = array[0]
    
    for i in range(1, len(array)):
        max_so_far = max(max_so_far + array[i], array[i])
        max_overall = max(max_overall, max_so_far)
        
    return max_overall

import unittest 
class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
        
        result = 19
        
        self.assertEqual(kadane_algorithm(array), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        result = 55
        
        self.assertEqual(kadane_algorithm(array), result)
        
    def test_program3(self):
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        
        result = -1
        
        self.assertEqual(kadane_algorithm(array), result)
        
if __name__ == '__main__':
    unittest.main()
