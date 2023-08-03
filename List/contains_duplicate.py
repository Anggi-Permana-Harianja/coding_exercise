"""
Blind 75

https://leetcode.com/problems/contains-duplicate/description/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Time: O(N)
Space: O(N)

Hint:
    - one liner solution using set()
"""

import unittest
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    # Use set() to get unique elements
    return len(nums) > len(set(nums))

class TestCases(unittest.TestCase):
    def test_case1(self):
        nums = [1,2,3,1]

        return self.assertEqual(contains_duplicate(nums), True)
    
    def test_case2(self):
         nums = [1,2,3,4]

         return self.assertEqual(contains_duplicate(nums), False)
    
    def test_case3(self):
        nums = [1,1,1,3,3,4,3,2,4,2]

        return self.assertEqual(contains_duplicate(nums), True)
    
if __name__ == "__main__":
    unittest.main()