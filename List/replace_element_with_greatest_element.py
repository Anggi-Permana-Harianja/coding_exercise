'''
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

Time: O(N)
Space: O(1)
'''

def replace_element(arr: list[int]) -> list[int]:
    idx = 0
    while idx < len(arr) - 1:
        arr[idx] = max(arr[idx + 1 : ])
        idx += 1
        
    arr[-1] = -1
    
    return arr

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        arr = [17,18,5,4,6,1]
        
        result = [18,6,6,6,1,-1]
        
        return self.assertEqual(replace_element(arr), result)
    
    def test_program2(self):
        arr = [1, 2, 3, 4]
        
        result = [4, 4, 4, -1]
        
        return self.assertEqual(replace_element(arr), result)
    
if __name__ == '__main__':
    unittest.main()