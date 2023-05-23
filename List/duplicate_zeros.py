'''
https://leetcode.com/problems/duplicate-zeros/

Time: O(N)
Space: O(1) because the constraint of this question is to have in-place computing

hint: 
    - expand the array
    - loop backwards
    - simple use of copy
'''

def duplicate_zeros(array: list[int]) -> list[int]:
    len_ = len(array)
    zeros_count = array.count(0)
    final_len = len_ + zeros_count

    last_index = len_ - 1
    final_index = final_len - 1

    # expand the array
    if final_len > len_:
        array[len_:] = array + ([0] * zeros_count)
    
    # slide backwards
    while last_index != final_index and zeros_count >= 0:
        # copy value == 0 and slide backwards, substract count_zeros
        if array[last_index] == 0:
            array[final_index] = 0
            final_index -= 1
            zeros_count -= 1

        # copy value from last_index to final_index
        array[final_index] = array[last_index]
        final_index -= 1
        last_index -= 1

    # return only neccesary length
    return array[:len_]
                
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
