'''
Blind 75

https://www.algoexpert.io/questions/three-number-sum
https://leetcode.com/problems/3sum/

Time: O(N^2)
Space: O(N)

Hint:
    - Sort first
    - Use slide window technique
'''

from typing import *

class Solution:
    def three_sum(self, nums: List[int], target_sum: int) -> List[int]:
        result = []
        curr_idx = 0
        
        nums.sort()
        
        while curr_idx < len(nums):
            left_idx = curr_idx + 1 #no need to re-loop from same idx pair
            right_idx = len(nums) - 1
            
            while left_idx < right_idx:
                sums = nums[curr_idx] + nums[left_idx] + nums[right_idx]
                
                if sums == target_sum:
                    result.append([nums[curr_idx], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1    
                elif sums < target_sum:
                    left_idx += 1
                else:
                    right_idx -= 1
                    
            curr_idx += 1
            
        return result
                
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [12, 3, 1, 2, -6, 5, -8, 6]
        target_sum = 0
        
        solution = Solution()
        
        result = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        
        self.assertEqual(solution.three_sum(nums, target_sum), result)
    
    def test_program2(self):
        nums = [1, 2, 3]
        target_sum = 6
        
        solution = Solution()
        
        result = [[1, 2, 3]]
        
        self.assertEqual(solution.three_sum(nums, target_sum), result)
        
    def test_program3(self):
        nums = [1, 2, 3]
        target_sum = 7
        
        solution = Solution()
        
        result = []
        
        self.assertEqual(solution.three_sum(nums, target_sum), result)
        
if __name__ == '__main__':
     unittest.main()