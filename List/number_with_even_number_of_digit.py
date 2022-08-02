'''
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Time: O(N)
Space: O(1)
'''

def find_number(nums: list[int]) -> int:
    return sum([1 if len(str(num)) % 2 == 0 else 0 for num in nums])

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        nums = [12,345,2,6,7896]
        result = 2
        
        self.assertEqual(find_number(nums), result)
        
    def test_program2(self):
        nums = [555,901,482,1771]
        result = 1
        
        self.assertEqual(find_number(nums), result)
        
if __name__ == '__main__':
    unittest.main()