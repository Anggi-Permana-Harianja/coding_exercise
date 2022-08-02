'''
https://leetcode.com/problems/running-sum-of-1d-array/submissions/

Time: O(N)
Space: O(1)
'''

def running_sum(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
        
    return nums

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        array = [1, 2, 3]
        result = [1, 3, 6]
        
        self.assertEqual(running_sum(array), result)
        
    def test_program2(self):
        array = [1, 2, 3, 4]
        result = [1, 3, 6, 10]
        
        self.assertEqual(running_sum(array), result)
        
if __name__ == '__main__':
    unittest.main()

