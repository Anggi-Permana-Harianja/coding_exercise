'''
https://leetcode.com/problems/duplicate-zeros/

Time: O(N)
Space: O(1) because the constraint of this question is to have in-place computing

hint: 
    - loop backwards
    - if idx + shift < len(arr) then shift it to rightmost
'''

def duplicate_zeros(arr: list[int]) -> list[int]:
    shift = 0
    len_ = len(arr)
    
    ''' count possible shift by count 0 appearances '''
    for num in arr:
        if num == 0:
            shift += 1
            
    for i in range(len_ - 1, -1, -1):
        ''' shift to rightmost if possible '''
        if i + shift < len_:
            arr[i + shift] = arr[i]
        ''' if meet 0, shift to rightmost by adding 0 if possible, substract shift '''
        if arr[i] == 0:
            shift -= 1
            if i + shift < len_:
                arr[i + shift] = 0
                
    return arr
                
import unittest

class TestProgram(unittest.TestCase):
    def test_program1(self):
        arr = [1,0,2,3,0,4,5,0] 
        result = [1,0,0,2,3,0,0,4]
        
        self.assertEqual(duplicate_zeros(arr), result)
        
    def test_program2(self):
        arr = [1, 2, 3]
        result = [1, 2, 3]
        
        self.assertEqual(duplicate_zeros(arr), result)
        
    def test_program3(self):
        arr = [1, 2, 3, 4, 0, 0]
        result = [1, 2, 3, 4, 0, 0]
        
        self.assertEqual(duplicate_zeros(arr), result)
        
if __name__ == '__main__':
    unittest.main()