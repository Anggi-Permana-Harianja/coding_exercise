'''
https://leetcode.com/problems/move-zeroes/

Time: O(N)
Space: O(1) because in-place computation

Hint:
    - count zero appearances
    - do in two parts: 
        - move non-zeros to left
        - replace rightmost with zeros
    - be careful with edge cases
'''

def move_zeros(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return nums
    
    first_idx = 0
    second_idx = 0
    len_ = len(nums) - 1
    
    ''' count zero appearances '''
    cnt_null = nums.count(0)
    if cnt_null == 0:
        return nums
    
    ''' move non-zeros to left '''
    while second_idx <= len_:
        if nums[second_idx] != 0:
            nums[first_idx] = nums[second_idx]
            first_idx += 1
        second_idx += 1
    
    ''' replace rightmost with zeros '''
    i = 0
    while cnt_null > 0:
        nums[len_ - i] = 0
        i += 1
        cnt_null -= 1
        
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