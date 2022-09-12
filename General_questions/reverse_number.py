'''
Reverse number without convert it to List[str] at all

Time: O(N); N is length of number
Space: O(1)
'''

from typing import *

def reverse_number(num: int) -> int:
    result = 0
    while num:
        mod_ = num % 10
        num = num // 10
        result = (10 * result) + mod_
        
    return result

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        num = 123
        
        result = 321
        
        self.assertEqual(reverse_number(num), result)
        
    def test_program2(self):
        num = 123456789
        
        result = 987654321
        
        self.assertEqual(reverse_number(num), result)
        
    def test_program3(self):
        num = 100
        
        result = 1
        
        self.assertEqual(reverse_number(num), result)
        
    def test_program4(self):
        num = 10000
        
        result = 1
        
        self.assertEqual(reverse_number(num), result)
        
if __name__ == '__main__':
    unittest.main()
        