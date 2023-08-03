"""
Blind 75

https://leetcode.com/problems/climbing-stairs/description/

Time: O(N)
Space: O(1) as we only store 2 variables (last_step and second_last_step)

Hint:
    - This is DP problem but works like a fibonacci
"""

import unittest

def climb_stairs(n: int) -> int:
    # define last 2 steps on the stair
    last_step, second_last_step = 1, 1

    for _ in range(n - 1):
        last_step, second_last_step = last_step + second_last_step, last_step

    return last_step

class TestCases(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(climb_stairs(2), 2)
    
    def test_case2(self):
        return self.assertEqual(climb_stairs(3), 3)
    
    def test_case3(self):
        return self.assertEqual(climb_stairs(5), 8)
    
if __name__ == "__main__":
    unittest.main()
