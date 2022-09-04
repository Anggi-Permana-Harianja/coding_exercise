'''
Daily Coding Problem: Problem #1178 [Easy]

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
'''

from typing import *

class Solution:
    def collatz(self, n: int) -> bool:
        while n != 1 and n > 0:
            if n % 2 == 0:
                n /= 2
            else:
                n = (3 * n) + 1
        
        return True
    
import unittest
class TestProgram(unittest.TestCase):
    def test_program1(self):
        n = 100
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.collatz(n), result)
        
    def test_program2(self):
        n = 1991
        
        solution = Solution()
        
        result = True
        
        self.assertEqual(solution.collatz(n), result)
        
if __name__ == '__main__':
    unittest.main()