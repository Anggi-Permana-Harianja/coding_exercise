'''
https://leetcode.com/problems/check-if-n-and-its-double-exist/

Time: O(N)
Space: O(1) since we use dictionary

Hint:
    - 0 is an edge case
    - use Set to make sure there is no duplicate first
'''

def check_if_exists(arr: list[int]) -> bool:
    seen = set()

    for num in arr:
        if num * 2 in seen or num / 2 in seen:
            return True
        seen.add(num)
        
    return False

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        arr = [4,-7,11,4,18]
        
        result = False
        
        self.assertEqual(check_if_exists(arr), result)
        
    def test_program2(self):
        arr = [7,1,14,11]
        
        result = True
        
        self.assertEqual(check_if_exists(arr), result)
        
    def test_program3(self):
        arr = [3,1,7,11]
        
        result = False
        
        self.assertEqual(check_if_exists(arr), result)
        
        
if __name__ == '__main__':
    unittest.main()
        