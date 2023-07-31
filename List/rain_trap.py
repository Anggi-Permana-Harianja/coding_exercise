"""
Blind 75

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented
by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

hint: 
    - use two pointers
    - it uses simple sliding window
    - keep track left_max and right_max values

Time: O(N)
Space: O(N)
"""

def rain_trap(heights: list[int]) -> int:
    # edge case
    if len(heights) < 3:
        return 0
    
    left, right = 0, len(heights) - 1
    left_max = right_max = water_trap = 0

    while left < right:
        # compute on left hand side, starts if left is lower than right
        if heights[left] < heights[right]:
            # compute how much water can be hold
            if heights[left] > left_max:
                left_max = heights[left]
            else:
                water_trap += left_max - heights[left]
            left += 1
        # compute the same thing for right hand side
        else:
            if heights[right] > right_max:
                right_max = heights[right]
            else:
                water_trap += right_max - heights[right]
            right -= 1

    return water_trap

import unittest

class TestProgram(unittest.TestCase):
    def test_case1(self):
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]

        return self.assertEqual(rain_trap(heights), 6)

    def test_case2(self):
        heights = [4,2,0,3,2,5]

        return self.assertEqual(rain_trap(heights), 9)
    
    def test_case3(self):
        heights = [4, 3, 2, 1, 5, 2, 0, 1]

        return self.assertEqual(rain_trap(heights), 7)


if __name__ == "__main__":
    unittest.main() 
