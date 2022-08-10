'''
https://leetcode.com/problems/remove-element/

Time: O(N)
Space: O(1) since only keep counting the un-removed elements

Hint:
    - Using two pointers
'''

def remove_element(nums: list[int], val: int) -> int:
    first_idx = 0
    second_idx = 0
    
    while second_idx <= len(nums) - 1:
        if nums[second_idx] != val:
            nums[first_idx] = nums[second_idx]
            first_idx += 1
        second_idx += 1
        
    return nums[:first_idx]

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [3, 2, 2, 3]
        val = 3
        
        result = [2, 2]
        
        self.assertEqual(remove_element(nums, val), result)
        
    def test_program2(self):
        nums = [0,1,2,2,3,0,4,2]
        val = 2
        
        result = [0, 1, 3, 0, 4]
        
        self.assertEqual(remove_element(nums, val), result)
        

if __name__ == '__main__':
    unittest.main()

