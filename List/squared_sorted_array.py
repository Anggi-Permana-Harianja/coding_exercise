'''
https://leetcode.com/problems/squares-of-a-sorted-array/

Time: O(N)
Space: O(N)

Hint: use window index
'''

def sorted_squares(nums: list[int]) -> list[int]:
    left_idx = 0
    right_idx = len(nums) - 1
    result = []
    
    while left_idx <= right_idx:
        left_squared = nums[left_idx] ** 2
        right_squared = nums[right_idx] ** 2
        if left_squared >= right_squared:
            result = [left_squared] + result
            left_idx += 1
        else:
            result = [right_squared] + result
            right_idx -= 1
            
    return result

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [-4,-1,0,3,10]
        result = [0,1,9,16,100]
        
        self.assertEqual(sorted_squares(nums), result)
        
    def test_program2(self):
        nums = [-7,-3,2,3,11]
        result = [4,9,9,49,121]
        
        self.assertEqual(sorted_squares(nums), result)

        
if __name__ == '__main__':
    unittest.main()