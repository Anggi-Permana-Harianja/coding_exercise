'''
https://leetcode.com/problems/max-consecutive-ones/

Time: O(N)
Space: O(1) 

Hint: using Kadane approach
'''

def find_max_consecutive_ones(nums: list[int]) -> int:
    current_consecutive = 0
    max_consecutive = 0
    
    for num in nums:
        if num == 0:
            max_consecutive = max(max_consecutive, current_consecutive)
            current_consecutive = 0
        else:
            current_consecutive += 1
            
    return max(max_consecutive, current_consecutive)

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [1,1,0,1,1,1]
        result = 3
        
        self.assertEqual(find_max_consecutive_ones(nums), result)
        
    def test_program2(self):
        nums = [0, 1, 1, 1, 0, 1, 1]
        result = 3
        
        self.assertEqual(find_max_consecutive_ones(nums), result)
        
if __name__ == '__main__':
    unittest.main()