'''
https://leetcode.com/problems/move-zeroes/

Time: O(N)
Space: O(1) because in-place computation

Hint:
    - use two pointers
    - swap
'''

def move_zeros(nums: list[int]) -> list[int]:
    first_idx = 0
    second_idx = 0

    while second_idx < len(nums):
        if nums[second_idx] != 0:
            # swap
            nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
            first_idx += 1
        second_idx += 1

    return nums

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [45192,0,-659,-52359,-99225,-75991,0,-15155,27382,59818,0,-30645,-17025,81209,887,64648]
        
        result = [45192,-659,-52359,-99225,-75991,-15155,27382,59818,-30645,-17025,81209,887,64648,0,0,0]

        self.assertEqual(move_zeros(nums), result)
        
    def test_program2(self):
        nums = [0,1,0,3,12]
        
        result = [1,3,12,0,0]
        
        self.assertEqual(move_zeros(nums), result)
        
    def test_program3(self):
        nums = [1, 2]
        
        result = [1, 2]
        
        self.assertEqual(move_zeros(nums), result)
        

if __name__ == '__main__':
    unittest.main()