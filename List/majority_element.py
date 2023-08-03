"""
Blind 75

https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Time: O(N)
Space: O(1)

Hint:
    - use Boyer-Moore Voting algorithm
"""

import unittest
from typing import List

def majority_elements(nums: List[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

class TestCases(unittest.TestCase):
    def test_case1(self):
        nums = [3, 2, 3]

        return self.assertEqual(majority_elements(nums), 3 )
    
    def test_case2(self):
        nums =  [2,2,1,1,1,2,2]

        return self.assertEqual(majority_elements(nums), 2)
    
if __name__ == "__main__":
    unittest.main()