'''
https://leetcode.com/problems/valid-mountain-array/

Time: O(N)
Space: O(1)

Hint:
    - edge case where has no peak or has no valley
'''

def valid_mountain(arr: list[int]) -> bool:
    ''' cant make mountain if len < 3 '''
    if len(arr) < 3:
        return False
    
    max_idx = arr.index(max(arr))
    
    ''' edge cases where there is no valley or no mountain '''
    if max_idx == len(arr) - 1 or max_idx == 0:
        return False
    
    ''' check peak '''
    for i in range(1, max_idx + 1):
        if arr[i] <= arr[i - 1]:
            return False
        
    ''' check valley '''
    for i in range(max_idx, len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False
        
    return True

import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        arr = [2,1]
        
        result = False
        
        self.assertEqual(valid_mountain(arr), result)
        
    def test_program2(self):
        arr = [3, 5, 5]
        
        result = False
        
        self.assertEqual(valid_mountain(arr), result)
        
    def test_program3(self):
        arr = [0, 3, 2, 1]
        
        result = True
        
        self.assertEqual(valid_mountain(arr), result)
        
    def test_program4(self):
        arr = [1, 2, 3, 4, 3, 2, 1]
        
        result = True
        
        self.assertEqual(valid_mountain(arr), result)
        
if __name__ == '__main__':
    unittest.main()
        