# Link: https://leetcode.com/problems/maximum-subarray/

#53. Maximum Subarray

#Given an integer array nums, find the contiguous subarray (containing at least one number)
#which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

#HINT: This question can be solved using Kadane algorithm

#Time: O(N)
#Space: O(1)

def max_subarray(nums:list[int]) -> int:
    largest_so_far = nums[0]
    largest = largest_so_far
    
    for i in range(1, len(nums)):
        largest_so_far = max(largest_so_far + nums[i], nums[i])
        largest = max(largest, largest_so_far)
        
    return largest


import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        
        result = 6
        
        self.assertEqual(max_subarray(nums), result)
        
    def test_program2(self):
        nums = [1, 2, 3, -5]
        
        result = 6
        
        self.assertEqual(max_subarray(nums), result)
        
if __name__ == '__main__':
    unittest.main()