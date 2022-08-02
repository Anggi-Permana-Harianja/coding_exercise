'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solution/

Time: O(log N)
Space: O(1)
'''

def number_of_steps(num: int) -> int:
    if num == 0:
        return 0
    
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        steps += 1
        
    return steps

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        num = 14
        result = 6
        
        self.assertEqual(number_of_steps(num), result)
        
    def test_program2(self):
        num = 8
        result = 4
        
        self.assertEqual(number_of_steps(num), result)
        
if __name__ == '__main__':
    unittest.main()
    
