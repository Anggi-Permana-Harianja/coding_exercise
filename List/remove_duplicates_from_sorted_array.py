'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Time: O(N)
Space: O(1) since we compute in-place

Hint:
    - using two pointers
'''

def remove_duplicates(nums: list[int]) -> list[int]:
    first_idx = 0
    second_idx = 1
    
    while second_idx <= len(nums) - 1:
        if nums[first_idx] != nums[second_idx]:
            nums[first_idx + 1] = nums[second_idx]
            first_idx += 1
        second_idx += 1
        
    return nums[ : first_idx + 1]

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [1,1,2]
        
        result = [1, 2]
        
        self.assertEqual(remove_duplicates(nums), result)
        
    def test_program2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        
        result = [0,1,2,3,4]
        
        self.assertEqual(remove_duplicates(nums), result)
        
if __name__ == '__main__':
    unittest.main()