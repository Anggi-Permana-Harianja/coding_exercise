"""
Blind 75
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Time: O(log n)
Space: O(1)
"""
from typing import List
import unittest

def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

class TestCase(unittest.TestCase):
    def test_case1(self):
        nums = [-1,0,3,5,9,12]
        target = 9

        return self.assertEqual(binary_search(nums, target), 4)
    
    def test_case2(self):
        nums = [-1,0,3,5,9,12]
        target = 2

        return self.assertEqual(binary_search(nums, target), -1)
    

if __name__== "__main__":
    unittest.main()
