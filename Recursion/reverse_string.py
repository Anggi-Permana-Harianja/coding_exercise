'''
https://leetcode.com/problems/reverse-string/

Time: O(N) because we solve this recursively
Space: O(N)

Hint:
    - This solution is recursive one, we can use sliding window as well
    - Solution done in-place, so there is no extra space
'''

from typing import *

class Solution:
    def reverse_string(self, s: List[str]) -> None:
        return self.helper(0, len(s) - 1, s)
    
    def helper(self, left, right, s):
        if left < right:
            s[left], s[right] = s[right], s[left]
            self.helper(left + 1, right - 1, s)
            
        return s
            
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        s = ['h', 'e', 'l', 'l', 'o']
        
        solution = Solution()
        
        result = ['o', 'l', 'l', 'e', 'h']
        
        self.assertEqual(solution.reverse_string(s), result)
        
    def test_program2(self):
        s = ['q', 'w', 'e', 'r', 't', 'y']
        
        solution = Solution()
        
        result = ['y', 't', 'r', 'e', 'w', 'q']
        
        self.assertEqual(solution.reverse_string(s), result)
        
if __name__ == '__main__':
    unittest.main()