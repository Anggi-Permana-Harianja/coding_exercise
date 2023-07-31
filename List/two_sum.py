"""
Blind 75

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Time: O(N)
Space: O(N)

Hint:
    - using hash map
"""

import unittest
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # create hash map
    dict_ = {}

    for i, num in enumerate(nums):
        remains = target - num
        if remains in dict_:
            return [dict_[remains], i]
        dict_[num] = i

    return [-1, -1]

class TestCases(unittest.TestCase):
    def test_case1(self):
        nums = [2,7,11,15]
        target = 9

        return self.assertEqual(two_sum(nums, target), [0, 1])
    
    def test_case2(self):
        nums = [3,2,4]
        target = 6

        return self.assertEqual(two_sum(nums, target), [1, 2])
    
    def test_case3(self):
        nums = [3, 3]
        target = 6

        return self.assertEqual(two_sum(nums, target), [0, 1])
    
if __name__ == "__main__":
    unittest.main()
